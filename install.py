#! /usr/bin/env python
import commands,sys,os,subprocess,stat,math,pwd
import datetime
import time 
from os import listdir
from os.path import isfile, join
from optparse import OptionParser
import argparse
import random

eos='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select'
#MGrelease="2_5_2"
MGrelease="2_5_1"
#MGrelease="2_4_3"

def completed(name,medrange,dmrange,basedir,carddir):
    completed = True
    for med in medrange:
        for dm in dmrange:
            if med < dm: 
                continue
            fileExists=os.path.isfile('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s_%s_%s/process/run.sh' % (basedir,name,name,med,dm)) 
            if fileExists:
                madgraph='%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s_%s_%s/mgbasedir' % (basedir,name,name,med,dm)
                process ='%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s_%s_%s/process'   % (basedir,name,name,med,dm)
                runcms  ='%s/runcmsgrid.sh'                           % (basedir)
                output  ='%s_%s_%s_tarball.tar.xz'                    % (name,med,dm)
                os.system('XZ_OPT="--lzma2=preset=9,dict=512MiB" tar -cJpsf '+output+' '+madgraph+' '+process+' '+runcms)
            else:
                if not os.path.isfile('MG_%s_%s_%s.tgz' % (name,med,dm)):
                    completed = False
    return completed

def replace(name,med,dm,gdm,gq,proc,rand,directory):
    #Avoid restrict cards
    if gq == 1:
        gq=9.999999e-1
    if gdm == 1:
        gdm=9.999999e-1
    if dm==1:
        dm=9.999999e-1
    gqS=gq
    gqP=gq
    gdmS=gdm
    gdmP=gdm
    gqV=gq
    gqA=gq
    #Diagonals for monotop (set it to 0 for now)
    gqVii=0
    gqAii=0
    gdmV=gdm
    gdmA=gdm
    gSw=gq*(80.19)*math.sqrt(3.1419265/132.5/0.233)
    gPw=gq*(80.19)*math.sqrt(3.1419265/132.5/0.233)
    gSb=gq*(80.19)*math.sqrt(3.1419265/132.5/(1-0.233))
    gPb=gq*(80.19)*math.sqrt(3.1419265/132.5/(1-0.233))
    gSinTheta=gq
    gH=1
    print "!!!!!!!!!!!!!!!!",gdm,med,dm,gq,gdmS,gdmP
    if proc == 805:
        gqP=0#1e-99
        gdmP=0#1e-99
        gqV=0
        gqA=0
        gdmV=0
        gdmA=0
        gPw=0
        gPb=0
    elif proc == 806:
        gqS=0#1e-99
        gdmS=0#1e-99
        gqV=0
        gqA=0
        gdmV=0
        gdmA=0
        gSw=0
        gSb=0
        gSinTheta=0
    elif proc == 801:
        gqS=0
        gdmS=0
        gqP=0
        gdmP=0
        gqV=1e-99
        gdmV=1e-99
        gSw=0
        gSb=0
        gPw=0
        gPb=0
        gSinTheta=0
    else:
        gqS=0
        gdmS=0
        gqP=0
        gdmP=0
        gqA=1e-99
        gdmA=1e-99
        gSw=0
        gSb=0
        gPw=0
        gPb=0
        gSinTheta=0
    print "!!!!!!!!!!!!!!!!",gdm,med,dm,gq,gdmS,gdmP
    parameterfiles = [ f for f in listdir(directory) if isfile(join(directory,f)) ]    
    for f in parameterfiles:
         with open('%s/%s_tmp' % (directory,f),"wt") as fout: 
            with open(directory+'/'+f        ,"rt") as fin: 
                for line in fin:
                    tmpline =    line.replace('X_MMED_X' ,str(med))
                    tmpline = tmpline.replace('X_MMED2_X',str(max(med,400.)))
                    tmpline = tmpline.replace('X_MDM_X' ,str(float(dm)))
                    tmpline = tmpline.replace('X_gS_X'  ,str(gqS))
                    tmpline = tmpline.replace('X_gP_X'  ,str(gqP))
                    tmpline = tmpline.replace('X_gDMS_X',str(gdmS))
                    tmpline = tmpline.replace('X_gDMP_X',str(gdmP))
                    tmpline = tmpline.replace('X_gV_X'  ,str(gqV))
                    tmpline = tmpline.replace('X_gA_X'  ,str(gqA))
                    tmpline = tmpline.replace('X_gVii_X',str(gqVii))
                    tmpline = tmpline.replace('X_gAii_X',str(gqAii))
                    tmpline = tmpline.replace('X_gDMV_X',str(gdmV))
                    tmpline = tmpline.replace('X_gDMA_X',str(gdmA))
                    tmpline = tmpline.replace('X_gSw_X' ,str(gSw))
                    tmpline = tmpline.replace('X_gPw_X' ,str(gPw))
                    tmpline = tmpline.replace('X_gSb_X' ,str(gSb))
                    tmpline = tmpline.replace('X_gPb_X' ,str(gPb))
                    tmpline = tmpline.replace('X_gDMA_X',str(gdmA))
                    tmpline = tmpline.replace('X_sintheta_X',str(gSinTheta))
                    tmpline = tmpline.replace('X_gH_X',str(gH))
                    tmpline = tmpline.replace('MED'     ,str(med))
                    tmpline = tmpline.replace('XMASS'   ,str(dm))
                    tmpline = tmpline.replace('PROC'    ,str(proc))
                    tmpline = tmpline.replace('RAND'    ,str(rand))
                    fout.write(tmpline)
         os.system('mv %s/%s_tmp %s/%s'%(directory,f,directory,f))
 
