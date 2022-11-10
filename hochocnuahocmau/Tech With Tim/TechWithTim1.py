import pygame

#initialize pygame
pygame.init()

#window(size:500x500)
screen = pygame.display.set_mode((500, 500))
#screen caption
pygame.display.set_caption("Tech With Tim Course 1")

#variables
#position
x =50
y = 425
#size
width = 40
height = 60
#speed(for movement)
velocity = 7  

isJump = False
jumpCount = 10

#game main loop
running = True
while running:
   
   #time in game
   pygame.time.delay(60) #time goes by 60 fps
   
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 #keys function for movemnent 
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT] and x > velocity: #prevent x<0
       x -= velocity
   if keys[pygame.K_RIGHT] and x < 500 - 40 - velocity: #prevent x>screen width
       x += velocity
   if not (isJump):   
       if keys[pygame.K_UP] and y > velocity: #prevent y>screen height
          y -= velocity
       if keys[pygame.K_DOWN] and y <500 - 60 - velocity: #prevent y<0
          y += velocity
       if keys[pygame.K_SPACE]:
          isJump = True
   else:
       if jumpCount >= -10:
         neg = 1         
         if jumpCount < 0:
           neg = -1
         y -= (jumpCount ** 2) * 0.5 * neg
         jumpCount -= 1
       else:
          isJump = False 
          jumpCount = 10 
 #rectangle move => fill its path with Black color(0, 0, 0) as window color
   screen.fill((0, 0, 0))
 #draw rectangle as Red color(255, 0, 0) object with variables above 
 # on the screen 
   pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
   pygame.display.update()      #update window

pygame.quit()
