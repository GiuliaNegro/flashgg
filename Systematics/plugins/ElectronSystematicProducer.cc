#include "flashgg/DataFormats/interface/Electron.h"
#include "flashgg/Systematics/interface/BaseSystMethod.h"
#include "flashgg/Systematics/interface/ObjectSystematicProducer.h"

namespace flashgg {

    typedef ObjectSystematicProducer<Electron, int, std::vector> ElectronSystematicProducer;

}

typedef flashgg::ElectronSystematicProducer FlashggElectronSystematicProducer;
DEFINE_FWK_MODULE( FlashggElectronSystematicProducer );

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4