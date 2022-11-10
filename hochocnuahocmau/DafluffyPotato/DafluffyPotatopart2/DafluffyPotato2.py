#set up python--------------------------------------------------------------------------f
import pygame, sys

#set up pygame--------------------------------------------------------------------------f
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('DafluffyPotato Course13')
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

#variables-------------------------------------------------------------------------------f
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
fullscreen = False

#loop-------------------------------------------------------------------------------------f
while True:
    #screen---------------------------------------------------------------------------------f
    screen.fill((0, 0, 50))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() - 5 - (screen.get_width() / 5), 50, screen.get_width() / 5, 50))
    
    #buttons---------------------------------------------------------------------------------f
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      if event.type == VIDEORESIZE:
          if not fullscreen:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        if event.key == pygame.K_F10:
          fullscreen = not fullscreen
          if fullscreen:
            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
          else:
            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
    
    #updates-----------------------------------------------------------------------------------f
    pygame.display.update()    
    clock.tick(60)