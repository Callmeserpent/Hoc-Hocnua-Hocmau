# Supply you own "img.png" to test outlines with. 40x40 or less is recommended.
# press A to switch the outlining method
# press S to show/hide the image
# the part that activates the Pygame 2 method has been commented out. feel free to add it back in

#setup python--------------------------------------------------------------------------------------------f
import pygame, sys, time

#setup pygame--------------------------------------------------------------------------------------------f
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('DafluffyPotato Course15 Part1')
screen = pygame.display.set_mode((500, 300), 0, 32)
display = pygame.Surface((250, 150))

test_img = pygame.image.load(r'C:\Users\DELL\vscodeproject\hochocnuahocmau\DafluffyPotato\DafluffyPotatopart2\pacman.png').convert()
test_img.set_colorkey((0, 0, 0))
#text_img = pygame.image.load('text.png').convert()
#text_img.set_colorkey((0, 0, 0))

#method 1st: using mask_outline = mask.outline()-------------------------------------------------------f
def outline_mask(img, loc):
  mask = pygame.mask.from_surface(img)
  mask_outline = mask.outline()
  n = 0
  for point in mask_outline:
    mask_outline[n] = (point[0] + loc[0], point[1] + loc[1])
    n += 1
  pygame.draw.polygon(display, (255, 255, 255), mask_outline, 3)

#method 2nd: using mask_surface = mask.to_surface()----------------------------------------------------f  
def perfect_outline(img, loc):
  mask = pygame.mask.from_surface(img)
  mask_surf = mask.to_surface()
  mask_surf.set_colorkey((0, 0, 0))
  display.blit(mask_surf, (loc[0] - 1, loc[1]))
  display.blit(mask_surf, (loc[0] + 1, loc[1]))
  display.blit(mask_surf, (loc[0], loc[1] - 1))
  display.blit(mask_surf, (loc[0], loc[1] + 1))

#method 3rd: combine 2 methods above-------------------------------------------------------------------f
def perfect_outline_2(img, loc):
  mask = pygame.mask.from_surface(img)
  mask_outline = mask.outline()
  mask_surf = pygame.Surface(img.get_size())
  for pixel in mask_outline:
    mask_surf.set_at(pixel, (255, 255, 255))
  mask_surf.set_colorkey((0, 0, 0))
  display.blit(mask_surf, (loc[0] - 1, loc[1]))
  display.blit(mask_surf, (loc[0] + 1, loc[1]))
  display.blit(mask_surf, (loc[0], loc[1] - 1))
  display.blit(mask_surf, (loc[0], loc[1] + 1))

#variables----------------------------------------------------------------------------------------------f
show = False
mode = 0

#main loop-----------------------------------------------------------------------------------------------f
while True:
  #background--------------------------------------------------------------------------------------------f
  display.fill((0, 0, 0))
  pygame.draw.rect(display, (255, 255, 255), pygame.Rect(0, 0, 250, 150), 1)
  #display.blit(text_img, (10, 70))
  
  #method choose:
  if mode == 0:
    outline_mask(test_img, (10, 10))
  elif mode == 1:
    perfect_outline(test_img, (100,10))
  else:
    perfect_outline_2(test_img, (190, 10))

  #show 3 images:
  if show:
    display.blit(test_img, (10, 10))
    display.blit(test_img, (100, 10))
    display.blit(test_img, (190, 10))

  #buttons-----------------------------------------------------------------------------------------------f
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
      if event.key == pygame.K_s:
        show = not show
      if event.key == pygame.K_a:
        mode += 1
        if mode > 2:
          mode = 0

  #updates----------------------------------------------------------------------------------------------f
  screen.blit(pygame.transform.scale(display, (500, 300)), (0, 0))
  clock.tick(60)
  pygame.display.update()      