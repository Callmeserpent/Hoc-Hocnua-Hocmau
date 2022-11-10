#Dinosaur images by Arks
#http://ark.itch.io/dino-characters
#Twitter: @ScissorMarks

import pygame

#constant variables
SCREEN_size = (700,500)
DARK_grey = (50, 50, 50) #dark grey color in rbg colors
Mustard = (209, 206, 25)
x, y, vel = 300, 237, 5
clock = pygame.time.Clock()

#intialize pygame
pygame.init()

#window(size:700x500)
screen = pygame.display.set_mode(SCREEN_size)
pygame.display.set_caption("Rik Cross Course1")

#player
player_img = pygame.image.load(r'C:\Users\DELL\OneDrive\Hình ảnh\Pixel art\character\dinoCharactersVersion1.1\images\DinoSprites - doux\doux_00.png')

#platforms
platforms = [ 
   #middle
   pygame.Rect(100, 300, 400, 50),
   #left
   pygame.Rect(100, 250, 50, 50),
   #right
   pygame.Rect(450, 250, 50, 50)
]


#game loop
running = True
while running:
    clock.tick(60)
    #input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
        #if event.type == 12: (event type '12' is pygame.QUIT)
            running = False
    
    new_x = x

    #player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > 145 - vel: #prevent x<0
            new_x -= vel
    if keys[pygame.K_d] and x < 395 - vel: #prevent x>screen width
            new_x += vel   
    
    #horizontal movement:
    new_player_rect = pygame.Rect(new_x, 100, 72, 72)
    x_collision = False 
    #check again any platforms
    for p in platforms:
        if p.colliderect(new_player_rect):
            x_collision = True
            break
    if x_collision == False:
        x = new_x
    
    #update
   
    #draw
    
    
    #player move => fill its path with
    #Dark grey color(50, 50, 50) as window color
    screen.fill((DARK_grey))   
    #platforms
    for p in platforms:
        pygame.draw.rect(screen, Mustard, p)

    #load the player_image to the screen in (300,100) position
    screen.blit(player_img, (x, y))     
    pygame.display.flip()

#quit
pygame.quit()    