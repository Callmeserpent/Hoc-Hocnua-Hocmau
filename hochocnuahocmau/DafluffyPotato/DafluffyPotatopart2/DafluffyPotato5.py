# This script only works in Pygame 2
# Press E for the "explosion"

#set up python----------------------------------------------------------------------------------------f
import pygame, sys, time, os, random, math

#setup pygame-----------------------------------------------------------------------------------------f
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('DafluffyPotato Course15 Part2')
screen = pygame.display.set_mode((500, 500), 0, 32)
display = pygame.Surface((250, 250))

permanent_surf = pygame.Surface(display.get_size())
permanent_surf.set_colorkey((0, 0, 0))
temp_surf = pygame.Surface(display.get_size())
circles = []
explosions = []

def inverted(img):
  inv = pygame.Surface(img.get_rect().size, pygame.SRCALPHA)
  inv.fill((255, 255, 255, 255))
  inv.blit(img, (0, 0), None, BLEND_RGB_SUB)
  return inv

#variables----------------------------------------------------------------------------------------------f 
show_outline = False

#main loop--------------------------------------------------------------------------------------------f
while True:
  
  #background------------------------------------------------------------------------------------------f
  display.fill((255, 255, 255))
  if show_outline:
    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(0, 0, 250, 250), 1)

  #mouse-------------------------------------------------------------------------------------------------f
  mx, my = pygame.mouse.get_pos()
  mx = int(mx/2)
  my = int(my/2)

  #render------------------------------------------------------------------------------------------------f
  temp_surf.fill((0, 0, 0))
  r_list = []
  circles.append([mx, my, 16]) #x, y, radius
  n = 0
  for circle in circles:
    pygame.draw.circle(temp_surf, (255, 255, 255), (int(circle[0]), int(circle[1])), int(circle[2]))
    circle[2] -= 2
    if circle[2] <= 5:
      r_list.append(n)
    n += 1
  r_list.sort(reverse = True)
  for circle in r_list:
    circles.pop(circle)  

  r_list = []
  n = 0
  for explosion in explosions:
    explosion[1] += math.cos(math.radians(explosion[0])) * 2.5
    explosion[2] += math.sin(math.radians(explosion[0])) * 2.5
    pygame.draw.circle(permanent_surf, (255, 255, 255), (explosion[1], explosion[2]), explosion[3])
    explosion[3] -= 0.25
    if explosion[3] <= 3.5:
      r_list.append(n)
    n += 1   
    r_list.sort(reverse = True)
  for explosion in r_list:
    explosions.pop(explosion)

  temp_surf.blit(permanent_surf, (0, 0))  
  if show_outline:
    inverted_surf = inverted(temp_surf)
    inverted_surf.set_colorkey((255, 255, 255))
    display.blit(inverted_surf, (0, 1))
    display.blit(inverted_surf, (1, 0))
    display.blit(inverted_surf, (0, -1))
    display.blit(inverted_surf, (-1, 0))
    temp_surf.set_colorkey((0, 0, 0))
  else:
    temp_surf.set_colorkey()
  display.blit(temp_surf, (0, 0))
  if not show_outline:
    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(0, 0, 250, 250), 1)

  #buttons-----------------------------------------------------------------------------------------------f
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
       pygame.quit()
       sys.exit()
      if event.key == pygame.K_e:
        for i in range(random.randint(4, 5)):
          explosions.append([random.randint(0, 360), mx, my, random.randint(7, 10)])
      if event.key == pygame.K_q:
        show_outline = not show_outline

  #updates-----------------------------------------------------------------------------------------------f
  screen.blit(pygame.transform.scale(display, (500, 500)), (0, 0))
  clock.tick(60)
  pygame.display.update()     
        

