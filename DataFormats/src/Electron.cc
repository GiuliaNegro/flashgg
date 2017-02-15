#include "flashgg/DataFormats/interface/Electron.h"

using namespace flashgg;

Electron::Electron() : pat::Electron()
{}

Electron::~Electron()
{}

Electron::Electron( const pat::Electron &anelectron ) : pat::Electron( anelectron )
{}

bool Electron::hasEnergyAtStep( std::string key ) const
{
    return hasUserFloat( key );
}

void Electron::setEnergyAtStep( std::string key, float val )
{
    addUserFloat( key, val );
}

void Electron::updateEnergy( std::string key, float val )
{

    // Current energy saved when updated, unless we're still at the initial step
    if( !hasEnergyAtStep( "initial" ) ) {
        setEnergyAtStep( "initial", energy() );
    }

    // Update new energy
    setEnergyAtStep( key, val );

    // Update 4-vector
    setP4( ( val / energy() )*p4() );
}


// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

