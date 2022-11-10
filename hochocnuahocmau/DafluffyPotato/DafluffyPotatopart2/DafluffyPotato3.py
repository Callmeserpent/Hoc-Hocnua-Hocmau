#set up python --------------------------------------------------------------------f
import pygame, sys, math
#set up pygame, window--------------------------------------------------------------f
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('DafluffyPotato Course')
screen = pygame.display.set_mode((500, 500), 0, 32)

arrow_img = pygame.image.load(r'C:\Users\DELL\vscodeproject\hochocnuahocmau\DafluffyPotato\DafluffyPotatopart1\data\images\jumper.png')

arrow_spin = 0

#loop--------------------------------------------------------------------------------f
while True:
  
  #background------------------------------------------------------------------------f
  screen.fill((0, 0, 0))

  arrow_spin += 1

  for i in range(4):
      arrow_coppy = arrow_img.copy()
      if i == 0:
        arrow_coppy = pygame.transform.flip(arrow_coppy, True, False)     #flip
      if i == 1:
        arrow_coppy = pygame.transform.scale(arrow_coppy, (80, 10))       #scale
      if i == 2:
        arrow_coppy = pygame.transform.rotate(arrow_coppy, arrow_spin)    #rotate
      
      screen.blit(arrow_coppy, (50 + i * 120, 200))
      if i == 3:
                            #math geometry for movement:
                            #movement_x = math.cos(arrow_angle) * speed     
                            #movement_y = math.sin(arrow_angle) * speed
                            #arrow_x += movement_x
                            #arrow_y += movement_y
       pass

  #Buttons-------------------------------------------------------------------------f
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
 
  #Updates---------------------------------------------------------------------------f
  clock.tick(60)
  pygame.display.update()    