import sounddevice as sd
from scipy.io.wavfile import write

seconds = 5
fs = 44100
print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
write("recording.wav", fs, recording)
print("Saved recording.wav")
