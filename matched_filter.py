import Utils
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc, rcParams
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern'],'size':16})

# Set your favorite parameters
SamplingFrequency = 8192.0
DistanceInMegaparsecs = 10.0
SignalMassInSolarMasses = 5.0
TemplateMassInSolarMasses = 5.0

def NonspinningGW(MassInSolarMasses, DistanceInMegaparsecs=DistanceInMegaparsecs):
    if(MassInSolarMasses<5.0):
        raise ValueError("The mass {0} is too small".format(MassInSolarMasses))
    return Utils.Waveform('Data/rhOverM_EqualMassNonspinning_L2_M2.dat',
        SamplingFrequency, MassInSolarMasses, DistanceInMegaparsecs)

# Make a compact binary coalescence signal
W = NonspinningGW(SignalMassInSolarMasses)

plt.plot(W.t, W.data,'r')
plt.xlabel(r'$t$ (seconds)')
plt.ylabel(r'$h$ (dimensionless strain)')
plt.title(r'Gravitational-wave signal as a function of time');
plt.show()

# Load the LIGO noise
LIGONoise = Utils.Waveform('Data/LIGONoise.dat')

plt.plot(LIGONoise.t, LIGONoise.data,'b')
plt.plot(W.t, W.data,'r')
plt.xlabel(r'$t$ (seconds)')
plt.ylabel(r'$h$ (dimensionless strain)')
plt.title(r'LIGO noise as a function of time');
plt.show()

### Convert to frequency domain
fft_n = LIGONoise.fft() # Take the Fourier transform and save as 'NoiseFFT'
f_n = LIGONoise.f # Values of the f_i

### Now plot it
plt.loglog(f_n, abs(fft_n))
plt.xlim(35.0,2048.0)
plt.ylim(ymin=5e-24)
plt.xlabel(r"$f_i$ (Hertz)")
plt.ylabel(r"$\tilde{n}_{f_i}$ (dimensionless strain)")
plt.title("Amplitude of the Fourier transform of LIGO noise");
plt.show()

# Make up our various signals
TemplateSignal = NonspinningGW(TemplateMassInSolarMasses) # Template signal
SimulatedSignal = Utils.Waveform(LIGONoise) # Make a copy of the noise
SimulatedSignal.data += NonspinningGW(SignalMassInSolarMasses).Roll(1.5).data # Add a GW to the copy's data, and offset it by 1.5 seconds

Match = abs(Utils.Match(SimulatedSignal, TemplateSignal, LIGONoise))

max_index = np.argmax(Match)
max_value = Match[max_index]
max_time = TemplateSignal.t[max_index]
print(r'Maximum value of match is %f at delta_t = %f seconds' % (max_value, max_time))

plt.plot(TemplateSignal.t, Match)
plt.xlim(TemplateSignal.t[0]-1.0,TemplateSignal.t[-1]+1.0)
plt.xlabel(r'$\delta t$ (seconds)')
plt.ylabel(r'$\langle t | n \rangle_{\delta t}$ (dimensionless)')
plt.title(r'Match between the template and pure noise');
plt.show()
