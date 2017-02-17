import FWCore.ParameterSet.Config as cms

binInfo = cms.PSet(
	variables = cms.vstring("eta","pt"),
	bins = cms.VPSet(
		# CutBasedId - LooseWP scale factors (80X)
	# https://twiki.cern.ch/twiki/bin/view/CMS/EgammaIDRecipesRun2#Electron_efficiencies_and_scale : 80X series - Moriond 2017 recommandation; combined : Reconstruction efficiency. Scale factors for 80X and Electron cut-based 80XID WPs. Scale factors for 80X : Loose cut-based ID WP scale factor | for a total of : 36.3 /fb.
	#Note : SFs valid only from 10GeV, eta 2.5, bins extended to extremes to prevent any crashes 

	cms.PSet( lowBounds = cms.vdouble( -6.0000, 0.0000 ) , upBounds = cms.vdouble( -2.4500, 20.0000 ) , values = cms.vdouble( 1.1377 ) , uncertainties = cms.vdouble( 0.0258 ) ),
	cms.PSet( lowBounds = cms.vdouble( -6.0000, 20.0000 ) , upBounds = cms.vdouble( -2.4500, 35.0000 ) , values = cms.vdouble( 1.2545 ) , uncertainties = cms.vdouble( 0.0195 ) ),
	cms.PSet( lowBounds = cms.vdouble( -6.0000, 35.0000 ) , upBounds = cms.vdouble( -2.4500, 50.0000 ) , values = cms.vdouble( 1.2992 ) , uncertainties = cms.vdouble( 0.0199 ) ),
	cms.PSet( lowBounds = cms.vdouble( -6.0000, 50.0000 ) , upBounds = cms.vdouble( -2.4500, 80.0000 ) , values = cms.vdouble( 1.3161 ) , uncertainties = cms.vdouble( 0.0200 ) ),
	cms.PSet( lowBounds = cms.vdouble( -6.0000, 80.0000 ) , upBounds = cms.vdouble( -2.4500, 90.0000 ) , values = cms.vdouble( 1.3161 ) , uncertainties = cms.vdouble( 0.0223 ) ),
	cms.PSet( lowBounds = cms.vdouble( -6.0000, 90.0000 ) , upBounds = cms.vdouble( -2.4500, 150.0000 ) , values = cms.vdouble( 1.3663 ) , uncertainties = cms.vdouble( 0.0429 ) ),
	cms.PSet( lowBounds = cms.vdouble( -6.0000, 150.0000 ) , upBounds = cms.vdouble( -2.4500, 9999999.0000 ) , values = cms.vdouble( 1.3663 ) , uncertainties = cms.vdouble( 0.0432 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -2.4500, 0.0000 ) , upBounds = cms.vdouble( -2.4000, 20.0000 ) , values = cms.vdouble( 0.9617 ) , uncertainties = cms.vdouble( 0.0203 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4500, 20.0000 ) , upBounds = cms.vdouble( -2.4000, 35.0000 ) , values = cms.vdouble( 1.0605 ) , uncertainties = cms.vdouble( 0.0129 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4500, 35.0000 ) , upBounds = cms.vdouble( -2.4000, 50.0000 ) , values = cms.vdouble( 1.0982 ) , uncertainties = cms.vdouble( 0.0130 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4500, 50.0000 ) , upBounds = cms.vdouble( -2.4000, 80.0000 ) , values = cms.vdouble( 1.1125 ) , uncertainties = cms.vdouble( 0.0130 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4500, 80.0000 ) , upBounds = cms.vdouble( -2.4000, 90.0000 ) , values = cms.vdouble( 1.1125 ) , uncertainties = cms.vdouble( 0.0164 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4500, 90.0000 ) , upBounds = cms.vdouble( -2.4000, 150.0000 ) , values = cms.vdouble( 1.1550 ) , uncertainties = cms.vdouble( 0.0349 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4500, 150.0000 ) , upBounds = cms.vdouble( -2.4000, 9999999.0000 ) , values = cms.vdouble( 1.1550 ) , uncertainties = cms.vdouble( 0.0352 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -2.4000, 0.0000 ) , upBounds = cms.vdouble( -2.3000, 20.0000 ) , values = cms.vdouble( 0.8847 ) , uncertainties = cms.vdouble( 0.0182 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4000, 20.0000 ) , upBounds = cms.vdouble( -2.3000, 35.0000 ) , values = cms.vdouble( 0.9756 ) , uncertainties = cms.vdouble( 0.0104 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4000, 35.0000 ) , upBounds = cms.vdouble( -2.3000, 50.0000 ) , values = cms.vdouble( 1.0103 ) , uncertainties = cms.vdouble( 0.0104 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4000, 50.0000 ) , upBounds = cms.vdouble( -2.3000, 80.0000 ) , values = cms.vdouble( 1.0235 ) , uncertainties = cms.vdouble( 0.0103 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4000, 80.0000 ) , upBounds = cms.vdouble( -2.3000, 90.0000 ) , values = cms.vdouble( 1.0235 ) , uncertainties = cms.vdouble( 0.0144 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4000, 90.0000 ) , upBounds = cms.vdouble( -2.3000, 150.0000 ) , values = cms.vdouble( 1.0625 ) , uncertainties = cms.vdouble( 0.0318 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.4000, 150.0000 ) , upBounds = cms.vdouble( -2.3000, 9999999.0000 ) , values = cms.vdouble( 1.0625 ) , uncertainties = cms.vdouble( 0.0320 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -2.3000, 0.0000 ) , upBounds = cms.vdouble( -2.2000, 20.0000 ) , values = cms.vdouble( 0.8753 ) , uncertainties = cms.vdouble( 0.0178 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.3000, 20.0000 ) , upBounds = cms.vdouble( -2.2000, 35.0000 ) , values = cms.vdouble( 0.9651 ) , uncertainties = cms.vdouble( 0.0096 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.3000, 35.0000 ) , upBounds = cms.vdouble( -2.2000, 50.0000 ) , values = cms.vdouble( 0.9995 ) , uncertainties = cms.vdouble( 0.0096 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.3000, 50.0000 ) , upBounds = cms.vdouble( -2.2000, 80.0000 ) , values = cms.vdouble( 1.0125 ) , uncertainties = cms.vdouble( 0.0095 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.3000, 80.0000 ) , upBounds = cms.vdouble( -2.2000, 90.0000 ) , values = cms.vdouble( 1.0125 ) , uncertainties = cms.vdouble( 0.0138 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.3000, 90.0000 ) , upBounds = cms.vdouble( -2.2000, 150.0000 ) , values = cms.vdouble( 1.0511 ) , uncertainties = cms.vdouble( 0.0312 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.3000, 150.0000 ) , upBounds = cms.vdouble( -2.2000, 9999999.0000 ) , values = cms.vdouble( 1.0511 ) , uncertainties = cms.vdouble( 0.0315 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -2.2000, 0.0000 ) , upBounds = cms.vdouble( -2.0000, 20.0000 ) , values = cms.vdouble( 0.8698 ) , uncertainties = cms.vdouble( 0.0170 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.2000, 20.0000 ) , upBounds = cms.vdouble( -2.0000, 35.0000 ) , values = cms.vdouble( 0.9591 ) , uncertainties = cms.vdouble( 0.0079 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.2000, 35.0000 ) , upBounds = cms.vdouble( -2.0000, 50.0000 ) , values = cms.vdouble( 0.9932 ) , uncertainties = cms.vdouble( 0.0077 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.2000, 50.0000 ) , upBounds = cms.vdouble( -2.0000, 80.0000 ) , values = cms.vdouble( 1.0061 ) , uncertainties = cms.vdouble( 0.0075 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.2000, 80.0000 ) , upBounds = cms.vdouble( -2.0000, 90.0000 ) , values = cms.vdouble( 1.0061 ) , uncertainties = cms.vdouble( 0.0125 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.2000, 90.0000 ) , upBounds = cms.vdouble( -2.0000, 150.0000 ) , values = cms.vdouble( 1.0445 ) , uncertainties = cms.vdouble( 0.0305 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.2000, 150.0000 ) , upBounds = cms.vdouble( -2.0000, 9999999.0000 ) , values = cms.vdouble( 1.0445 ) , uncertainties = cms.vdouble( 0.0307 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -2.0000, 0.0000 ) , upBounds = cms.vdouble( -1.8000, 20.0000 ) , values = cms.vdouble( 0.8705 ) , uncertainties = cms.vdouble( 0.0197 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.0000, 20.0000 ) , upBounds = cms.vdouble( -1.8000, 35.0000 ) , values = cms.vdouble( 0.9667 ) , uncertainties = cms.vdouble( 0.0128 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.0000, 35.0000 ) , upBounds = cms.vdouble( -1.8000, 50.0000 ) , values = cms.vdouble( 0.9904 ) , uncertainties = cms.vdouble( 0.0079 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.0000, 50.0000 ) , upBounds = cms.vdouble( -1.8000, 80.0000 ) , values = cms.vdouble( 0.9948 ) , uncertainties = cms.vdouble( 0.0073 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.0000, 80.0000 ) , upBounds = cms.vdouble( -1.8000, 90.0000 ) , values = cms.vdouble( 0.9948 ) , uncertainties = cms.vdouble( 0.0124 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.0000, 90.0000 ) , upBounds = cms.vdouble( -1.8000, 150.0000 ) , values = cms.vdouble( 1.0100 ) , uncertainties = cms.vdouble( 0.0153 ) ),
	cms.PSet( lowBounds = cms.vdouble( -2.0000, 150.0000 ) , upBounds = cms.vdouble( -1.8000, 9999999.0000 ) , values = cms.vdouble( 1.0100 ) , uncertainties = cms.vdouble( 0.0157 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -1.8000, 0.0000 ) , upBounds = cms.vdouble( -1.6300, 20.0000 ) , values = cms.vdouble( 0.8704 ) , uncertainties = cms.vdouble( 0.0194 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.8000, 20.0000 ) , upBounds = cms.vdouble( -1.6300, 35.0000 ) , values = cms.vdouble( 0.9667 ) , uncertainties = cms.vdouble( 0.0122 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.8000, 35.0000 ) , upBounds = cms.vdouble( -1.6300, 50.0000 ) , values = cms.vdouble( 0.9903 ) , uncertainties = cms.vdouble( 0.0069 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.8000, 50.0000 ) , upBounds = cms.vdouble( -1.6300, 80.0000 ) , values = cms.vdouble( 0.9948 ) , uncertainties = cms.vdouble( 0.0062 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.8000, 80.0000 ) , upBounds = cms.vdouble( -1.6300, 90.0000 ) , values = cms.vdouble( 0.9948 ) , uncertainties = cms.vdouble( 0.0117 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.8000, 90.0000 ) , upBounds = cms.vdouble( -1.6300, 150.0000 ) , values = cms.vdouble( 1.0100 ) , uncertainties = cms.vdouble( 0.0147 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.8000, 150.0000 ) , upBounds = cms.vdouble( -1.6300, 9999999.0000 ) , values = cms.vdouble( 1.0100 ) , uncertainties = cms.vdouble( 0.0152 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -1.6300, 0.0000 ) , upBounds = cms.vdouble( -1.5660, 20.0000 ) , values = cms.vdouble( 0.8677 ) , uncertainties = cms.vdouble( 0.0195 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.6300, 20.0000 ) , upBounds = cms.vdouble( -1.5660, 35.0000 ) , values = cms.vdouble( 0.9636 ) , uncertainties = cms.vdouble( 0.0123 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.6300, 35.0000 ) , upBounds = cms.vdouble( -1.5660, 50.0000 ) , values = cms.vdouble( 0.9872 ) , uncertainties = cms.vdouble( 0.0071 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.6300, 50.0000 ) , upBounds = cms.vdouble( -1.5660, 80.0000 ) , values = cms.vdouble( 0.9916 ) , uncertainties = cms.vdouble( 0.0064 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.6300, 80.0000 ) , upBounds = cms.vdouble( -1.5660, 90.0000 ) , values = cms.vdouble( 0.9916 ) , uncertainties = cms.vdouble( 0.0119 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.6300, 90.0000 ) , upBounds = cms.vdouble( -1.5660, 150.0000 ) , values = cms.vdouble( 1.0068 ) , uncertainties = cms.vdouble( 0.0148 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.6300, 150.0000 ) , upBounds = cms.vdouble( -1.5660, 9999999.0000 ) , values = cms.vdouble( 1.0068 ) , uncertainties = cms.vdouble( 0.0153 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -1.5660, 0.0000 ) , upBounds = cms.vdouble( -1.4440, 20.0000 ) , values = cms.vdouble( 1.0049 ) , uncertainties = cms.vdouble( 0.1274 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.5660, 20.0000 ) , upBounds = cms.vdouble( -1.4440, 35.0000 ) , values = cms.vdouble( 0.9616 ) , uncertainties = cms.vdouble( 0.1906 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.5660, 35.0000 ) , upBounds = cms.vdouble( -1.4440, 50.0000 ) , values = cms.vdouble( 0.9607 ) , uncertainties = cms.vdouble( 0.0265 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.5660, 50.0000 ) , upBounds = cms.vdouble( -1.4440, 80.0000 ) , values = cms.vdouble( 0.9585 ) , uncertainties = cms.vdouble( 0.0274 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.5660, 80.0000 ) , upBounds = cms.vdouble( -1.4440, 90.0000 ) , values = cms.vdouble( 0.9585 ) , uncertainties = cms.vdouble( 0.0291 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.5660, 90.0000 ) , upBounds = cms.vdouble( -1.4440, 150.0000 ) , values = cms.vdouble( 1.0211 ) , uncertainties = cms.vdouble( 0.0396 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.5660, 150.0000 ) , upBounds = cms.vdouble( -1.4440, 9999999.0000 ) , values = cms.vdouble( 1.0211 ) , uncertainties = cms.vdouble( 0.0398 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -1.4440, 0.0000 ) , upBounds = cms.vdouble( -1.2000, 20.0000 ) , values = cms.vdouble( 0.9692 ) , uncertainties = cms.vdouble( 0.0140 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.4440, 20.0000 ) , upBounds = cms.vdouble( -1.2000, 35.0000 ) , values = cms.vdouble( 0.9648 ) , uncertainties = cms.vdouble( 0.0136 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.4440, 35.0000 ) , upBounds = cms.vdouble( -1.2000, 50.0000 ) , values = cms.vdouble( 0.9725 ) , uncertainties = cms.vdouble( 0.0042 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.4440, 50.0000 ) , upBounds = cms.vdouble( -1.2000, 80.0000 ) , values = cms.vdouble( 0.9760 ) , uncertainties = cms.vdouble( 0.0070 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.4440, 80.0000 ) , upBounds = cms.vdouble( -1.2000, 90.0000 ) , values = cms.vdouble( 0.9760 ) , uncertainties = cms.vdouble( 0.0121 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.4440, 90.0000 ) , upBounds = cms.vdouble( -1.2000, 150.0000 ) , values = cms.vdouble( 0.9929 ) , uncertainties = cms.vdouble( 0.0143 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.4440, 150.0000 ) , upBounds = cms.vdouble( -1.2000, 9999999.0000 ) , values = cms.vdouble( 0.9929 ) , uncertainties = cms.vdouble( 0.0148 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -1.2000, 0.0000 ) , upBounds = cms.vdouble( -1.0000, 20.0000 ) , values = cms.vdouble( 0.9652 ) , uncertainties = cms.vdouble( 0.0145 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.2000, 20.0000 ) , upBounds = cms.vdouble( -1.0000, 35.0000 ) , values = cms.vdouble( 0.9609 ) , uncertainties = cms.vdouble( 0.0140 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.2000, 35.0000 ) , upBounds = cms.vdouble( -1.0000, 50.0000 ) , values = cms.vdouble( 0.9685 ) , uncertainties = cms.vdouble( 0.0055 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.2000, 50.0000 ) , upBounds = cms.vdouble( -1.0000, 80.0000 ) , values = cms.vdouble( 0.9720 ) , uncertainties = cms.vdouble( 0.0079 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.2000, 80.0000 ) , upBounds = cms.vdouble( -1.0000, 90.0000 ) , values = cms.vdouble( 0.9720 ) , uncertainties = cms.vdouble( 0.0126 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.2000, 90.0000 ) , upBounds = cms.vdouble( -1.0000, 150.0000 ) , values = cms.vdouble( 0.9888 ) , uncertainties = cms.vdouble( 0.0148 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.2000, 150.0000 ) , upBounds = cms.vdouble( -1.0000, 9999999.0000 ) , values = cms.vdouble( 0.9888 ) , uncertainties = cms.vdouble( 0.0152 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -1.0000, 0.0000 ) , upBounds = cms.vdouble( -0.8000, 20.0000 ) , values = cms.vdouble( 0.9612 ) , uncertainties = cms.vdouble( 0.0139 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.0000, 20.0000 ) , upBounds = cms.vdouble( -0.8000, 35.0000 ) , values = cms.vdouble( 0.9569 ) , uncertainties = cms.vdouble( 0.0135 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.0000, 35.0000 ) , upBounds = cms.vdouble( -0.8000, 50.0000 ) , values = cms.vdouble( 0.9645 ) , uncertainties = cms.vdouble( 0.0040 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.0000, 50.0000 ) , upBounds = cms.vdouble( -0.8000, 80.0000 ) , values = cms.vdouble( 0.9680 ) , uncertainties = cms.vdouble( 0.0069 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.0000, 80.0000 ) , upBounds = cms.vdouble( -0.8000, 90.0000 ) , values = cms.vdouble( 0.9680 ) , uncertainties = cms.vdouble( 0.0120 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.0000, 90.0000 ) , upBounds = cms.vdouble( -0.8000, 150.0000 ) , values = cms.vdouble( 0.9847 ) , uncertainties = cms.vdouble( 0.0142 ) ),
	cms.PSet( lowBounds = cms.vdouble( -1.0000, 150.0000 ) , upBounds = cms.vdouble( -0.8000, 9999999.0000 ) , values = cms.vdouble( 0.9847 ) , uncertainties = cms.vdouble( 0.0147 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -0.8000, 0.0000 ) , upBounds = cms.vdouble( -0.6000, 20.0000 ) , values = cms.vdouble( 0.9495 ) , uncertainties = cms.vdouble( 0.0220 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.8000, 20.0000 ) , upBounds = cms.vdouble( -0.6000, 35.0000 ) , values = cms.vdouble( 0.9535 ) , uncertainties = cms.vdouble( 0.0151 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.8000, 35.0000 ) , upBounds = cms.vdouble( -0.6000, 50.0000 ) , values = cms.vdouble( 0.9582 ) , uncertainties = cms.vdouble( 0.0038 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.8000, 50.0000 ) , upBounds = cms.vdouble( -0.6000, 80.0000 ) , values = cms.vdouble( 0.9587 ) , uncertainties = cms.vdouble( 0.0059 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.8000, 80.0000 ) , upBounds = cms.vdouble( -0.6000, 90.0000 ) , values = cms.vdouble( 0.9587 ) , uncertainties = cms.vdouble( 0.0114 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.8000, 90.0000 ) , upBounds = cms.vdouble( -0.6000, 150.0000 ) , values = cms.vdouble( 0.9785 ) , uncertainties = cms.vdouble( 0.0163 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.8000, 150.0000 ) , upBounds = cms.vdouble( -0.6000, 9999999.0000 ) , values = cms.vdouble( 0.9785 ) , uncertainties = cms.vdouble( 0.0167 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -0.6000, 0.0000 ) , upBounds = cms.vdouble( -0.4000, 20.0000 ) , values = cms.vdouble( 0.9525 ) , uncertainties = cms.vdouble( 0.0226 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.6000, 20.0000 ) , upBounds = cms.vdouble( -0.4000, 35.0000 ) , values = cms.vdouble( 0.9565 ) , uncertainties = cms.vdouble( 0.0160 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.6000, 35.0000 ) , upBounds = cms.vdouble( -0.4000, 50.0000 ) , values = cms.vdouble( 0.9612 ) , uncertainties = cms.vdouble( 0.0063 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.6000, 50.0000 ) , upBounds = cms.vdouble( -0.4000, 80.0000 ) , values = cms.vdouble( 0.9617 ) , uncertainties = cms.vdouble( 0.0078 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.6000, 80.0000 ) , upBounds = cms.vdouble( -0.4000, 90.0000 ) , values = cms.vdouble( 0.9617 ) , uncertainties = cms.vdouble( 0.0125 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.6000, 90.0000 ) , upBounds = cms.vdouble( -0.4000, 150.0000 ) , values = cms.vdouble( 0.9815 ) , uncertainties = cms.vdouble( 0.0171 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.6000, 150.0000 ) , upBounds = cms.vdouble( -0.4000, 9999999.0000 ) , values = cms.vdouble( 0.9815 ) , uncertainties = cms.vdouble( 0.0175 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -0.4000, 0.0000 ) , upBounds = cms.vdouble( -0.2000, 20.0000 ) , values = cms.vdouble( 0.9495 ) , uncertainties = cms.vdouble( 0.0226 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.4000, 20.0000 ) , upBounds = cms.vdouble( -0.2000, 35.0000 ) , values = cms.vdouble( 0.9535 ) , uncertainties = cms.vdouble( 0.0160 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.4000, 35.0000 ) , upBounds = cms.vdouble( -0.2000, 50.0000 ) , values = cms.vdouble( 0.9582 ) , uncertainties = cms.vdouble( 0.0065 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.4000, 50.0000 ) , upBounds = cms.vdouble( -0.2000, 80.0000 ) , values = cms.vdouble( 0.9587 ) , uncertainties = cms.vdouble( 0.0079 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.4000, 80.0000 ) , upBounds = cms.vdouble( -0.2000, 90.0000 ) , values = cms.vdouble( 0.9587 ) , uncertainties = cms.vdouble( 0.0126 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.4000, 90.0000 ) , upBounds = cms.vdouble( -0.2000, 150.0000 ) , values = cms.vdouble( 0.9785 ) , uncertainties = cms.vdouble( 0.0172 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.4000, 150.0000 ) , upBounds = cms.vdouble( -0.2000, 9999999.0000 ) , values = cms.vdouble( 0.9785 ) , uncertainties = cms.vdouble( 0.0176 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( -0.2000, 0.0000 ) , upBounds = cms.vdouble( 0.0000, 20.0000 ) , values = cms.vdouble( 0.9484 ) , uncertainties = cms.vdouble( 0.0223 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.2000, 20.0000 ) , upBounds = cms.vdouble( 0.0000, 35.0000 ) , values = cms.vdouble( 0.9524 ) , uncertainties = cms.vdouble( 0.0156 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.2000, 35.0000 ) , upBounds = cms.vdouble( 0.0000, 50.0000 ) , values = cms.vdouble( 0.9571 ) , uncertainties = cms.vdouble( 0.0055 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.2000, 50.0000 ) , upBounds = cms.vdouble( 0.0000, 80.0000 ) , values = cms.vdouble( 0.9575 ) , uncertainties = cms.vdouble( 0.0072 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.2000, 80.0000 ) , upBounds = cms.vdouble( 0.0000, 90.0000 ) , values = cms.vdouble( 0.9575 ) , uncertainties = cms.vdouble( 0.0121 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.2000, 90.0000 ) , upBounds = cms.vdouble( 0.0000, 150.0000 ) , values = cms.vdouble( 0.9773 ) , uncertainties = cms.vdouble( 0.0168 ) ),
	cms.PSet( lowBounds = cms.vdouble( -0.2000, 150.0000 ) , upBounds = cms.vdouble( 0.0000, 9999999.0000 ) , values = cms.vdouble( 0.9773 ) , uncertainties = cms.vdouble( 0.0172 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 0.0000, 0.0000 ) , upBounds = cms.vdouble( 0.2000, 20.0000 ) , values = cms.vdouble( 0.9334 ) , uncertainties = cms.vdouble( 0.0223 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.0000, 20.0000 ) , upBounds = cms.vdouble( 0.2000, 35.0000 ) , values = cms.vdouble( 0.9577 ) , uncertainties = cms.vdouble( 0.0157 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.0000, 35.0000 ) , upBounds = cms.vdouble( 0.2000, 50.0000 ) , values = cms.vdouble( 0.9654 ) , uncertainties = cms.vdouble( 0.0056 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.0000, 50.0000 ) , upBounds = cms.vdouble( 0.2000, 80.0000 ) , values = cms.vdouble( 0.9647 ) , uncertainties = cms.vdouble( 0.0072 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.0000, 80.0000 ) , upBounds = cms.vdouble( 0.2000, 90.0000 ) , values = cms.vdouble( 0.9647 ) , uncertainties = cms.vdouble( 0.0121 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.0000, 90.0000 ) , upBounds = cms.vdouble( 0.2000, 150.0000 ) , values = cms.vdouble( 0.9856 ) , uncertainties = cms.vdouble( 0.0169 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.0000, 150.0000 ) , upBounds = cms.vdouble( 0.2000, 9999999.0000 ) , values = cms.vdouble( 0.9856 ) , uncertainties = cms.vdouble( 0.0173 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 0.2000, 0.0000 ) , upBounds = cms.vdouble( 0.4000, 20.0000 ) , values = cms.vdouble( 0.9374 ) , uncertainties = cms.vdouble( 0.0226 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.2000, 20.0000 ) , upBounds = cms.vdouble( 0.4000, 35.0000 ) , values = cms.vdouble( 0.9618 ) , uncertainties = cms.vdouble( 0.0161 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.2000, 35.0000 ) , upBounds = cms.vdouble( 0.4000, 50.0000 ) , values = cms.vdouble( 0.9695 ) , uncertainties = cms.vdouble( 0.0065 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.2000, 50.0000 ) , upBounds = cms.vdouble( 0.4000, 80.0000 ) , values = cms.vdouble( 0.9689 ) , uncertainties = cms.vdouble( 0.0080 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.2000, 80.0000 ) , upBounds = cms.vdouble( 0.4000, 90.0000 ) , values = cms.vdouble( 0.9689 ) , uncertainties = cms.vdouble( 0.0126 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.2000, 90.0000 ) , upBounds = cms.vdouble( 0.4000, 150.0000 ) , values = cms.vdouble( 0.9898 ) , uncertainties = cms.vdouble( 0.0173 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.2000, 150.0000 ) , upBounds = cms.vdouble( 0.4000, 9999999.0000 ) , values = cms.vdouble( 0.9898 ) , uncertainties = cms.vdouble( 0.0177 ) ),

	cms.PSet( lowBounds = cms.vdouble( 0.4000, 0.0000 ) , upBounds = cms.vdouble( 0.6000, 20.0000 ) , values = cms.vdouble( 0.9364 ) , uncertainties = cms.vdouble( 0.0225 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.4000, 20.0000 ) , upBounds = cms.vdouble( 0.6000, 35.0000 ) , values = cms.vdouble( 0.9608 ) , uncertainties = cms.vdouble( 0.0160 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.4000, 35.0000 ) , upBounds = cms.vdouble( 0.6000, 50.0000 ) , values = cms.vdouble( 0.9685 ) , uncertainties = cms.vdouble( 0.0063 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.4000, 50.0000 ) , upBounds = cms.vdouble( 0.6000, 80.0000 ) , values = cms.vdouble( 0.9679 ) , uncertainties = cms.vdouble( 0.0078 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.4000, 80.0000 ) , upBounds = cms.vdouble( 0.6000, 90.0000 ) , values = cms.vdouble( 0.9679 ) , uncertainties = cms.vdouble( 0.0125 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.4000, 90.0000 ) , upBounds = cms.vdouble( 0.6000, 150.0000 ) , values = cms.vdouble( 0.9888 ) , uncertainties = cms.vdouble( 0.0172 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.4000, 150.0000 ) , upBounds = cms.vdouble( 0.6000, 9999999.0000 ) , values = cms.vdouble( 0.9888 ) , uncertainties = cms.vdouble( 0.0176 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 0.6000, 0.0000 ) , upBounds = cms.vdouble( 0.8000, 20.0000 ) , values = cms.vdouble( 0.9364 ) , uncertainties = cms.vdouble( 0.0220 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.6000, 20.0000 ) , upBounds = cms.vdouble( 0.8000, 35.0000 ) , values = cms.vdouble( 0.9608 ) , uncertainties = cms.vdouble( 0.0152 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.6000, 35.0000 ) , upBounds = cms.vdouble( 0.8000, 50.0000 ) , values = cms.vdouble( 0.9685 ) , uncertainties = cms.vdouble( 0.0038 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.6000, 50.0000 ) , upBounds = cms.vdouble( 0.8000, 80.0000 ) , values = cms.vdouble( 0.9679 ) , uncertainties = cms.vdouble( 0.0059 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.6000, 80.0000 ) , upBounds = cms.vdouble( 0.8000, 90.0000 ) , values = cms.vdouble( 0.9679 ) , uncertainties = cms.vdouble( 0.0115 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.6000, 90.0000 ) , upBounds = cms.vdouble( 0.8000, 150.0000 ) , values = cms.vdouble( 0.9888 ) , uncertainties = cms.vdouble( 0.0164 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.6000, 150.0000 ) , upBounds = cms.vdouble( 0.8000, 9999999.0000 ) , values = cms.vdouble( 0.9888 ) , uncertainties = cms.vdouble( 0.0168 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 0.8000, 0.0000 ) , upBounds = cms.vdouble( 1.0000, 20.0000 ) , values = cms.vdouble( 0.9804 ) , uncertainties = cms.vdouble( 0.0141 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.8000, 20.0000 ) , upBounds = cms.vdouble( 1.0000, 35.0000 ) , values = cms.vdouble( 0.9676 ) , uncertainties = cms.vdouble( 0.0135 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.8000, 35.0000 ) , upBounds = cms.vdouble( 1.0000, 50.0000 ) , values = cms.vdouble( 0.9706 ) , uncertainties = cms.vdouble( 0.0040 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.8000, 50.0000 ) , upBounds = cms.vdouble( 1.0000, 80.0000 ) , values = cms.vdouble( 0.9741 ) , uncertainties = cms.vdouble( 0.0069 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.8000, 80.0000 ) , upBounds = cms.vdouble( 1.0000, 90.0000 ) , values = cms.vdouble( 0.9741 ) , uncertainties = cms.vdouble( 0.0120 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.8000, 90.0000 ) , upBounds = cms.vdouble( 1.0000, 150.0000 ) , values = cms.vdouble( 0.9973 ) , uncertainties = cms.vdouble( 0.0143 ) ),
	cms.PSet( lowBounds = cms.vdouble( 0.8000, 150.0000 ) , upBounds = cms.vdouble( 1.0000, 9999999.0000 ) , values = cms.vdouble( 0.9973 ) , uncertainties = cms.vdouble( 0.0148 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 1.0000, 0.0000 ) , upBounds = cms.vdouble( 1.2000, 20.0000 ) , values = cms.vdouble( 0.9804 ) , uncertainties = cms.vdouble( 0.0146 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.0000, 20.0000 ) , upBounds = cms.vdouble( 1.2000, 35.0000 ) , values = cms.vdouble( 0.9676 ) , uncertainties = cms.vdouble( 0.0141 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.0000, 35.0000 ) , upBounds = cms.vdouble( 1.2000, 50.0000 ) , values = cms.vdouble( 0.9706 ) , uncertainties = cms.vdouble( 0.0055 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.0000, 50.0000 ) , upBounds = cms.vdouble( 1.2000, 80.0000 ) , values = cms.vdouble( 0.9741 ) , uncertainties = cms.vdouble( 0.0079 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.0000, 80.0000 ) , upBounds = cms.vdouble( 1.2000, 90.0000 ) , values = cms.vdouble( 0.9741 ) , uncertainties = cms.vdouble( 0.0126 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.0000, 90.0000 ) , upBounds = cms.vdouble( 1.2000, 150.0000 ) , values = cms.vdouble( 0.9973 ) , uncertainties = cms.vdouble( 0.0148 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.0000, 150.0000 ) , upBounds = cms.vdouble( 1.2000, 9999999.0000 ) , values = cms.vdouble( 0.9973 ) , uncertainties = cms.vdouble( 0.0153 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 1.2000, 0.0000 ) , upBounds = cms.vdouble( 1.4440, 20.0000 ) , values = cms.vdouble( 0.9803 ) , uncertainties = cms.vdouble( 0.0141 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.2000, 20.0000 ) , upBounds = cms.vdouble( 1.4440, 35.0000 ) , values = cms.vdouble( 0.9675 ) , uncertainties = cms.vdouble( 0.0136 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.2000, 35.0000 ) , upBounds = cms.vdouble( 1.4440, 50.0000 ) , values = cms.vdouble( 0.9705 ) , uncertainties = cms.vdouble( 0.0042 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.2000, 50.0000 ) , upBounds = cms.vdouble( 1.4440, 80.0000 ) , values = cms.vdouble( 0.9740 ) , uncertainties = cms.vdouble( 0.0070 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.2000, 80.0000 ) , upBounds = cms.vdouble( 1.4440, 90.0000 ) , values = cms.vdouble( 0.9740 ) , uncertainties = cms.vdouble( 0.0121 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.2000, 90.0000 ) , upBounds = cms.vdouble( 1.4440, 150.0000 ) , values = cms.vdouble( 0.9972 ) , uncertainties = cms.vdouble( 0.0144 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.2000, 150.0000 ) , upBounds = cms.vdouble( 1.4440, 9999999.0000 ) , values = cms.vdouble( 0.9972 ) , uncertainties = cms.vdouble( 0.0149 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 1.4440, 0.0000 ) , upBounds = cms.vdouble( 1.5660, 20.0000 ) , values = cms.vdouble( 1.0161 ) , uncertainties = cms.vdouble( 0.1280 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.4440, 20.0000 ) , upBounds = cms.vdouble( 1.5660, 35.0000 ) , values = cms.vdouble( 0.9581 ) , uncertainties = cms.vdouble( 0.1915 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.4440, 35.0000 ) , upBounds = cms.vdouble( 1.5660, 50.0000 ) , values = cms.vdouble( 0.9531 ) , uncertainties = cms.vdouble( 0.0262 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.4440, 50.0000 ) , upBounds = cms.vdouble( 1.5660, 80.0000 ) , values = cms.vdouble( 0.9571 ) , uncertainties = cms.vdouble( 0.0272 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.4440, 80.0000 ) , upBounds = cms.vdouble( 1.5660, 90.0000 ) , values = cms.vdouble( 0.9571 ) , uncertainties = cms.vdouble( 0.0290 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.4440, 90.0000 ) , upBounds = cms.vdouble( 1.5660, 150.0000 ) , values = cms.vdouble( 0.9986 ) , uncertainties = cms.vdouble( 0.0391 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.4440, 150.0000 ) , upBounds = cms.vdouble( 1.5660, 9999999.0000 ) , values = cms.vdouble( 0.9986 ) , uncertainties = cms.vdouble( 0.0393 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 1.5660, 0.0000 ) , upBounds = cms.vdouble( 1.6300, 20.0000 ) , values = cms.vdouble( 0.8736 ) , uncertainties = cms.vdouble( 0.0195 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.5660, 20.0000 ) , upBounds = cms.vdouble( 1.6300, 35.0000 ) , values = cms.vdouble( 0.9480 ) , uncertainties = cms.vdouble( 0.0123 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.5660, 35.0000 ) , upBounds = cms.vdouble( 1.6300, 50.0000 ) , values = cms.vdouble( 0.9775 ) , uncertainties = cms.vdouble( 0.0071 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.5660, 50.0000 ) , upBounds = cms.vdouble( 1.6300, 80.0000 ) , values = cms.vdouble( 0.9864 ) , uncertainties = cms.vdouble( 0.0064 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.5660, 80.0000 ) , upBounds = cms.vdouble( 1.6300, 90.0000 ) , values = cms.vdouble( 0.9864 ) , uncertainties = cms.vdouble( 0.0119 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.5660, 90.0000 ) , upBounds = cms.vdouble( 1.6300, 150.0000 ) , values = cms.vdouble( 0.9950 ) , uncertainties = cms.vdouble( 0.0147 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.5660, 150.0000 ) , upBounds = cms.vdouble( 1.6300, 9999999.0000 ) , values = cms.vdouble( 0.9950 ) , uncertainties = cms.vdouble( 0.0152 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 1.6300, 0.0000 ) , upBounds = cms.vdouble( 1.8000, 20.0000 ) , values = cms.vdouble( 0.8763 ) , uncertainties = cms.vdouble( 0.0195 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.6300, 20.0000 ) , upBounds = cms.vdouble( 1.8000, 35.0000 ) , values = cms.vdouble( 0.9510 ) , uncertainties = cms.vdouble( 0.0122 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.6300, 35.0000 ) , upBounds = cms.vdouble( 1.8000, 50.0000 ) , values = cms.vdouble( 0.9806 ) , uncertainties = cms.vdouble( 0.0069 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.6300, 50.0000 ) , upBounds = cms.vdouble( 1.8000, 80.0000 ) , values = cms.vdouble( 0.9895 ) , uncertainties = cms.vdouble( 0.0061 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.6300, 80.0000 ) , upBounds = cms.vdouble( 1.8000, 90.0000 ) , values = cms.vdouble( 0.9895 ) , uncertainties = cms.vdouble( 0.0117 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.6300, 90.0000 ) , upBounds = cms.vdouble( 1.8000, 150.0000 ) , values = cms.vdouble( 0.9982 ) , uncertainties = cms.vdouble( 0.0146 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.6300, 150.0000 ) , upBounds = cms.vdouble( 1.8000, 9999999.0000 ) , values = cms.vdouble( 0.9982 ) , uncertainties = cms.vdouble( 0.0151 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 1.8000, 0.0000 ) , upBounds = cms.vdouble( 2.0000, 20.0000 ) , values = cms.vdouble( 0.8755 ) , uncertainties = cms.vdouble( 0.0197 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.8000, 20.0000 ) , upBounds = cms.vdouble( 2.0000, 35.0000 ) , values = cms.vdouble( 0.9501 ) , uncertainties = cms.vdouble( 0.0127 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.8000, 35.0000 ) , upBounds = cms.vdouble( 2.0000, 50.0000 ) , values = cms.vdouble( 0.9796 ) , uncertainties = cms.vdouble( 0.0079 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.8000, 50.0000 ) , upBounds = cms.vdouble( 2.0000, 80.0000 ) , values = cms.vdouble( 0.9885 ) , uncertainties = cms.vdouble( 0.0073 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.8000, 80.0000 ) , upBounds = cms.vdouble( 2.0000, 90.0000 ) , values = cms.vdouble( 0.9885 ) , uncertainties = cms.vdouble( 0.0123 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.8000, 90.0000 ) , upBounds = cms.vdouble( 2.0000, 150.0000 ) , values = cms.vdouble( 0.9972 ) , uncertainties = cms.vdouble( 0.0152 ) ),
	cms.PSet( lowBounds = cms.vdouble( 1.8000, 150.0000 ) , upBounds = cms.vdouble( 2.0000, 9999999.0000 ) , values = cms.vdouble( 0.9972 ) , uncertainties = cms.vdouble( 0.0156 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 2.0000, 0.0000 ) , upBounds = cms.vdouble( 2.2000, 20.0000 ) , values = cms.vdouble( 0.8723 ) , uncertainties = cms.vdouble( 0.0169 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.0000, 20.0000 ) , upBounds = cms.vdouble( 2.2000, 35.0000 ) , values = cms.vdouble( 0.9297 ) , uncertainties = cms.vdouble( 0.0078 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.0000, 35.0000 ) , upBounds = cms.vdouble( 2.2000, 50.0000 ) , values = cms.vdouble( 0.9704 ) , uncertainties = cms.vdouble( 0.0076 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.0000, 50.0000 ) , upBounds = cms.vdouble( 2.2000, 80.0000 ) , values = cms.vdouble( 0.9868 ) , uncertainties = cms.vdouble( 0.0075 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.0000, 80.0000 ) , upBounds = cms.vdouble( 2.2000, 90.0000 ) , values = cms.vdouble( 0.9868 ) , uncertainties = cms.vdouble( 0.0124 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.0000, 90.0000 ) , upBounds = cms.vdouble( 2.2000, 150.0000 ) , values = cms.vdouble( 1.0182 ) , uncertainties = cms.vdouble( 0.0302 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.0000, 150.0000 ) , upBounds = cms.vdouble( 2.2000, 9999999.0000 ) , values = cms.vdouble( 1.0182 ) , uncertainties = cms.vdouble( 0.0304 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 2.2000, 0.0000 ) , upBounds = cms.vdouble( 2.3000, 20.0000 ) , values = cms.vdouble( 0.8751 ) , uncertainties = cms.vdouble( 0.0177 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.2000, 20.0000 ) , upBounds = cms.vdouble( 2.3000, 35.0000 ) , values = cms.vdouble( 0.9326 ) , uncertainties = cms.vdouble( 0.0094 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.2000, 35.0000 ) , upBounds = cms.vdouble( 2.3000, 50.0000 ) , values = cms.vdouble( 0.9734 ) , uncertainties = cms.vdouble( 0.0094 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.2000, 50.0000 ) , upBounds = cms.vdouble( 2.3000, 80.0000 ) , values = cms.vdouble( 0.9898 ) , uncertainties = cms.vdouble( 0.0094 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.2000, 80.0000 ) , upBounds = cms.vdouble( 2.3000, 90.0000 ) , values = cms.vdouble( 0.9898 ) , uncertainties = cms.vdouble( 0.0136 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.2000, 90.0000 ) , upBounds = cms.vdouble( 2.3000, 150.0000 ) , values = cms.vdouble( 1.0213 ) , uncertainties = cms.vdouble( 0.0308 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.2000, 150.0000 ) , upBounds = cms.vdouble( 2.3000, 9999999.0000 ) , values = cms.vdouble( 1.0213 ) , uncertainties = cms.vdouble( 0.0310 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 2.3000, 0.0000 ) , upBounds = cms.vdouble( 2.4000, 20.0000 ) , values = cms.vdouble( 0.8650 ) , uncertainties = cms.vdouble( 0.0179 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.3000, 20.0000 ) , upBounds = cms.vdouble( 2.4000, 35.0000 ) , values = cms.vdouble( 0.9219 ) , uncertainties = cms.vdouble( 0.0101 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.3000, 35.0000 ) , upBounds = cms.vdouble( 2.4000, 50.0000 ) , values = cms.vdouble( 0.9622 ) , uncertainties = cms.vdouble( 0.0101 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.3000, 50.0000 ) , upBounds = cms.vdouble( 2.4000, 80.0000 ) , values = cms.vdouble( 0.9784 ) , uncertainties = cms.vdouble( 0.0101 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.3000, 80.0000 ) , upBounds = cms.vdouble( 2.4000, 90.0000 ) , values = cms.vdouble( 0.9784 ) , uncertainties = cms.vdouble( 0.0142 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.3000, 90.0000 ) , upBounds = cms.vdouble( 2.4000, 150.0000 ) , values = cms.vdouble( 1.0096 ) , uncertainties = cms.vdouble( 0.0308 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.3000, 150.0000 ) , upBounds = cms.vdouble( 2.4000, 9999999.0000 ) , values = cms.vdouble( 1.0096 ) , uncertainties = cms.vdouble( 0.0310 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 2.4000, 0.0000 ) , upBounds = cms.vdouble( 2.4500, 20.0000 ) , values = cms.vdouble( 0.8484 ) , uncertainties = cms.vdouble( 0.0189 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4000, 20.0000 ) , upBounds = cms.vdouble( 2.4500, 35.0000 ) , values = cms.vdouble( 0.9042 ) , uncertainties = cms.vdouble( 0.0122 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4000, 35.0000 ) , upBounds = cms.vdouble( 2.4500, 50.0000 ) , values = cms.vdouble( 0.9437 ) , uncertainties = cms.vdouble( 0.0124 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4000, 50.0000 ) , upBounds = cms.vdouble( 2.4500, 80.0000 ) , values = cms.vdouble( 0.9597 ) , uncertainties = cms.vdouble( 0.0125 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4000, 80.0000 ) , upBounds = cms.vdouble( 2.4500, 90.0000 ) , values = cms.vdouble( 0.9597 ) , uncertainties = cms.vdouble( 0.0159 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4000, 90.0000 ) , upBounds = cms.vdouble( 2.4500, 150.0000 ) , values = cms.vdouble( 0.9902 ) , uncertainties = cms.vdouble( 0.0312 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4000, 150.0000 ) , upBounds = cms.vdouble( 2.4500, 9999999.0000 ) , values = cms.vdouble( 0.9902 ) , uncertainties = cms.vdouble( 0.0315 ) ),
	
	cms.PSet( lowBounds = cms.vdouble( 2.4500, 0.0000 ) , upBounds = cms.vdouble( 6.0000, 20.0000 ) , values = cms.vdouble( 0.7926 ) , uncertainties = cms.vdouble( 0.0222 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4500, 20.0000 ) , upBounds = cms.vdouble( 6.0000, 35.0000 ) , values = cms.vdouble( 0.8447 ) , uncertainties = cms.vdouble( 0.0180 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4500, 35.0000 ) , upBounds = cms.vdouble( 6.0000, 50.0000 ) , values = cms.vdouble( 0.8816 ) , uncertainties = cms.vdouble( 0.0187 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4500, 50.0000 ) , upBounds = cms.vdouble( 6.0000, 80.0000 ) , values = cms.vdouble( 0.8965 ) , uncertainties = cms.vdouble( 0.0189 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4500, 80.0000 ) , upBounds = cms.vdouble( 6.0000, 90.0000 ) , values = cms.vdouble( 0.8965 ) , uncertainties = cms.vdouble( 0.0213 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4500, 90.0000 ) , upBounds = cms.vdouble( 6.0000, 150.0000 ) , values = cms.vdouble( 0.9250 ) , uncertainties = cms.vdouble( 0.0332 ) ),
	cms.PSet( lowBounds = cms.vdouble( 2.4500, 150.0000 ) , upBounds = cms.vdouble( 6.0000, 9999999.0000 ) , values = cms.vdouble( 0.9250 ) , uncertainties = cms.vdouble( 0.0333 ) )

		)
	)	



emptyBins = cms.PSet(
	variables = cms.vstring("1"),
	bins = cms.VPSet()
	)


scalesAndSmearingsPrefix = cms.string("EgammaAnalysis/ElectronTools/data/Winter_2016_reReco_v1_ele")


MCSmearHighR9EB_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronSmearStochasticEGMTool"),
		MethodName = cms.string("FlashggElectrons2D"),
		Label = cms.string("MCSmearHighR9EB"),
		FirstParameterName = cms.string("Rho"),
		SecondParameterName = cms.string("Phi"),
		CorrectionFile = scalesAndSmearingsPrefix,
		NSigmas = cms.PSet( firstVar = cms.vint32(1,-1,0,0),
							secondVar = cms.vint32(0,0,1,-1)),
		OverallRange = cms.string("full5x5_r9>0.94&&abs(superCluster.eta)<1.5"),
		BinList = emptyBins,
		# has to match the labels embedded in the photon object as
		# defined e.g. in dafne/MicroAOD/python/flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		#           or in flashgg/MicroAOD/python/flashggRandomizedElectronProducer_cff.py (if at MicroAOD prod.)
		# RandomLabel = cms.string("rnd_g_E"), #for flashggRandomizedElectronProducer_cff.py
		RandomLabel = cms.string("smearE"),    #for flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		Debug = cms.untracked.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		ApplyCentralValue = cms.bool(True)
		)

