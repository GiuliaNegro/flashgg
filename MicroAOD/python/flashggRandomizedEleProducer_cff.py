import FWCore.ParameterSet.Config as cms

# add the following lines to the module used to configure the RandomNumberGeneratorService
# process.RandomNumberGeneratorService.flashggRandomizedEle = cms.PSet(
#           initialSeed = cms.untracked.uint32(16253245)
#         # engineName = cms.untracked.string('TRandom3') # optional, default to HepJamesRandom if absent
#         )

flashggRandomizedEle = cms.EDProducer("FlashggRandomizedEleProducer",
                                    src = cms.InputTag("flashggSelectedElectrons"),  
                                    # labels of various gaussian random numbers with mean=0, sigma=1
                                    # to be associated with the photon object
                                    labels = cms.vstring("smearE")
                                    )