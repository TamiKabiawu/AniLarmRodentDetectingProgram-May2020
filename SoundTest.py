import pyaudio
import numpy as np
import Truncate as tr

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
#input number for how long you want it to run. Any sounds above the peak(dB) have the time that they were recorded.
for i in range(int(20.476 * int(input()))): #20.476 * each second
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    bars="#"*int(50*peak/2**16)
    if (peak/325 > 50):
        print("%s %s "%(tr.truncate((i/20.476),2), bars))
       # print("%04d %05d %s"%((i/20.476)+1,peak/325,bars))

stream.stop_stream()
stream.close()
p.terminate()