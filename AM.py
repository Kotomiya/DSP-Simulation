import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
fs =1000
T=1.0/fs

t = np.arange(0,1,T)
freq=20
carrier=np.cos(2*np.pi*freq*t)
freq2=5
base=np.cos(2*np.pi*freq2*t)

m=1
sig = (1+m*base)*carrier
FFTsig = np.fft.fft(sig)/fs
FFTfreq = np.fft.fftfreq(fs, T)

plt.subplot(211)
plt.title('Carrier= '+str(freq)+' Hz, '+'Sig= '+str(freq2)+' Hz')
plt.plot(t,sig)
plt.axis([0,1, min(sig)-1,max(sig)+1])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.grid()

plt.subplot(212)
plt.stem(FFTfreq, abs(FFTsig), marker= 'o', linestyle='-')
plt.axis([-2*freq, 2*freq, 0, 1])
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude spectrum")
plt.grid()

plt.show()
