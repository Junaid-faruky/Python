import wave
import numpy as np
import matplotlib.pyplot as plt

wf = wave.open("sample.wav", "rb")
frames = wf.readframes(wf.getnframes())
data = np.frombuffer(frames, dtype=np.int16)
plt.plot(data[:1000])
plt.title("Waveform (first chunk)")
plt.show()
