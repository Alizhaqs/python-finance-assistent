import os
import io
import wave

with wave.open('audio/test1.wav',"rb") as wave_file:
    frame_rate = wave_file.getframerate()
    print(wave_file.getparams())
    print(wave_file.getsampwidth())