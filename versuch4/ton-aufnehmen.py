# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:26:48 2024

@author: pbegu
"""

import numpy as np
import matplotlib.pyplot as plt
import pyaudio
from scipy.signal import gausspulse
from scipy.signal.windows import gaussian


# Audio recording parameters
FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220

# Initialize PyAudio
p = pyaudio.PyAudio()
print('running')

# Open stream
stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                input=True, frames_per_buffer=FRAMESIZE)

# Read audio data
data = stream.read(NOFFRAMES * FRAMESIZE)
decoded = np.frombuffer(data, dtype=np.int16)

# Close stream
stream.stop_stream()
stream.close()
p.terminate()

# Generate a unique filename
filename = "rechts10.npy"
np.save(filename, decoded)
print(f'Data saved as {filename}')

# Plotting the audio data
time_axis = np.linspace(0, len(decoded) / SAMPLEFREQ, num=len(decoded))

plt.figure(figsize=(10, 4))
plt.plot(time_axis, decoded)
plt.title('Audio Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
