#ifndef flashgg_MicroAOD__FLASHggObjectSelector_h
#define flashgg_MicroAOD__FLASHggObjectSelector_h

#include "flashgg/DataFormats/interface/Electron.h"
#include "flashgg/DataFormats/interface/Muon.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "CommonTools/UtilAlgos/interface/StringCutObjectSelector.h"
#include "CommonTools/UtilAlgos/interface/SingleObjectSelector.h"

#include <vector>


//typedef reco::Track Track_t;
typedef pat::PackedCandidate Track_t;


namespace flashgg {

    typedef SingleObjectSelector <
    std::vector<Electron>,
        StringCutObjectSelector<Electron>
        > FLASHggElectronSelector;

    typedef SingleObjectSelector <
    std::vector<Muon>,
        StringCutObjectSelector<Muon>
        > FLASHggMuonSelector;

    typedef SingleObjectSelector <
    std::vector<Photon>,
        StringCutObjectSelector<Photon>
        > FLASHggPhotonSelector;

    typedef SingleObjectSelector <
    std::vector<Jet>,
        StringCutObjectSelector<Jet>
        > FLASHggJetSelector;

    typedef SingleObjectSelector <        //adding track selector
    std::vector<Track_t>,                 
        StringCutObjectSelector<Track_t>  
        > FLASHggTrackSelector;

}

#endif

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
