import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/exo_heavyNeutrino/displaced_2017/v1/HeavyNeutrino_trilepton_M-1_V-0.0949736805647_mu_massiveAndCKM_LO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

# Link to cards:
# https://github.com/cms-sw/genproductions/tree/e3bf0a9b8180b78938a34e4d06036d5dd096d8ef/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/exo_heavyNeutrino_LO/HeavyNeutrino_trilepton_M-1_V-0.0949736805647_mu_massiveAndCKM_LO


import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    )
    )
)


# Link to generator fragment:
# https://raw.githubusercontent.com/isildakbora/EXO-MC-REQUESTS/master/Heavy_Neutrino/HeavyNeutrino_trilepton_M-1_V-0.0949736805647_mu_massiveAndCKM_LO.py
