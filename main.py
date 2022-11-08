import os
import io
import wave
import soundfile as sf

with open('audio/test1.wav', 'rb') as file:
    data, samplerate = sf.read(file)
    if sf.check_format('WAV', 'PCM_24') == True:
        print('Proshel proverku na PCM i WAV')
        print(samplerate)
    else:
        print('Ne prowel proverku')
    print(sf.check_format('WAV', 'PCM_16'))
