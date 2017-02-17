#ifndef FLASHgg_ElectronBase_h
#define FLASHgg_ElectronBase_h

#include "flashgg/Systematics/interface/BaseSystMethod.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/PtrVector.h"
#include "flashgg/DataFormats/interface/Electron.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"
#include <memory>

namespace flashgg {


    template <class param_var>
    class ElectronBase : public BaseSystMethod<Electron, param_var>
    {

    public:
        ElectronBase( const edm::ParameterSet &conf, edm::ConsumesCollector && iC, const GlobalVariablesComputer * gv );

        void applyCorrection( Electron &y, param_var syst_shift ) override;
        float makeWeight( const Electron &y, param_var syst_shift ) override;
        std::string shiftLabel( param_var ) const override;
        void eventInitialize( const edm::Event &iEvent, const edm::EventSetup & iSetup ) override;

        void setRandomEngine( CLHEP::HepRandomEngine &eng ) override
        {
            //            std::cout << " ElectronBase::setRandomEngine " << std::endl;
            BaseSystMethod<Electron, param_var>::setRandomEngine( eng );
            electron_corr_->setRandomEngine( eng );
        }
        
    protected:
        bool debug_;

    private:
        std::unique_ptr<BaseSystMethod<flashgg::Electron, param_var> > electron_corr_;
    };

    template<class param_var>
    ElectronBase<param_var>::ElectronBase( const edm::ParameterSet &conf, edm::ConsumesCollector && iC, const GlobalVariablesComputer * gv ) :
        BaseSystMethod<Electron, param_var>::BaseSystMethod( conf, std::forward<edm::ConsumesCollector>(iC) ),
        debug_( conf.getUntrackedParameter<bool>( "Debug", false ) )
    {
        std::string electronMethodName = conf.getParameter<std::string>( "ElectronMethodName" );
        electron_corr_.reset( FlashggSystematicMethodsFactory<flashgg::Electron, param_var>::get()->create( electronMethodName, conf, std::forward<edm::ConsumesCollector>(iC), gv ) );
        this->setMakesWeight( electron_corr_->makesWeight() );
    }

    template<class param_var>
    std::string ElectronBase<param_var>::shiftLabel( param_var syst_value ) const
    {
        return electron_corr_->shiftLabel( syst_value );
    }

    template<typename param_var>
    float ElectronBase<param_var>::makeWeight( const Electron &y, param_var syst_shift )
    {
        if( debug_ ) {
            std::cout << "START OF Electron::makeWeight M PT E ETA "
                    << y.mass() << " " << y.pt() << " " << y.energy() << " " << y.eta() << std::endl;
        }

        float weight = electron_corr_->makeWeight( y, syst_shift );

        if( debug_ ) {
            std::cout << "END OF Electron::makeWeight M PT E ETA "
                      << " weight=" << weight << std::endl;
        }
        return weight;
    }

    template<class param_var>
    void ElectronBase<param_var>::applyCorrection( Electron &y, param_var syst_shift )
    {
        if( debug_ ) {
            std::cout << "START OF Electron::applyCorrection M PT E ETA "
                    << y.mass() << " " << y.pt() << " " << y.energy() << " " << y.eta() << std::endl;
        }
        
        electron_corr_->applyCorrection( y, syst_shift );

        // y.computeP4AndOrder();

        if( debug_ ) {
            std::cout << "END OF Electron::applyCorrection M PT E ETA "
                    << y.mass() << " " << y.pt() << " " << y.energy() << " " << y.eta() << std::endl;
        }
    }

    template<class param_var>
    void ElectronBase<param_var>::eventInitialize( const edm::Event &ev, const edm::EventSetup & es )
    {
        if( debug_ ) {
            std::cout << "calling event initialize for electron " << std::endl;
        }
        electron_corr_->eventInitialize( ev, es );
    }
}

#endif

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4