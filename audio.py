import pyaudio
import struct #converts strings of bytes to something readable
import numpy as np
import matplotlib.pyplot as plt
import pygame

print("Hey")

#%matplotlib tk

def main():
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
    
    x = (display_width*0.5)
    y = (display_height*0.5)
    y_change = 0 
    
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
    

    

        #print("----------")
        data = stream.read(CHUNK)
        #print(data)
        data_int = np.array(struct.unpack(str(2 * CHUNK)+ 'B', data), dtype='b')[::2] + 128
        
        if 255 in data_int:
            y_change = -5
        else:
            y_change = 5
                
        y += y_change
        
        gameDisplay.fill(white)
        
        balloon(x, y)
        
        
        
        pygame.display.update()
        clock.tick(60)
        
        y_change = 0

pygame.init()

pygame.display.set_caption("Balloon")

display_width = 600
display_height = 800

# Colour definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode(
    (display_width, display_height))
    
clock = pygame.time.Clock()

balloonImg = pygame.image.load("balloonImg.png")
balloon_width = 49
balloon_height = 103

def balloon(x, y):
    gameDisplay.blit(balloonImg, (x, y))

main()       
pygame.quit()
quit()















