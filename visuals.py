import pygame

print("Hey there, in visuals py")

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
    
def main_game():
    x = (display_width*0.45)
    y = (display_height*0.8)
    y_change = 0
    
    gameExit = False
    
    while not gameExit:
        # EVENT HANDLING
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5 
                elif event.key == pygame.K_DOWN:
                    y_change = 5 

            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0  
          
        y += y_change

        gameDisplay.fill(white)
        
        balloon(x, y)
        
        pygame.display.update()
        clock.tick(60)
        
main_game()
pygame.quit()
quit()
        
    
    
    
    
    
    
    
    
    
    
    
    
