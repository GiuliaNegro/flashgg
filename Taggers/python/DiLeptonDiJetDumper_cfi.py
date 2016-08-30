import FWCore.ParameterSet.Config as cms

from flashgg.Taggers.DiLeptonDiJetDumpConfig_cff import DiLeptonDiJetDumpConfig

DiLeptonDiJetDumper = cms.EDAnalyzer('CutBasedDiLeptonDiJetDumper',
                                **DiLeptonDiJetDumpConfig.parameters_()
                                )

