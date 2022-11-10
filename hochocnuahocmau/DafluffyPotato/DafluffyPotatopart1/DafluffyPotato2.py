import pygame, sys # import pygame and sys
 
clock = pygame.time.Clock() # set up the clock
 
from pygame.locals import * # import pygame modules
pygame.init() # initiate pygame
 
pygame.display.set_caption('DafluffyPotato Course1') # set the window name


WINDOW_SIZE = (600,400) # set up window size
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) # initiate screen


#load images
player_img = pygame.image.load(r'C:/Users/DELL/vscodeproject/hochocnuahocmau/DafluffyPotato/player.png')
player_img.set_colorkey((255, 255, 255))

moving_right = False
moving_left = False

player_location = [50,50]
player_y_momentum = 0   

player_rect = pygame.Rect(player_location[0], player_location[1], 
player_img.get_width(), player_img.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)
#game main loop
while True:
    #draw:
    screen.fill((146, 244, 255))  
   
    screen.blit(player_img,player_location) # render player
    
     # bouncy stoff
    if player_location[1] > WINDOW_SIZE[1]-player_img.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    
    # movement
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
 
    player_rect.x = player_location[0] # update rect x
    player_rect.y = player_location[1] # update rect y
 
    # test rect for collisions
    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen,(255,0,0),test_rect)
    else:
        pygame.draw.rect(screen,(0,0,0),test_rect)
    
    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
 
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps