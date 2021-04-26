import pyaudio
import struct #converts strings of bytes to something readable
import numpy as np
import matplotlib.pyplot as plt

print("Hey")

#%matplotlib tk

CHUNK = 1024*4 #how many audio sample per frame to display
FORMAT = pyaudio.paInt16
CHANNELS = 1 #mono sound
RATE = 44100 #samples per second

p = pyaudio.PyAudio() # main pyaudio object

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)



fig, ax = plt.subplots()

plt.show(block=False)

x = np.arange(0, 2*CHUNK, 2) #start at 0 to 2*CHUNK, step size is 2
ax.set_ylim(-255*2, 255*2)
ax.set_xlim(0, CHUNK)

#create line and update line in a loop
line, = ax.plot(x, np.random.rand(CHUNK)) #plot some data that has the right length

while True:
    print("Here again")
    data = stream.read(CHUNK)
    #print(data)
    data_int = np.array(struct.unpack(str(2 * CHUNK)+ 'B', data), dtype='b')[::2] + 128
    print(np.amax(data_int))
    #if len(np.where(data_int == 100))>0:
    #    print("success")
    
    count = 0
    for i in data_int:
        if i == 255:
            count = count + 1
            print("success")
    
    #updates the plot
    line.set_ydata(data_int)
    
    try: 
        fig.canvas.draw()
        fig.canvas.flush_events()
        
    except:
        print("Error")
        break

#ax.plot(data_int, '-')
#plt.show()


















