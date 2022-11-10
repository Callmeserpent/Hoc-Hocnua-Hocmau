import pygame

#initialize pygame
pygame.init()

#window(size:500x500)
screen = pygame.display.set_mode((1000, 500))
#screen caption
pygame.display.set_caption("Tech With Tim Course 1")

walkRight = [pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R1.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R2.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R3.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R4.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R5.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R6.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R7.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R8.png'),
 pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/R9.png')]
walkLeft = [pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L1.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L2.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L3.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L4.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L5.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L6.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L7.png'), pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L8.png'), 
pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/L9.png')]
bg = pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/background/winter.jpg')
char = pygame.image.load(r'C:/Users/DELL/OneDrive/Hình ảnh/Pixel art/character/char/standing.png')
#variables
#position
clock = pygame.time.Clock()
x =50
y = 380
#size
width = 64
height = 64
#speed(for movement)
velocity = 7  

isJump = False
jumpCount = 11

left = False
right = False
walkcount = 0

def redrawGameWindow():
    global walkcount
 #rectangle move => fill its path with Black color(0, 0, 0) as window color
    screen.blit(bg, (0, 0))

    if walkcount + 1 >= 27:
        walkcount = 0
    
    if left:
        screen.blit(walkLeft[walkcount//3], (x, y))
        walkcount += 1
    elif right:
        screen.blit(walkRight[walkcount//3], (x, y))
        walkcount += 1 
    else:
        screen.blit(char, (x, y))       
    
    pygame.display.update()      #update window

#game main loop
running = True
while running:
   
   #time in game
   clock.tick(27) #time goes by 27 fps
   
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 #keys function for movemnent 
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT] and x > velocity: #prevent x<0
       x -= velocity
       left = True
       right = False
   elif keys[pygame.K_RIGHT] and x < 1000 - 40 - velocity: #prevent x>screen width
       x += velocity
       right = True
       left = False
   else:
       right = False
       left = False
       walkcount = 0   
   if not (isJump):   
       if keys[pygame.K_SPACE]:
          isJump = True
          right = False
          left = False
          walkcount = 0
   else:
       if jumpCount >= -11:
         neg = 1         
         if jumpCount < 0:
           neg = -1
         y -= (jumpCount ** 2) * 0.5 * neg
         jumpCount -= 1
       else:
          isJump = False 
          jumpCount = 11

   redrawGameWindow()

pygame.quit()
