#include "flashgg/DataFormats/interface/DiMuDiJetTag.h"
#include <algorithm>

using namespace flashgg;

DiMuDiJetTag::DiMuDiJetTag() : DiLeptonDiJetTagBase::DiLeptonDiJetTagBase()
{}

DiMuDiJetTag::~DiMuDiJetTag()
{}

// N.B. Other attributes are set using methods in header file
DiMuDiJetTag::DiMuDiJetTag( edm::Ptr<DiLeptonDiJetCandidate> diMuDiJet ) : DiLeptonDiJetTagBase::DiLeptonDiJetTagBase( diMuDiJet ) {}  


// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4