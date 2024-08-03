import numpy as ny
import sounddevice as sd

class Sound_info:

    def __init__(self, frequency, duration):
        self.frequency = frequency
        self.duration = duration
        self.sample_rate = 44100

    def get_signal(self):
        t = ny.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        signal = 0.5 * ny.sin(2 * ny.pi * self.frequency * t)
        return signal
    
    def play_tone(self):
        tone = self.get_signal()
        sd.play(tone, self.sample_rate, blocking=False, latency='low')
        sd.wait()

        