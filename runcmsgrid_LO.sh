#!/bin/bash

nevt=${1}
echo "%MSG-MG5 number of events requested = $nevt"

rnum=${2}
echo "%MSG-MG5 random seed used for the run = $rnum"

ncpu=${3}
echo "%MSG-MG5 number of cpus = $ncpu"

LHEWORKDIR=`pwd`

cd process

#make sure lhapdf points to local cmssw installation area
LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`

#if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
if [ -e $LHAPDF6TOOLFILE ]; then
  LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
fi

#make sure env variable for pdfsets points to the right place
export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`

echo "lhapdf = $LHAPDFCONFIG" >> ./madevent/Cards/me5_configuration.txt
# echo "cluster_local_path = `${LHAPDFCONFIG} --datadir`" >> ./madevent/Cards/me5_configuration.txt

if [ "$ncpu" -gt "1" ]; then
  echo "run_mode = 2" >> ./madevent/Cards/me5_configuration.txt
  echo "nb_core = $ncpu" >> ./madevent/Cards/me5_configuration.txt
fi

#generate events
./run.sh $nevt $rnum

domadspin=0
if [ -f ./madspin_card.dat ] ;then
    domadspin=1
    echo "import events.lhe.gz" > madspinrun.dat
    rnum2=$(($rnum+1000000))
    echo `echo "set seed $rnum2"` >> madspinrun.dat
    cat ./madspin_card.dat >> madspinrun.dat
    cat madspinrun.dat | $LHEWORKDIR/mgbasedir/MadSpin/madspin
fi

cd $LHEWORKDIR

if [ "$domadspin" -gt "0" ] ; then 
    mv process/events_decayed.lhe.gz events_presys.lhe.gz
else
    mv process/events.lhe.gz events_presys.lhe.gz
fi

gzip -d events_presys.lhe.gz


#run syscalc to populate pdf and scale variation weights
echo "
# Central scale factors
scalefact:
1 2 0.5
# choice of correlation scheme between muF and muR
# set here to reproduce aMC@NLO order
scalecorrelation:
0 3 6 1 4 7 2 5 8
" > syscalc_card.dat
sed "s@\<rwgt\>*\<\/rwgt\>@@g" events_presys.lhe > events_presys_tmp.lhe
sed -e 's/(<rwgt>)(.*)(<\/rwgt>)//g' events_presys.lhe > events_presys_tmp.lhe
cat events_presys.lhe | perl -pe  's/\<wgt.*wgt\>\n//'  | perl -pe  's/\<rwgt\>\n//' | perl -pe 's/\<\/rwgt\>\s*\n//' | sed "s@&@@g"   > events_presys_tmp.lhe
LD_LIBRARY_PATH=`${LHAPDFCONFIG} --libdir`:${LD_LIBRARY_PATH} ./mgbasedir/SysCalc/sys_calc events_presys_tmp.lhe syscalc_card.dat cmsgrid_final.lhe

#reweight if necessary
if [ -e process/madevent/Cards/reweight_card.dat ]; then
    echo "reweighting events"
    mv cmsgrid_final.lhe process/madevent/Events/GridRun_${rnum}/unweighted_events.lhe
    export LIBRARY_PATH=$LD_LIBRARY_PATH 
    cd process/madevent
    ./bin/madevent reweight  GridRun_${rnum}
    cd ../..
    mv process/madevent/Events/GridRun_${rnum}/unweighted_events.lhe.gz cmsgrid_final.lhe.gz
    gzip -d  cmsgrid_final.lhe.gz
fi

ls -l
echo

exit 0