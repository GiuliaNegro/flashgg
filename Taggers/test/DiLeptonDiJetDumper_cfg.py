#!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("Analysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring(
        "file:myMicroAODOutputFile_DiLeptonDiJet.root"  
        #"file:root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/cmshgg/ferriff/flashgg/RunIISpring16DR80X-2_2_0-25ns_ICHEP16_MiniAODv2/2_2_0/DoubleEG/RunIISpring16DR80X-2_2_0-25ns_ICHEP16_MiniAODv2-2_2_0-v0-Run2016B-PromptReco-v2/160707_143218/0000/myMicroAODOutputFile_938.root" 
        )
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("test.root")
)

#process.load("flashgg.MicroAOD.flashggDiLeptonDiJet_cfi")  ##  import DiLeptonDiJet (producer)
process.load("flashgg.Taggers.DiLeptonDiJetDumper_cfi") ##  import DiLeptonDiJetDumper 
import flashgg.Taggers.dumperConfigTools as cfgTools

#process.DiLeptonDiJetDumper.src = "flashggDiLeptonDiJet"  
process.DiLeptonDiJetDumper.dumpTrees = True
process.DiLeptonDiJetDumper.dumpWorkspace = False
process.DiLeptonDiJetDumper.quietRooFit = True


# split tree, histogram and datasets by process
# process.DiLeptonDiJetDumper.nameTemplate ="$PROCESS_$SQRTS_$LABEL_$SUBCAT"
process.DiLeptonDiJetDumper.nameTemplate ="nuMSM_$SQRTS_$LABEL_$SUBCAT"


## do not split by process
## process.DiLeptonDiJetDumper.nameTemplate = "minitree_$SQRTS_$LABEL_$SUBCAT"

## define categories and associated objects to dump
cfgTools.addCategory(process.DiLeptonDiJetDumper,
                     "Reject",
                     "0",
                     # "abs(leadingPhoton.superCluster.eta)>=1.4442&&abs(leadingPhoton.superCluster.eta)<=1.566||abs(leadingPhoton.superCluster.eta)>=2.5"
                     # "||abs(subLeadingPhoton.superCluster.eta)>=1.4442 && abs(subLeadingPhoton.superCluster.eta)<=1.566||abs(subLeadingPhoton.superCluster.eta)>=2.5",
                      -1 ## if nSubcat is -1 do not store anythings
                     )

# interestng categories 
cfgTools.addCategories(process.DiLeptonDiJetDumper,
                       ## categories definition
                       ## cuts are applied in cascade. Events getting to these categories have already failed the "Reject" selection
                       [("all","1",0)
                       # [("EBHighR9","max(abs(leadingPhoton.superCluster.eta),abs(leadingPhoton.superCluster.eta))<1.4442"
                       #   "&& min(leadingPhoton.r9,subLeadingPhoton.r9)>0.94",0), ## EB high R9
                       #  ("EBLowR9","max(abs(leadingPhoton.superCluster.eta),abs(leadingPhoton.superCluster.eta))<1.4442",0), ## remaining EB is low R9
                       #  ("EEHighR9","min(leadingPhoton.r9,subLeadingPhoton.r9)>0.94",0), ## then EE high R9
                       #  ("EELowR9","1",0), ## evereything elese is EE low R9
                        ],
                       ## variables to be dumped in trees/datasets. Same variables for all categories
                       ## if different variables wanted for different categories, can add categorie one by one with cfgTools.addCategory
                       variables=[#"CMS_hgg_mass[320,100,180]:=mass",   
                                  "leadElePt                   :=leadingEle.pt",
                                  "subLeadElePt                :=subLeadingEle.pt",
                                  "leadJetPt                   :=leadingJet.pt",
                                  "subLeadJetPt                :=subLeadingJet.pt"
                                  ],
                       ## histograms to be plotted. 
                       ## the variables need to be defined first
                       histograms=[#"CMS_hgg_mass>>mass(320,100,180)",
                                   # "subleadPt:leadPt>>ptSubVsLead(180,20,200:180,20,200)",
                                   "leadElePt>>leadElePt(100, 0, 100)",
                                   "subLeadElePt>>subLeadElePt(100, 0, 100)",
                                   "leadJetPt>>leadJetPt(100, 0, 100)",
                                   "subLeadJetPt>>subLeadJetPt(100, 0, 100)",
                                   ]
                       )


process.p1 = cms.Path(
    #process.flashggDiLeptonDiJet*process.DiLeptonDiJetDumper  #add producer if microAOD producted without DiLeptonDiJet
    process.DiLeptonDiJetDumper   #if microAOD producted with DiLeptonDiJet
    )


from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",100)
customize(process)

