# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SquarkToNeutralinoTo2LNu-MSquark_1500_MChi_494_ctau_10000mm-fragment.py --python_filename TSG-Run3Summer22GS-00039_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:TSG-Run3Summer22GS-00039.root --conditions 124X_mcRun3_2022_realistic_v11 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --no_exec --mc -n 100 --no_exec
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
    input = cms.untracked.int32(100),
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
    annotation = cms.untracked.string('Configuration/GenProduction/python/SquarkToNeutralinoTo2LNu-MSquark_1500_MChi_494_ctau_10000mm-fragment.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
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
    fileName = cms.untracked.string('file:TSG-Run3Summer22GS-00039.root'),
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

process.generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters'
        ),
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:gg2squarkantisquark  = on',
            'SUSY:qqbar2squarkantisquark= on',
            'RHadrons:allow  = off',
            'RHadrons:allowDecay = off',
            'RHadrons:setMasses = off',
            '1000022:tau0 = 10000.000000'
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
    SLHATableForPythia8 = cms.string('\nBLOCK SPINFO      # Spectrum calculator information\n    1   SOFTSUSY    # spectrum calculator\n    2   2.0.5         # version number\n\nBLOCK MODSEL      # Model selection\n    1    1        #\n\nBLOCK MASS        # Mass Spectrum\n#   PDG code   mass  particle\n# PDG code           mass       particle\n   1000001     1.500000E+03      # ~d_L\n   2000001     1.500000E+03      # ~d_R\n   1000002     1.500000E+03      # ~u_L\n   2000002     1.500000E+03      # ~u_R\n   1000003     1.500000E+03      # ~s_L\n   2000003     1.500000E+03      # ~s_R\n   1000004     1.500000E+03      # ~c_L\n   2000004     1.500000E+03      # ~c_R\n   1000005     1.500000E+03      # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     1.500000E+03    # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     1.00000000E+05   # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.00000000E+05   # ~g\n   1000022     4.940000E+02       # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n\nDECAY   1000001     5.31278772E+00   # sdown_L decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   1   # BR(~d_L -> ~chi_10 d)\nDECAY   2000001     2.85812308E-01   # sdown_R decays\n#          BR         NDA      ID1       ID2\n      1000000E+00     2        1000022   1   # BR(~d_R -> ~chi_10 d)\nDECAY   1000002     5.47719539E+00   # sup_L decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   2   # BR(~u_L -> ~chi_10 u)\nDECAY   2000002     1.15297292E+00   # sup_R decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   2   # BR(~u_R -> ~chi_10 u)\nDECAY   1000003     5.31278772E+00   # sstrange_L decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   3   # BR(~s_L -> ~chi_10 s)\nDECAY   2000003     2.85812308E-01   # sstrange_R decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   3   # BR(~s_R -> ~chi_10 s)\nDECAY   1000004     5.47719539E+00   # scharm_L decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   4   # BR(~c_L -> ~chi_10 c)\nDECAY   2000004     1.15297292E+00   # scharm_R decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   4   # BR(~c_R -> ~chi_10 c)\nDECAY   1000005     3.73627601E+00   # sbottom1 decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   5   # BR(~b_1 -> ~chi_10 b )\nDECAY   1000006     1.97326971684839e-13   # stop1 decays\n#          BR         NDA      ID1       ID2\n      1.00000E+00     2        1000022   6   # BR(~t_1 -> ~chi_10 t )\nDECAY   1000022     1.970000E-17              # neutralino1 decays\n#          BR         NDA      ID1       ID2      ID3\n      0.25000E+00     3        11       -11       12   # BR(~chi_10 -> e+   e-   nu_e)\n      0.25000E+00     3        13       -13       14   # BR(~chi_10 -> mu+  mu-  nu_mu)\n      0.25000E+00     3        11       -11       14   # BR(~chi_10 -> e+   e-   nu_mu)\n      0.25000E+00     3        13       -13       12   # BR(~chi_10 -> mu+  mu-  nu_e)\n'),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


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
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

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
