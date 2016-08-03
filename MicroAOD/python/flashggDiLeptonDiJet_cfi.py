import FWCore.ParameterSet.Config as cms

flashggDiLeptonDiJet = cms.EDProducer('FlashggDiLeptonDiJetProducer',   #devo usare flashgg tags
									ElectronTag=cms.InputTag('flashggElectrons'),  #'slimmedElectrons'), 
									MuonTag=cms.InputTag('flashggMuons'),          #'slimmedMuons'),
									JetTag=cms.InputTag('slimmedJets'),   
									TrackTag=cms.InputTag('packedPFCandidates'),
									VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'), 
									##Parameters  
                                    minElectronPt=cms.double(5.),
                                    maxElectronEta=cms.double(2.4),
									minMuonPt=cms.double(5.),
									maxMuonEta=cms.double(2.4),
                                    minJetPt=cms.double(7.),
                                    maxJetEta=cms.double(2.4)
                                  )
