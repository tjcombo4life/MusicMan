# Import a library of functions called 'pygame'
import os
import pygame
import random
from Draw import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 60, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
GROUND = 250 #pixel ground level

mod = 0
        
def main():
    
    pygame.init()# Initialize the game engine

    size = (700, 500)   #Window Size
    screen = pygame.display.set_mode(size)  #Window Creation
    pygame.display.set_caption("MusicRun")  #Displays Window Title

    
    done = False # Loop until the user clicks the close button.

    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    
    velocity = 4 #speed of character

    cloudX, cloudY = SCREEN_WIDTH, random.randrange(10, 100) #Starting pos of clouds
    floorX_1, floorX_2 = 0, 700 #Placement of grass running surface
    
    player = Player()   #Creation of player object
    platform1 = Platform(150, 238,"Platform_02", 26, 90)    #Creates Vine Platform Object
    platform2 = Platform(150, 114,"Platform_01", 20, 90)    #Creates Cloud Platform Object
    platform3 = Platform(150, 351,"Platform_03", 18, 90)    #Creates Stone Platform Object
    
    mod = [0] #determines how fast scenery moves

    #pygame.mixer.music.load('A Wish.ogg')   #Loads song into pygame
    #pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)     #A trigger event for when song ends
    #pygame.mixer.music.play(50) #!?!?Not a permenent solution for infinite loop!?!?    

    #jump_sound = pygame.mixer.Sound("spin_jump.wav") #Jump Sound

    floor_1 = pygame.image.load("Grass.png").convert()  #loads Grass Platform
    floor_2 = pygame.image.load("Grass.png").convert()  #loads Grass Platform

    #---Main Program Loop-------------------------------

    while not done:
        # --- Main event loop---------------------------

        for event in pygame.event.get(): # User did something
            if (event.type == pygame.QUIT): # If user clicked close
                done = True # Flag that we are done so we exit this loop

        onPlatform = [] #Carries each platforms location 
        onPlatform.append(platform1.coord())
        onPlatform.append(platform2.coord())
        onPlatform.append(platform3.coord())
        player.isPlatform(onPlatform)

        #---Updates Screen with new drawings------------
                
        screen.fill(WHITE) #Clears screen to white

        pygame.draw.rect(screen, (100,100,200), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - 150]) #Sky Backdrop
        
        screen.blit(floor_1,(floorX_1, 350))    #Draws Grass to screen
        screen.blit(floor_2,(floorX_2, 350))    #Draws Grass to screen

        platform1.draw(screen)  #Draws Vine platform
        platform2.draw(screen)  #Draws Cloud platform
        platform3.draw(screen)  #Draws Stone Platform
        
        player.draw(screen) #Draws player to screen

        #---Player's Behavior----------------------------

        player.update(mod)

        #---Platform Behavior----------------------------

        platform1.update(mod)
        platform2.update(mod)
        platform3.update(mod)
        
        #---Ground Behavior------------------------------

        floorX_1 -= 1 + mod[0]
        floorX_2 -= 1 + mod[0]

        if(floorX_1 <= -700):   #if floor platform goes out of left screen    
            floorX_1 = 700     #Returns floor platform to the right of the screen
        if(floorX_2 <= -700):
            floorX_2 = 700

        #---Handles all key down events-----------------

        player.handle_keys(mod)
    
        #---Updates the screen with what we've drawn----

        pygame.display.flip()
        
        #---Limit to 60 frames per second---------------

        clock.tick(60)

    pygame.quit()
    
main()