def fileExists(user,filename):
   sc=None
   #print '%s ls eos/cms/store/user/%s/gridpack/%s | wc -l' %(eos,user,filename)
   #exists = commands.getoutput('%s ls eos/cms/store/user/%s/gridpack/%s | wc -l' %(eos,user,filename)  )
   exists = commands.getoutput('ls /eos/user/c/cmantill/gridpack/%s | wc -l' %(filename)  )
   if len(exists.splitlines()) > 1: 
      exists = exists.splitlines()[1]
   else:
      exists = exists.splitlines()[0]
   #print exists
   return int(exists) == 1

def loadRestrict(iFile):
    #print iFile
    inputfile =  open(iFile)
    pairs=[]
    for line in inputfile:
        if line.find("#") > -1:
            continue
        tmpline=line.replace("\n","").replace(" ","").replace("\t","")
        lX = tmpline.split(":")[0]
        lY = tmpline.split(":")[1].split(",")
        for pY in lY:
            pairs.append([int(pY),int(lX)])
    return pairs

def checkRestrict(iRestrict,iMMED,iMDM):
    for pair in iRestrict:
        if iMMED == pair[0] and iMDM == pair[1]:
            return True
    return False

aparser = argparse.ArgumentParser(description='Process benchmarks.')
aparser.add_argument('-carddir','--carddir'   ,action='store',dest='carddir',default='Cards/Axial_MonoTop_NLO_Mphi_Mchi_gSM-0p25_gDM-1p0_13TeV-madgraph'   ,help='carddir')
aparser.add_argument('-q'      ,'--queue'      ,action='store',dest='queue'  ,default='2nw'                   ,help='queue')
aparser.add_argument('-dm'      ,'--dmrange'   ,dest='dmrange' ,nargs='+',type=int,default=[1,5,10,50,75,100,150,200,300,400,350,450,500,600,700,1000,3000,4000],help='mass range')
aparser.add_argument('-med'     ,'--medrange'  ,dest='medrange',nargs='+',type=int,default=[10,20,50,100,125,150,200,300,350,400,500,750,1000,1250,1500,1750,2000,2250,2500,3000,3500,4000,4500,5000,6000,7000,8000,10000],help='mediator range')
#aparser.add_argument('-med'     ,'--medrange'  ,dest='medrange',nargs='+',type=int,default=[4000,4500,5000,5500,6000,7000,8000,10000],help='mediator range')
aparser.add_argument('-proc'    ,'--proc'      ,dest='procrange',nargs='+',type=int,     default=[805],help='proc')
aparser.add_argument('-gq'      ,'--gq'        ,dest='gq',nargs='+',type=float,      default=[1.0],help='gq')
aparser.add_argument('-gdm'     ,'--gdm'       ,dest='gdm',nargs='+',type=float,     default=[1.0],help='gdm')
aparser.add_argument('-resubmit','--resubmit'  ,type=bool      ,dest='resubmit',default=False,help='resubmit')
aparser.add_argument('-install' ,'--install'   ,type=bool      ,dest='install' ,default=True ,help='install MG')
aparser.add_argument('-runcms'  ,'--runcms'    ,action='store' ,dest='runcms'  ,default='runcmsgrid_NLO.sh',help='runcms')
aparser.add_argument('-release' ,'--release'    ,action='store' ,dest='release'  ,default='2_6_0',help='MG version')

