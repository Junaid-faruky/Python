import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from typing import Callable, List
import threading
import time

class RealTimeAudioProcessor:
    def __init__(self, sample_rate: int = 44100, chunk_size: int = 1024):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.audio = pyaudio.PyAudio()
        self.is_recording = False
        self.processors: List[Callable] = []
        
    def add_processor(self, processor: Callable):
        self.processors.append(processor)
    
    def apply_processors(self, audio_data: np.ndarray) -> np.ndarray:
        processed = audio_data.copy()
        for processor in self.processors:
            processed = processor(processed)
        return processed
    
    def low_pass_filter(self, cutoff: float = 4000):
        def processor(audio_data: np.ndarray) -> np.ndarray:
            nyquist = 0.5 * self.sample_rate
            normal_cutoff = cutoff / nyquist
            b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)
            return signal.filtfilt(b, a, audio_data)
        return processor
    
    def high_pass_filter(self, cutoff: float = 200):
        def processor(audio_data: np.ndarray) -> np.ndarray:
            nyquist = 0.5 * self.sample_rate
            normal_cutoff = cutoff / nyquist
            b, a = signal.butter(4, normal_cutoff, btype='high', analog=False)
            return signal.filtfilt(b, a, audio_data)
        return processor
    
    def compressor(self, threshold: float = 0.5, ratio: float = 4.0):
        def processor(audio_data: np.ndarray) -> np.ndarray:
            compressed = np.zeros_like(audio_data)
            for i in range(len(audio_data)):
                if abs(audio_data[i]) > threshold:
                    compressed[i] = threshold + (audio_data[i] - threshold) / ratio
                else:
                    compressed[i] = audio_data[i]
            return compressed
        return processor
    
    def fft_analysis(self, audio_data: np.ndarray) -> tuple:
        fft = np.fft.fft(audio_data)
        freqs = np.fft.fftfreq(len(audio_data), 1/self.sample_rate)
        return freqs[:len(freqs)//2], np.abs(fft[:len(fft)//2])
    
    def start_recording(self, callback: Callable = None):
        def audio_callback(in_data, frame_count, time_info, status):
            audio_array = np.frombuffer(in_data, dtype=np.float32)
            processed = self.apply_processors(audio_array)
            
            if callback:
                callback(processed)
            
            return (processed.astype(np.float32).tobytes(), pyaudio.paContinue)
        
        self.stream = self.audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            input=True,
            output=True,
            frames_per_buffer=self.chunk_size,
            stream_callback=audio_callback
        )
        
        self.is_recording = True
        self.stream.start_stream()
    
    def stop_recording(self):
        if self.is_recording:
            self.stream.stop_stream()
            self.stream.close()
            self.is_recording = False
    
    def visualize_audio(self, audio_data: np.ndarray):
        plt.figure(figsize=(12, 8))
        
        # Time domain
        plt.subplot(2, 1, 1)
        plt.plot(np.arange(len(audio_data)) / self.sample_rate, audio_data)
        plt.title('Time Domain')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        
        # Frequency domain
        plt.subplot(2, 1, 2)
        freqs, magnitudes = self.fft_analysis(audio_data)
        plt.plot(freqs, magnitudes)
        plt.title('Frequency Domain')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.xlim(0, 5000)
        
        plt.tight_layout()
        plt.show()

# Example usage
processor = RealTimeAudioProcessor()
processor.add_processor(processor.low_pass_filter(3000))
processor.add_processor(processor.compressor(0.3, 3.0))

def audio_callback(data):
    # Real-time processing callback
    pass

# Start processing in background thread
thread = threading.Thread(target=processor.start_recording, args=(audio_callback,))
thread.start()

# Let it run for 5 seconds
time.sleep(5)
processor.stop_recording()