MCSmearLowR9EB_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronSmearStochasticEGMTool"),
		MethodName = cms.string("FlashggElectrons2D"),
		Label = cms.string("MCSmearLowR9EB"),
		FirstParameterName = cms.string("Rho"),
		SecondParameterName = cms.string("Phi"),
		CorrectionFile = scalesAndSmearingsPrefix,
		NSigmas = cms.PSet( firstVar = cms.vint32(1,-1,0,0),
							secondVar = cms.vint32(0,0,1,-1)),
		OverallRange = cms.string("full5x5_r9<=0.94&&abs(superCluster.eta)<1.5"),
		BinList = emptyBins,
		# has to match the labels embedded in the photon object as
		# defined e.g. in dafne/MicroAOD/python/flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		#           or in flashgg/MicroAOD/python/flashggRandomizedElectronProducer_cff.py (if at MicroAOD prod.)
		# RandomLabel = cms.string("rnd_g_E"), #for flashggRandomizedElectronProducer_cff.py
		RandomLabel = cms.string("smearE"),    #for flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		Debug = cms.untracked.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		ApplyCentralValue = cms.bool(True)
		)

MCSmearHighR9EE_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronSmearStochasticEGMTool"),  
		MethodName = cms.string("FlashggElectrons2D"),
		Label = cms.string("MCSmearHighR9EE"),
		FirstParameterName = cms.string("Rho"),
		SecondParameterName = cms.string("Phi"),
		CorrectionFile = scalesAndSmearingsPrefix,
		NSigmas = cms.PSet( firstVar = cms.vint32(1,-1,0,0),
							secondVar = cms.vint32(0,0,1,-1)),
		OverallRange = cms.string("full5x5_r9>0.94&&abs(superCluster.eta)>=1.5"),
		BinList = emptyBins,
		# has to match the labels embedded in the photon object as
		# defined e.g. in dafne/MicroAOD/python/flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		#           or in flashgg/MicroAOD/python/flashggRandomizedElectronProducer_cff.py (if at MicroAOD prod.)
		# RandomLabel = cms.string("rnd_g_E"), #for flashggRandomizedElectronProducer_cff.py
		RandomLabel = cms.string("smearE"),    #for flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		Debug = cms.untracked.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		ApplyCentralValue = cms.bool(True)
		)

