import matplotlib.pyplot as plt
import numpy as np
import wave

wav = wave.open("song.wav", "r")
signal = wav.readframes(-1)
signal = np.frombuffer(signal, dtype=np.int16)

plt.specgram(signal, Fs=wav.getframerate())
plt.title("Music Visualizer")
plt.show()
