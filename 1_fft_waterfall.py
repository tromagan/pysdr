#!/usr/bin/env python3

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

FFT_N = 1024
W = 100
Fs = 1e6
N = FFT_N*W


def gen_sig(enable_tone=0):
    t = np.arange(FFT_N) / Fs
    f = 90e3  # freq of tone
    y = enable_tone*np.sin(2*np.pi*f*t) + 0.1*np.random.randn(len(t))
    return y


def make_fft(y):
    y = y * np.hamming(FFT_N)
    fft = np.fft.fftshift(np.fft.fft(y))
    fft_amp = 10*np.log10(np.abs(fft)**2)
    return fft_amp


def init_lst():
    l = []
    for r in range(W):
        col = []
        for c in range(FFT_N):
            col.append(0)
        l.append(col)
    return l


fft_lst = init_lst()
# fft_lst = np.array(fft_lst)
fig = plt.figure(1)
plt.ion()
for i in range(100):
    print(i)

    plt.imshow(fft_lst, aspect='auto', extent=[-Fs/2, Fs/2, 0, N/Fs])
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Time [s]")
    plt.pause(0.0001)

    if len(fft_lst) == W:
        fft_lst.pop(0)

    if random.random() >= 0.5:
        y = gen_sig(1)
    else:
        y = gen_sig(0)

    # y = gen_sig(1)
    fft = make_fft(y)
    fft_lst.append(fft)
    # fft_lst[0] = fft;
    # fft_lst = np.roll(fft_lst, 1, 0)
    time.sleep(0.001)

plt.ioff()
plt.show()
