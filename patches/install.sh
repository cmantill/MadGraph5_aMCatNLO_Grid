#!/bin/bash

version=$1
#exit on first error
set -e

RUNHOME=`pwd`

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release

AFSFOLD=${RUNHOME}/${name}
AFS_GEN_FOLDER=${RUNHOME}/${name}
CARDSDIR=${RUNHOME}/${carddir}

MGBASEDIR=mgbasedir

#MG=MG5_aMC_v2_5_2.tar.gz
#MG=MG5_aMC_v2_5_1.tar.gz
#MG=MG5_aMC_v2_5_3.tar.gz
#MG=MG5_aMC_v2.4.3.tar.gz
MG=MG5_aMC_v${version}.tar.gz
#MGSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$MG
#MGSOURCE=$MGSOURCE/$MG
MGSOURCE=/afs/cern.ch/work/p/pharris/public/$MG

#syscalc is a helper tool for madgraph to add scale and pdf variation weights for LO processes
SYSCALC=SysCalc_V1.1.0.tar.gz
SYSCALCSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$SYSCALC
SYSCALCSOURCE=$SYSCALC

#MGBASEDIRORIG=MG5_aMC_v2_5_3
#MGBASEDIRORIG=MG5_aMC_v2_5_1
#MGBASEDIRORIG=MG5_aMC_v2_4_3
MGBASEDIRORIG=MG5_aMC_v${version}
#MGBASEDIRORIG=MG5_aMC_v2_5_2

isscratchspace=0
user=`id -u -n`
#if [ ! -d "/tmp/$user/CMSSW_7_1_25_patch5" ]; then
#    cd /tmp/$user
#    scramv1 project CMSSW CMSSW_7_1_25_patch5
#fi 
#cd /tmp/$user/CMSSW_7_1_25_patch5/src
#if [ ! -d "/tmp/$user/CMSSW_7_1_20" ]; then
#    cd /tmp/$user
#    scramv1 project CMSSW CMSSW_7_1_20
#fi 
#cd /tmp/$user/CMSSW_7_1_20/src
#cd /afs/cern.ch/user/p/pharris/pharris/public/bacon/prod/CMSSW_7_1_20/src

export SCRAM_ARCH=slc6_amd64_gcc530
if [ ! -d "/tmp/$user/CMSSW_9_0_0_pre2" ]; then
    cd /tmp/$user
    scramv1 project CMSSW CMSSW_9_3_0_pre1
fi 
cd /tmp/$user/CMSSW_9_3_0_pre1/src
eval `scramv1 runtime -sh`
cd $RUNHOME
echo $CMSSW_BASE

#Copy, Unzip and Delete the MadGraph tarball#
#wget --no-check-certificate ${MGSOURCE}
cp ${MGSOURCE} .
tar xzf ${MG}
rm $MG

#Apply any necessary patches on top of official release
#patch -l -p0 -i $RUNHOME/patches/mgfixes.patch
#patch -l -p0 -i $RUNHOME/patches/models.patch
cd $MGBASEDIRORIG
LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
if [ -e $LHAPDF6TOOLFILE ]; then
    LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
else
    LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`
fi
#make sure env variable for pdfsets points to the right place
export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`
LHAPDFINCLUDES=`$LHAPDFCONFIG --incdir`
LHAPDFLIBS=`$LHAPDFCONFIG --libdir`
cd $CMSSW_BASE/src/
BOOSTINCLUDES=`scram tool tag boost INCLUDE`
cd -
echo  $LHAPDFCONFIG
#echo "set auto_update 0"                  >  mgconfigscript
#echo "set automatic_html_opening False"   >> mgconfigscript
#echo "set output_dependencies internal"   >> mgconfigscript
echo "set lhapdf $LHAPDFCONFIG"           >> mgconfigscript
if [ -n "$queue" ]; then
    echo "set run_mode  1"                 >> mgconfigscript
    echo "set cluster_type lsf"            >> mgconfigscript
    echo "set cluster_queue $queue"        >> mgconfigscript
    echo "set cluster_status_update 60 30" >> mgconfigscript
    echo "set cluster_nb_retry 5"          >> mgconfigscript
    echo "set cluster_retry_wait 300"      >> mgconfigscript 
    if [[ ! "$RUNHOME" =~ ^/afs/.* ]]; then
        echo "local path is not an afs path, batch jobs will use worker node scratch space instead of afs"
        echo "set cluster_temp_path `echo $RUNHOME`" >> mgconfigscript 
        isscratchspace=1
    fi      
else
    echo "set run_mode 2" >> mgconfigscript
fi
echo "save options" >> mgconfigscript
./bin/mg5_aMC mgconfigscript
cp ../patches/mg5_configuration.txt input
rm mgconfigscript
mv HEPTools/collier HEPTools/collier_sucks
#get syscalc and compile
#wget --no-check-certificate ${SYSCALCSOURCE}
cp /afs/cern.ch/cms/generators/www/${SYSCALCSOURCE} .
tar xzf ${SYSCALC}
rm $SYSCALC
cd SysCalc
sed -i "s#INCLUDES =  -I../include#INCLUDES =  -I../include -I${LHAPDFINCLUDES} -I${BOOSTINCLUDES}#g" src/Makefile
sed -i "s#LIBS = -lLHAPDF#LIBS = ${LHAPDFLIBS}/libLHAPDF.a #g" src/Makefile
make
cd ..
cd $WORKDIR

