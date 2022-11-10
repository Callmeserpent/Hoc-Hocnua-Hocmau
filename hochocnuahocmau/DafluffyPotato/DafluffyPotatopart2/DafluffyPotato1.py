import pygame, sys

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('DafluffyPotato Course12')
screen= pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
  textobj = font.render(text, 1, color)
  textrect = textobj.get_rect()
  textrect.topleft = (x, y)
  surface.blit(textobj, textrect)

click = False

def main_menu(): 

  while True:
  
    screen.fill((0, 0, 0))
    draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
  
    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(50, 100, 200, 50)
    button_2 = pygame.Rect(50, 200, 200, 50)
    if button_1.collidepoint(mx, my):
      if click:
        game()      
    if button_2.collidepoint(mx, my):
      if click:
        option()
    pygame.draw.rect(screen, (255, 0, 0), button_1)
    pygame.draw.rect(screen, (255, 0, 0), button_2)
  
    click = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          click = True
  
    clock.tick(60)
    pygame.display.update()

def game():
  running = True
  while running:
    screen.fill((0, 0, 0))
    
    draw_text('game', font, (255, 255, 255), screen, 20, 20)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
    
    clock.tick(60)
    pygame.display.update()    

def option():
  running = True
  while running:
    screen.fill((0, 0, 0))
    
    draw_text('option', font, (255, 255, 255), screen, 20, 20)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
    
    clock.tick(60)
    pygame.display.update()    

main_menu()