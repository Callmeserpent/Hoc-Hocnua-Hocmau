import pygame, sys

mainclock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Physics Explanation')

player = pygame.Rect(220, 270, 40, 80)
tiles = [pygame.Rect(200, 350, 50, 50), pygame.Rect(260, 320, 50, 50)]

def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
      if rect.colliderect(tile):
          collisions.append(tile)
    return collisions

def move(rect, movement, tiles):   #movementum = [5,2]
    rect.x += movement[0]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left = tile.right
    rect.y += movement[1]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom  
    return rect

right = False
left = False                  
up = False
down = False

while True:

    screen.fill((0, 0, 0))
    
    movement = [0, 0]
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -= 5    
    if up == True:
        movement[1] -= 5
    if down == True:
        movement[1] += 5    
    pygame.draw.rect(screen, (255, 255, 255), player)
    for tile in tiles:
     pygame.draw.rect(screen, (255, 0, 0), tile)

    player = move(player, movement, tiles)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                right = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False

    pygame.display.update()          
    mainclock.tick(60) 