args1 = aparser.parse_args()
MGrelease=args1.release

#print args1.carddir,args1.queue,args1.dmrange,args1.medrange,args1.install

user=pwd.getpwuid( os.getuid() ).pw_name
basedir=os.getcwd()
os.system('rm %s/%s/*~' % (basedir,args1.carddir))

##Get the base files
parameterdir   = [ f for f in listdir(basedir+'/'+args1.carddir) if not isfile(join(basedir+'/'+args1.carddir,f)) ]
parameterfiles = [ f for f in listdir(basedir+'/'+args1.carddir) if     isfile(join(basedir+'/'+args1.carddir,f)) ]
#print parameterfiles,' -',basedir+'/'+args1.carddir,parameterdir,parameterfiles

mgcf = [f for f in parameterfiles if f.find('madconfig') > -1]
proc = [f for f in parameterfiles if f.find('proc')      > -1]
cust = [f for f in parameterfiles if f.find('custom')    > -1]
spin = [f for f in parameterfiles if f.find('madspin')   > -1]
rwgt = [f for f in parameterfiles if f.find('reweight')  > -1]
rtct = [f for f in parameterfiles if f.find('mass')      > -1]

procnamebase = commands.getoutput('cat %s | grep output | awk \'{print $2}\' ' % (basedir+'/'+args1.carddir+'/'+proc[0]))

##Start with the basics download Madgraph and add the options we care  :
if not args1.resubmit and args1.install:
    #os.system('rm -rf /tmp/%s/CMSSW_7_1_25_patch5' % user)
    #os.system('rm -rf /tmp/%s/CMSSW_7_1_20' % user)
    #os.system('rm -rf /tmp/%s/CMSSW_9_0_0_pre2' % user)
    os.system('rm -rf /tmp/%s/CMSSW_9_3_0_pre1' % user)
    os.system('rm -rf /tmp/%s/MG5_aMC_v%s'  % (user,MGrelease))
    os.system('cp  patches/install.sh .')
    os.system('./install.sh %s' % args1.release)
    os.system(('mv MG5_aMC_v'+MGrelease+' %s_MG5_aMC_v'+MGrelease) % procnamebase)

os.chdir (('%s_MG5_aMC_v'+MGrelease) % procnamebase)

#print "MG config :",mgcf[0],"ProcName : ",procnamebase
if not args1.resubmit and args1.install:
    os.system("cp "+basedir+"/"+args1.carddir+"/%s ." % mgcf[0])
    #os.system("cp /afs/cern.ch/work/b/bmaier/public/xMadGraph243/lhe_parser.py ./madgraph/various/")
    #os.system("cp /afs/cern.ch/user/p/pharris/pharris/public/amcatnlo_run_interface.py ./madgraph/interface/amcatnlo_run_interface.py")
    os.system("./bin/mg5_aMC %s" % mgcf[0])

