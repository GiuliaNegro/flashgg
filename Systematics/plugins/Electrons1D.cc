#include "flashgg/Systematics/interface/ElectronBase.h"

namespace flashgg {

    typedef ElectronBase<int> Electrons1D;

}

DEFINE_EDM_PLUGIN( FlashggSystematicElectronMethodsFactory,
                   flashgg::Electrons1D,
                   "FlashggElectrons1D" );

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4