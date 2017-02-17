#include "flashgg/Systematics/interface/ElectronBase.h"

namespace flashgg {

    typedef ElectronBase<std::pair<int, int> > Electrons2D;

}

DEFINE_EDM_PLUGIN( FlashggSystematicElectronMethodsFactory2D,
                   flashgg::Electrons2D,
                   "FlashggElectrons2D" );

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4