MCSmearLowR9EE_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronSmearStochasticEGMTool"),
		MethodName = cms.string("FlashggElectrons2D"),
		Label = cms.string("MCSmearLowR9EE"),
		FirstParameterName = cms.string("Rho"),
		SecondParameterName = cms.string("Phi"),
		CorrectionFile = scalesAndSmearingsPrefix,
		NSigmas = cms.PSet( firstVar = cms.vint32(1,-1,0,0),
							secondVar = cms.vint32(0,0,1,-1)),
		OverallRange = cms.string("full5x5_r9<=0.94&&abs(superCluster.eta)>=1.5"),
		BinList = emptyBins,
		# has to match the labels embedded in the photon object as
		# defined e.g. in dafne/MicroAOD/python/flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		#           or in flashgg/MicroAOD/python/flashggRandomizedElectronProducer_cff.py (if at MicroAOD prod.)
		# RandomLabel = cms.string("rnd_g_E"), #for flashggRandomizedElectronProducer_cff.py
		RandomLabel = cms.string("smearE"),    #for flashggRandomizedElectronForDiLeptonDiJetProducer_cff.py
		Debug = cms.untracked.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		ApplyCentralValue = cms.bool(True)
		)


MCScaleHighR9EB_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronScaleEGMTool"),
		MethodName = cms.string("FlashggElectrons1D"),
		Label = cms.string("MCScaleHighR9EB"),
		NSigmas = cms.vint32(-1,1),
		OverallRange = cms.string("full5x5_r9>0.94&&abs(superCluster.eta)<1.5"),
		BinList = emptyBins,
		CorrectionFile = scalesAndSmearingsPrefix,
		ApplyCentralValue = cms.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		Debug = cms.untracked.bool(False)
		)

