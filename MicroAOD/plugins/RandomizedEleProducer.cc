#ifndef FLASHgg_RandomizedEleProducer_h
#define FLASHgg_RandomizedEleProducer_h

/* This is a *temporary* producer supposed to be replaced by the
 * RandomizedElectronProducer run at MicroAOD production time. This producer is
 * meant to be run on-the-fly on MicroAOD produced already with no random
 * information attached to the Electron's. It is close to a mere copy-n-paste of
 * RandomizedObjectProducer.h
 */

#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"
#include "CLHEP/Random/RandGauss.h"
#include "flashgg/DataFormats/interface/Electron.h"


using namespace edm;
using namespace std;


namespace flashgg {

	class RandomizedEleProducer : public EDProducer
	{
	public:
		RandomizedEleProducer( const ParameterSet & );
		void produce( Event &, const EventSetup & ) override;

	private:
		EDGetTokenT<View<flashgg::Electron> > token_;
		vector<string> labels_;
		//string pdf_; // only gaussians with mean 0 and width 1 for the time being
	};

	RandomizedEleProducer::RandomizedEleProducer( const ParameterSet &ps ) :
		token_(consumes<View<flashgg::Electron> >(ps.getParameter<InputTag>("src"))),
		labels_(ps.getParameter<vector<string> >("labels"))
		//prefix_(ps.getParameter<string>("pdf")
	{
		produces<vector<flashgg::Electron> >();
	}

	void RandomizedEleProducer::produce( Event &evt, const EventSetup & )
	{
		Service<RandomNumberGenerator> rng;
		if( ! rng.isAvailable() ) {
			throw cms::Exception( "Configuration" ) << "ObjectSystematicProducer requires the RandomNumberGeneratorService  - please add to configuration";
		}

		Handle<View<flashgg::Electron> > objects;
		evt.getByToken( token_, objects );

		CLHEP::HepRandomEngine & engine = rng->getEngine( evt.streamID() );
		auto_ptr<vector<flashgg::Electron> > out_obj( new vector<flashgg::Electron>() );
		CLHEP::RandGauss::shoot(&engine, 0., 1.);

		for (const auto & obj : *objects) {
			auto o = obj;
			for (auto l : labels_) {

				o.addUserFloat(l, CLHEP::RandGauss::shoot(&engine, 0., 1.));

				out_obj->push_back(o);
			}
		}
		evt.put(out_obj);
	}
}

typedef flashgg::RandomizedEleProducer FlashggRandomizedEleProducer;
DEFINE_FWK_MODULE( FlashggRandomizedEleProducer );

#endif

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
