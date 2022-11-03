MSQUARK = msquark_template
MCHI = mchi_template
CTAU = ctau_template
WIDTH = 0.0197e-11 / CTAU

SLHA_TABLE = '''
BLOCK SPINFO      # Spectrum calculator information
    1   SOFTSUSY    # spectrum calculator
    2   2.0.5         # version number

BLOCK MODSEL      # Model selection
    1    1        #

BLOCK MASS        # Mass Spectrum
#   PDG code   mass  particle
# PDG code           mass       particle
   1000001     {msquark:E}      # ~d_L
   2000001     {msquark:E}      # ~d_R
   1000002     {msquark:E}      # ~u_L
   2000002     {msquark:E}      # ~u_R
   1000003     {msquark:E}      # ~s_L
   2000003     {msquark:E}      # ~s_R
   1000004     {msquark:E}      # ~c_L
   2000004     {msquark:E}      # ~c_R
   1000005     {msquark:E}      # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     {msquark:E}    # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     1.00000000E+05   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     1.00000000E+05   # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     1.00000000E+05   # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     1.00000000E+05   # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     {mchi:E}       # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     1.00000000E+05   # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+

DECAY   1000001     5.31278772E+00   # sdown_L decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   1   # BR(~d_L -> ~chi_10 d)
DECAY   2000001     2.85812308E-01   # sdown_R decays
#          BR         NDA      ID1       ID2
      1000000E+00     2        1000022   1   # BR(~d_R -> ~chi_10 d)
DECAY   1000002     5.47719539E+00   # sup_L decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   2   # BR(~u_L -> ~chi_10 u)
DECAY   2000002     1.15297292E+00   # sup_R decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   2   # BR(~u_R -> ~chi_10 u)
DECAY   1000003     5.31278772E+00   # sstrange_L decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   3   # BR(~s_L -> ~chi_10 s)
DECAY   2000003     2.85812308E-01   # sstrange_R decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   3   # BR(~s_R -> ~chi_10 s)
DECAY   1000004     5.47719539E+00   # scharm_L decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   4   # BR(~c_L -> ~chi_10 c)
DECAY   2000004     1.15297292E+00   # scharm_R decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   4   # BR(~c_R -> ~chi_10 c)
DECAY   1000005     3.73627601E+00   # sbottom1 decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   5   # BR(~b_1 -> ~chi_10 b )
DECAY   1000006     1.97326971684839e-13   # stop1 decays
#          BR         NDA      ID1       ID2
      1.00000E+00     2        1000022   6   # BR(~t_1 -> ~chi_10 t )
DECAY   1000022     {width:E}              # neutralino1 decays
#          BR         NDA      ID1       ID2      ID3
      0.25000E+00     3        11       -11       12   # BR(~chi_10 -> e+   e-   nu_e)
      0.25000E+00     3        13       -13       14   # BR(~chi_10 -> mu+  mu-  nu_mu)
      0.25000E+00     3        11       -11       14   # BR(~chi_10 -> e+   e-   nu_mu)
      0.25000E+00     3        13       -13       12   # BR(~chi_10 -> mu+  mu-  nu_e)
'''.format(msquark = MSQUARK, mchi = MCHI, width = WIDTH)


import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter('Pythia8ConcurrentGeneratorFilter',
    comEnergy = cms.double(13600.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    SLHATableForPythia8 = cms.string(SLHA_TABLE),
    PythiaParameters = cms.PSet(
	pythia8CommonSettingsBlock,
	pythia8CP5SettingsBlock,
	processParameters = cms.vstring(
	    'SUSY:all = off',
	    'SUSY:gg2squarkantisquark  = on',
	    'SUSY:qqbar2squarkantisquark= on',
	    'RHadrons:allow  = off',
	    'RHadrons:allowDecay = off',
	    'RHadrons:setMasses = off',
	    '1000022:tau0 = %f' % CTAU,
	    ),
	parameterSets = cms.vstring(
	    'pythia8CommonSettings',
	    'pythia8CP5Settings',
	    'processParameters',
	    ),
	),
    )