MCScaleLowR9EB_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronScaleEGMTool"),
		MethodName = cms.string("FlashggElectrons1D"),
		Label = cms.string("MCScaleLowR9EB"),
		NSigmas = cms.vint32(-1,1),
		OverallRange = cms.string("full5x5_r9<0.94&&abs(superCluster.eta)<1.5"),
		BinList = emptyBins,
		CorrectionFile = scalesAndSmearingsPrefix,
		ApplyCentralValue = cms.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		Debug = cms.untracked.bool(False)
		)

MCScaleHighR9EE_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronScaleEGMTool"),
		MethodName = cms.string("FlashggElectrons1D"),
		Label = cms.string("MCScaleHighR9EE"),
		NSigmas = cms.vint32(-1,1),
		OverallRange = cms.string("full5x5_r9>0.94&&abs(superCluster.eta)>=1.5"),
		BinList = emptyBins,
		CorrectionFile = scalesAndSmearingsPrefix,
		ApplyCentralValue = cms.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		Debug = cms.untracked.bool(False)
		)

MCScaleLowR9EE_EGM = cms.PSet( ElectronMethodName = cms.string("FlashggElectronScaleEGMTool"),
		MethodName = cms.string("FlashggElectrons1D"),
		Label = cms.string("MCScaleLowR9EE"),
		NSigmas = cms.vint32(-1,1),
		OverallRange = cms.string("full5x5_r9<0.94&&abs(superCluster.eta)>=1.5"),
		BinList = emptyBins,
		CorrectionFile = scalesAndSmearingsPrefix,
		ApplyCentralValue = cms.bool(False),
		ExaggerateShiftUp = cms.bool(False),
		Debug = cms.untracked.bool(False)
		)




flashggElectronSystematics = cms.EDProducer('FlashggElectronEffSystematicProducer',
											src = cms.InputTag("flashggSelectedElectrons"),
											SystMethods2D = cms.VPSet(),
											SystMethods = cms.VPSet(cms.PSet( MethodName = cms.string("FlashggElectronWeight"),
																			  Label = cms.string("ElectronWeight"),
																			  NSigmas = cms.vint32(-1,1),
																			  OverallRange = cms.string("abs(eta)<2.5"),
																			  BinList = binInfo,
																			  Debug = cms.untracked.bool(False),
																			  ApplyCentralValue = cms.bool(True)
																			  )	
																	)
											)



flashggEleSystematics = cms.EDProducer('FlashggElectronSystematicProducer',
		src = cms.InputTag("flashggSelectedElectrons"),
		SystMethods2D = cms.VPSet(
				MCSmearHighR9EB_EGM,
				MCSmearLowR9EB_EGM,
				MCSmearHighR9EE_EGM,
				MCSmearLowR9EE_EGM		
		),
		SystMethods = cms.VPSet(
				MCScaleHighR9EB_EGM,
				MCScaleLowR9EB_EGM,
				MCScaleHighR9EE_EGM,
				MCScaleLowR9EE_EGM
		)
)

