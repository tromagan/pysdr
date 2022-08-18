#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

Fs = 1  # Hz
N = 100  # number of points to simulate, and our FFT size

t = np.arange(N)
s = np.sin(0.15*2*np.pi*t)
s = s * np.hamming(N)
S = np.fft.fftshift(np.fft.fft(s))

S_mag = np.abs(S)
S_phase = np.angle(S)
f = np.arange(Fs/-2, Fs/2, Fs/N)

plt.figure(1)
plt.plot(f, S_mag, '.-')
plt.plot(f, S_phase, '.-')
plt.show()

print("123")