# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:49:23 2024

@author: be681pek
"""

import pyaudio
import numpy
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220

p = pyaudio.PyAudio()
print('running')

stream = p.open(format=FORMAT, channels=1,rate=SAMPLEFREQ,
input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.frombuffer(data, dtype=int);

stream.stop_stream()
stream.close()
p.terminate()
numpy.save("tief5.npy", p)
print('done')
plt.plot(decoded)
plt.show()