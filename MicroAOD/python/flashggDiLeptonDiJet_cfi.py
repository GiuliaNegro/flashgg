import FWCore.ParameterSet.Config as cms

flashggDiLeptonDiJet = cms.EDProducer('FlashggDiLeptonDiJetProducer',     
									ElectronTag=cms.InputTag('flashggElectrons'),  #'slimmedElectrons'), 
									MuonTag=cms.InputTag('flashggMuons'),          #'slimmedMuons'),
									JetTag=cms.InputTag('flashggFinalJets'),       #'slimmedJets'),   
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


# flashggDiLeptonDiJet = cms.EDProducer('FlashggDiLeptonDiJetProducer',   #for Hgg microAOD
# 									ElectronTag=cms.InputTag('flashggSelectedElectrons'),  
# 									MuonTag=cms.InputTag('flashggSelectedMuons'),        
# 									JetTag=cms.InputTag('flashggFinalJets'), #'flashggJets'),
# 									TrackTag=cms.InputTag('packedPFCandidates'),
# 									VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'), 
# 									##Parameters  
#                                     minElectronPt=cms.double(5.),
#                                     maxElectronEta=cms.double(2.4),
# 									minMuonPt=cms.double(5.),
# 									maxMuonEta=cms.double(2.4),
#                                     minJetPt=cms.double(7.),
#                                     maxJetEta=cms.double(2.4)
#                                   )