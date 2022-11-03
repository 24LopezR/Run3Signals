# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/BToHNLEMuX_HNLToEMuLnu_SoftQCD_b_mHNL1p0_ctau1000mm.py --python_filename run_BToHNLEMuX_HNLToEMuLnu_SoftQCD_b_mHNL1p0_ctau1000mm_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:BToHNLEMuX_HNLToEMuLnu_SoftQCD_b_mHNL1p0_ctau1000mm.root --conditions 124X_mcRun3_2022_realistic_v11 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --no_exec --mc -n 1000 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('SIM',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13p6TeVEarly2022Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('B -> mu N X, with long-lived N, m=1.0GeV, ctau=1000.0mm'),
    name = cms.untracked.string('B -> mu N X, with long-lived N, m=1.0GeV, ctau=1000.0mm'),
    version = cms.untracked.string('$1.0$')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:BToHNLEMuX_HNLToEMuLnu_SoftQCD_b_mHNL1p0_ctau1000mm.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
if hasattr(process, "XMLFromDBSource"): process.XMLFromDBSource.label="Extended"
if hasattr(process, "DDDetectorESProducerFromDB"): process.DDDetectorESProducerFromDB.label="Extended"
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_mcRun3_2022_realistic_v11', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            convertPythiaCodes = cms.untracked.bool(False),
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            list_forced_decays = cms.vstring(
                'myB+',
                'myB-',
                'myB0',
                'myB0bar',
                'myB0s',
                'myB0sbar',
                'myHNL_mu',
                'myHNL_e'
            ),
            operates_on_particles = cms.vint32(
                521, -521, 511, -511, 531,
                -531, 9900015
            ),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_BHNL_mass1.0_ctau1000.0_maj.pdl'),
            user_decay_embedded = cms.vstring(
                'Alias myB+ B+',
                'Alias myB- B-',
                'Alias myB0 B0',
                'Alias myB0bar anti-B0',
                'Alias myB0s B_s0',
                'Alias myB0sbar anti-B_s0',
                'Alias myHNL_mu hnl',
                'Alias myHNL_e hnl',
                'ChargeConj myB+ myB-',
                'ChargeConj myB0 myB0bar',
                'ChargeConj myB0s myB0sbar',
                'Decay myB+',
                '0.0391954845               mu+    myHNL_mu    PHSP;',
                '17.8520061116    anti-D0    mu+    myHNL_mu    PHSP;',
                '40.4853103161    anti-D*0   mu+    myHNL_mu    PHSP;',
                '0.0565363004    pi0        mu+    myHNL_mu    PHSP;',
                '0.1516733895    rho0       mu+    myHNL_mu    PHSP;',
                '0.0391954845               mu+    myHNL_e     PHSP;',
                '17.8520061116    anti-D0    mu+    myHNL_e     PHSP;',
                '40.4853103161    anti-D*0   mu+    myHNL_e     PHSP;',
                '0.0565363004    pi0        mu+    myHNL_e     PHSP;',
                '0.1516733895    rho0       mu+    myHNL_e     PHSP;',
                '0.0387325105                e+     myHNL_mu    PHSP;',
                '17.9569707852     anti-D0    e+     myHNL_mu    PHSP;',
                '40.7470748545     anti-D*0   e+     myHNL_mu    PHSP;',
                '0.0565762628     pi0        e+     myHNL_mu    PHSP;',
                '0.1520165497     rho0       e+     myHNL_mu    PHSP;',
                'Enddecay',
                'CDecay myB-',
                'Decay myB0',
                '16.4702373621    D-     mu+    myHNL_mu    PHSP;',
                '37.8988504289    D*-    mu+    myHNL_mu    PHSP;',
                '0.1070098962    pi-    mu+    myHNL_mu    PHSP;',
                '0.2814223316    rho-   mu+    myHNL_mu    PHSP;',
                '16.4702373621    D-     mu+    myHNL_e     PHSP;',
                '37.8988504289    D*-    mu+    myHNL_e     PHSP;',
                '0.1070098962    pi-    mu+    myHNL_e     PHSP;',
                '0.2814223316    rho-   mu+    myHNL_e     PHSP;',
                '16.5674937131     D-     e+     myHNL_mu    PHSP;',
                '38.1426439086     D*-    e+     myHNL_mu    PHSP;',
                '0.1070887366     pi-    e+     myHNL_mu    PHSP;',
                '0.2820587870     rho-   e+     myHNL_mu    PHSP;',
                'Enddecay',
                'CDecay myB0bar',
                'Decay myB0s',
                '16.8729328916    D_s-    mu+    myHNL_mu    PHSP;',
                '38.2158202935    D_s*-   mu+    myHNL_mu    PHSP;',
                '0.1496250929    K-      mu+    myHNL_mu    PHSP;',
                '0.3022850956    K*-     mu+    myHNL_mu    PHSP;',
                '16.8729328916    D_s-    mu+    myHNL_e    PHSP;',
                '38.2158202935    D_s*-   mu+    myHNL_e    PHSP;',
                '0.1496250929    K-      mu+    myHNL_e    PHSP;',
                '0.3022850956    K*-     mu+    myHNL_e    PHSP;',
                '16.9747725407    D_s-     e+     myHNL_mu    PHSP;',
                '38.4658877924    D_s*-    e+     myHNL_mu    PHSP;',
                '0.1498348606    K-       e+     myHNL_mu    PHSP;',
                '0.3030259101    K*-      e+     myHNL_mu    PHSP;',
                'Enddecay',
                'CDecay myB0sbar',
                'Decay myHNL_mu',
                '0.5     mu-    pi+    PHSP;',
                '0.5     mu+    pi-    PHSP;',
                'Enddecay',
                'Decay myHNL_e',
                '0.5     e-    pi+    PHSP;',
                '0.5     e+    pi-    PHSP;',
                'Enddecay',
                'End'
            )
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters'
        ),
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'PTFilter:filter = on',
            'PTFilter:quarkToFilter = 5',
            'PTFilter:scaleToFilter = 5.0'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14',
            'Tune:ee 7',
            'MultipartonInteractions:ecmPow=0.03344',
            'MultipartonInteractions:bProfile=2',
            'MultipartonInteractions:pT0Ref=1.41',
            'MultipartonInteractions:coreRadius=0.7634',
            'MultipartonInteractions:coreFraction=0.63',
            'ColourReconnection:range=5.176',
            'SigmaTotal:zeroAXB=off',
            'SpaceShower:alphaSorder=2',
            'SpaceShower:alphaSvalue=0.118',
            'SigmaProcess:alphaSvalue=0.118',
            'SigmaProcess:alphaSorder=2',
            'MultipartonInteractions:alphaSvalue=0.118',
            'MultipartonInteractions:alphaSorder=2',
            'TimeShower:alphaSorder=2',
            'TimeShower:alphaSvalue=0.118',
            'SigmaTotal:mode = 0',
            'SigmaTotal:sigmaEl = 21.89',
            'SigmaTotal:sigmaTot = 100.309',
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2',
            'Main:timesAllowErrors = 10000',
            'Check:epTolErr = 0.01',
            'Beams:setProductionScalesFromLHEF = off',
            'SLHA:minMassSM = 1000.',
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tau0Max = 10',
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(13600.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.HNLDisplacementFilter = cms.EDFilter("MCDisplacementFilter",
    LengMax = cms.double(1300),
    LengMin = cms.double(0),
    ParticleIDs = cms.vint32(9900015)
)


process.HNLPionFilter = cms.EDFilter("PythiaFilterMultiMother",
    MaxEta = cms.untracked.double(10.0),
    MinEta = cms.untracked.double(-10.0),
    MinPt = cms.untracked.double(0.5),
    MotherIDs = cms.untracked.vint32(9900015),
    ParticleID = cms.untracked.int32(211)
)


process.TriggerMuonFilter = cms.EDFilter("PythiaFilterMultiMother",
    MaxEta = cms.untracked.double(1.55),
    MinEta = cms.untracked.double(-1.55),
    MinPt = cms.untracked.double(6.8),
    MotherIDs = cms.untracked.vint32(521, 511, 531, 9900015),
    ParticleID = cms.untracked.int32(13)
)


process.TripleLeptonFilter = cms.EDFilter("MCMultiParticleFilter",
    AcceptMore = cms.bool(True),
    EtaMax = cms.vdouble(1.55, 2.45, 0),
    NumRequired = cms.int32(3),
    ParticleID = cms.vint32(13, -13),
    PtMin = cms.vdouble(6.8, 1.0, 0.0),
    Status = cms.vint32(1, 1, 1)
)


process.DoubleLeptonFilter = cms.EDFilter("MCParticlePairFilter",
    MaxEta = cms.untracked.vdouble(1.55, 2.45),
    MaxInvMass = cms.untracked.double(10.0),
    MinEta = cms.untracked.vdouble(-1.55, -2.45),
    MinPt = cms.untracked.vdouble(6.8, 1.0),
    ParticleID1 = cms.untracked.vint32(-13, 13),
    ParticleID2 = cms.untracked.vint32(-11, 11, -13, 13),
    Status = cms.untracked.vint32(1, 1)
)


process.BFilter = cms.EDFilter("MCMultiParticleFilter",
    AcceptMore = cms.bool(True),
    EtaMax = cms.vdouble(10.0, 10.0, 10.0),
    NumRequired = cms.int32(1),
    ParticleID = cms.vint32(521, 511, 531),
    PtMin = cms.vdouble(0.0, 0.0, 0.0),
    Status = cms.vint32(0, 0, 0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.BFilter+process.TripleLeptonFilter+process.TriggerMuonFilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfConcurrentLuminosityBlocks = 1
process.options.eventSetup.numberOfConcurrentIOVs = 1
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
