# import soundcard as sc
# import soundfile as sf
# import numpy as np

# samplerate = 16000
# seconds = 5

# mic = sc.get_microphone("Stereo Mix", include_loopback=True)

# print("Recording...")

# with mic.recorder(samplerate=samplerate) as rec:
#     data = rec.record(numframes=samplerate * seconds)

# sf.write("live.wav", data, samplerate)

# print("Saved: live.wav")




import soundcard as sc
import soundfile as sf

SAMPLERATE = 16000
SECONDS = 5

# Stereo Mix use karo
mic = sc.get_microphone("Stereo Mix", include_loopback=True)

print("Recording system audio for 5 seconds...")

with mic.recorder(samplerate=SAMPLERATE) as recorder:
    data = recorder.record(numframes=SAMPLERATE * SECONDS)

sf.write("live.wav", data, SAMPLERATE)

print("Done!")
print("Saved as live.wav")