##Now build the directories iterating over options
random.seed(1)
for f in parameterdir:
    if f.find('model') == -1:
        continue
    os.system('echo cp -r %s/%s/%s models/%s' % (basedir,args1.carddir,f,f))
    os.system('cp -r %s/%s/%s models/%s' % (basedir,args1.carddir,f,f))
    os.chdir('models/%s' % (f))
    os.system('python write_param_card.py')
    os.system('cp param_card.dat restrict_test.dat')
    os.chdir(('%s/%s_MG5_aMC_v'+MGrelease) % (basedir,procnamebase))

restrict = loadRestrict(basedir+"/"+args1.carddir+"/"+rtct[0])

#Loop
for med    in args1.medrange:
    for dm in args1.dmrange:
        if not checkRestrict(restrict,med,dm):
            continue
        tmpMed = med
        tmpDM  = dm 
        if med == 2*dm:
            tmpDM = dm-10
        for pProc in args1.procrange:
            rand=random.randrange(1000,9999,1)
            procname=procnamebase.replace("PROC",str(pProc)).replace("MED",str(tmpMed)).replace("XMASS",str(tmpDM))
            if not args1.resubmit:
                for f in parameterdir:
                    os.system('cp -r %s/%s/%s models/%s_%s_%s_%s' % (basedir,args1.carddir,f,f,tmpMed,tmpDM,pProc))
                    os.system('echo cp -r %s/%s/%s models/%s_%s_%s' % (basedir,args1.carddir,f,f,tmpMed,tmpDM))
                    print "!!!!!",args1.gdm[0],args1.gq[0]
                    replace(procnamebase,tmpMed,tmpDM,args1.gdm[0],args1.gq[0],pProc,rand,'models/%s_%s_%s_%s' % (f,tmpMed,tmpDM,pProc))
                    os.chdir('models/%s_%s_%s_%s' % (f,tmpMed,tmpDM,pProc))
                    os.system('python write_param_card.py')
                    os.system('cp param_card.dat restrict_test.dat')
                    os.chdir(('%s/%s_MG5_aMC_v'+MGrelease) % (basedir,procnamebase))
                    os.system('mkdir MG_%s' % (procname))
                
                for f in parameterfiles:
                    with open('MG_%s/%s' % (procname,f), "wt") as fout: 
                        with open(basedir+'/'+args1.carddir+'/'+f        ,"rt") as fin: 
                            for line in fin:
                                tmpline =    line.replace('MED'  ,str(tmpMed))
                                tmpline = tmpline.replace('XMASS',str(tmpDM))
                                tmpline = tmpline.replace('PROC' ,str(pProc))
                                tmpline = tmpline.replace('RAND' ,str(random.randrange(1000,9999,1)))
                                fout.write(tmpline)
            
                job_file = open(('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh') % (basedir,procnamebase,procname), "wt")
                job_file.write('#!/bin/bash\n')
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/  .     \n') % (basedir,procnamebase,procname))
                job_file.write('export SCRAM_ARCH=slc6_amd64_gcc530 \n')
                #job_file.write('export SCRAM_ARCH=slc6_amd64_gcc481 \n')
                #job_file.write('cd /afs/cern.ch/user/p/pharris/pharris/public/bacon/prod/CMSSW_7_1_20/src \n')
                #job_file.write('scramv1 project CMSSW CMSSW_7_1_25_patch5 \n')
                #job_file.write('cd CMSSW_7_1_25_patch5/src \n')
                #job_file.write('scramv1 project CMSSW CMSSW_7_1_20 \n')
                #job_file.write('cd CMSSW_7_1_20/src \n')
                job_file.write('scramv1 project CMSSW CMSSW_9_3_0_pre1 \n')
                job_file.write('cd CMSSW_9_3_0_pre1/src \n')
                job_file.write('eval `scramv1 runtime -sh` \n')
                job_file.write('LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml \n')
                job_file.write('if [ -e $LHAPDF6TOOLFILE ]; then \n')
                job_file.write('  LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\\"LHAPDF6_BASE\\"" | cut -d \\" -f 4`/bin/lhapdf-config \n')
                job_file.write('else \n')
                job_file.write('  LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"` \n')
                job_file.write('fi \n')
                job_file.write('export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir` \n')
                job_file.write('LHAPDFINCLUDES=`$LHAPDFCONFIG --incdir` \n')
                job_file.write('LHAPDFLIBS=`$LHAPDFCONFIG --libdir` \n')
                job_file.write('cd - \n')
                job_file.write('cd MG_%s/                       \n' % (procname) )
                job_file.write(('%s/%s_MG5_aMC_v'+MGrelease+'/bin/mg5_aMC  %s  \n') % (basedir,procnamebase,proc[0]) )
                if len(cust) > 0:
                    job_file.write('cp %s %s/                   \n' % (cust[0],procname))
                if args1.runcms.find("NLO") > -1:
                    job_file.write('mv %s process  \n' % (procname))
                    job_file.write('cd process     \n' )
                else:
                    job_file.write('cd  %s                      \n' % (procname) )
                pReweight=False
                for f in parameterfiles:
                    if f.find('dat') > -1:
                        job_file.write('mv ../%s Cards \n' % f)
                    if f.find('.f')  > -1:
                        job_file.write('mv ../%s SubProcesses \n' % f)
                    if f.find('reweight') > -1:
                        job_file.write('cp Cards/%s . \n' % f)
                        pReweight=True
                if args1.runcms.find("NLO") > -1:
                    job_file.write('echo "shower=OFF" > makegrid.dat  \n')
                    #if pReweight:
                    #    job_file.write('echo "reweight=OFF" >> makegrid.dat  \n')
                job_file.write('echo "done"              >>  makegrid.dat  \n')
                if len(cust) > 0:
                    job_file.write('cat %s >> makegrid.dat \n' % (cust[0]))
                if args1.runcms.find("NLO") == -1:
                    job_file.write('echo "set gridpack true" >> makegrid.dat \n')
                job_file.write('echo "" >> makegrid.dat \n')
                job_file.write('echo "done">> makegrid.dat  \n')
                if args1.runcms.find("NLO") > -1:
                    job_file.write('cat makegrid.dat | ./bin/generate_events -n pilotrun \n')
                else:
                    job_file.write('cat makegrid.dat | ./bin/generate_events pilotrun \n')
                job_file.write('cd ..      \n')
                if args1.runcms.find("NLO") > -1:
                    job_file.write('echo "mg5_path = ../mgbasedir"  >> process/Cards/amcatnlo_configuration.txt \n')
                    job_file.write('echo "cluster_temp_path = None" >> process/Cards/amcatnlo_configuration.txt \n')  
                    job_file.write('cd process  \n')
                else:
                    job_file.write('mkdir process \n')
                    job_file.write('mv %s/pilotrun_gridpack.tar.gz                 process  \n' % (procname))
                    job_file.write('mv %s/Events/pilotrun/unweighted_events.lhe.gz process  \n' % (procname))
                    job_file.write('cd process  \n')
                    job_file.write('tar xzf pilotrun_gridpack.tar.gz  \n')
                    job_file.write('rm pilotrun_gridpack.tar.gz  \n')
                    job_file.write('echo "mg5_path = ../../mgbasedir" >> ./madevent/Cards/me5_configuration.txt \n')
                    job_file.write('echo "run_mode = 0" >> ./madevent/Cards/me5_configuration.txt \n')  
                    if len(spin) > 0: 
                        job_file.write('echo "import unweighted_events.lhe.gz"          >  madspinrun.dat \n')
                        job_file.write('cat %s                                          >> madspinrun.dat \n' % spin[0])
                        job_file.write('cat madspinrun.dat | MadSpin/madspin \n')
                        job_file.write('rm madspinrun.dat \n')
                        job_file.write('rm unweighted_events.lhe.gz \n')
                        job_file.write('rm -rf tmp* \n')
                        job_file.write('cp %s/%s/%s process/madspin_card.dat \n' % (basedir,args1.carddir,spin[0]))
                    if pReweight > 0: 
                        job_file.write('mkdir -p madevent/Events/pilotrun \n')
                        job_file.write('cp unweighted_events.lhe.gz madevent/Events/pilotrun \n')
                        #if args1.runcms.find("NLO") > -1:
                        #    job_file.write('echo "f2py_compiler=" `which gfortran` >> ./madevent/Cards/me5_configuration.txt \n')
                        job_file.write('export LIBRARY_PATH=$LD_LIBRARY_PATH \n')
                        job_file.write('cd madevent;./bin/madevent reweight pilotrun;cd .. \n')
                                   
                job_file.write('cd .. \n')
                job_file.write('cp    %s/cleangridmore.sh .      \n'  % (basedir))
                job_file.write('cp    %s/%s               runcmsgrid.sh      \n'  % (basedir,args1.runcms))
                job_file.write('./cleangridmore.sh               \n')
                job_file.write('mkdir  mgbasedir     \n')
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/MadSpin  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/SysCalc  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/input    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/HELAS    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/HEPTools mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/README   mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/Template mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/VERSION  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/aloha    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/bin      mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/madconfig  mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/madgraph   mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/mg5decay   mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/models     mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/tests      mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/vendor     mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/PLUGINS    mgbasedir \n') % (basedir,procnamebase))
                job_file.write(('cp -r %s/%s_MG5_aMC_v'+MGrelease+'/PLUGIN     mgbasedir \n') % (basedir,procnamebase))
                output  ='%s_tarball.tar.xz'                    % (procname)
                job_file.write('XZ_OPT="--lzma2=preset=9,dict=512MiB" tar -cJpsf '+output+' mgbasedir process runcmsgrid.sh \n')
                #job_file.write(('cp -r %s  %s/%s_MG5_aMC_v'+MGrelease+'/         \n') % (output,basedir,procnamebase))
                job_file.write(('rm  /eos/user/c/cmantill/gridpack/%s  \n') % (output))
                job_file.write(('cp %s  /eos/user/c/cmantill/gridpack/%s  \n') % (output,output))
                #job_file.write(('%s rm  eos/cms/store/user/%s/gridpack/%s  \n') % (eos,user,output))
                #job_file.write(('cp %s   /eos/cms/store/user/%s/gridpack/%s  \n') % (output,user,output))
                job_file.close()
                os.chmod(('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh')             % (basedir,procnamebase,procname),0777)
            if os.path.isfile(('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh')        % (basedir,procnamebase,procname)):
                #print "Looking",('%s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh')      % (basedir,procnamebase,procname)
                #print "Loooking More",('%s/%s_MG5_aMC_v'+MGrelease+'/%s_tarball.tar.xz') % (basedir,procnamebase,procname)
                #if not os.path.isfile(('%s/%s_MG5_aMC_v'+MGrelease+'/%s_tarball.tar.xz') % (basedir,procnamebase,procname)):
                output     ='%s_tarball.tar.xz'                    % (procname)
                if not fileExists(user,output):
                    os.system(('echo bsub -q  %s -R "rusage[mem=12000]" %s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh') % (args1.queue,basedir,procnamebase,procname))
                    os.system(('bsub -q  %s -R "rusage[mem=12000]" %s/%s_MG5_aMC_v'+MGrelease+'/MG_%s/integrate.sh') % (args1.queue,basedir,procnamebase,procname))


           
#while not completed(args1.name,args1.medrange,args1.dmrange,basedir,args1.carddir):
#    print "Waiting ",datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
#    time.sleep(60)
