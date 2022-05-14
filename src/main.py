
# pip install pygame

# imports

import sys
import math
import random
import pygame
from parts.partHandler import PartHandler
from parts.part import Part

# setup

pygame.init()
pygame.display.set_caption('PygameTemplate')

# variables

win = pygame.display.set_mode((1280, 720))
width, height = pygame.display.get_window_size()
fpsClock = pygame.time.Clock()

# loop

s = pygame.Surface((width, height))
s.set_alpha(10)
s.fill((0, 255, 0))

# parts

partHandler = PartHandler([])

while True:
  pygame.display.set_caption(f'parts: {len(partHandler.parts)}')
  
  # clear

  win.blit(s, (0, 0))

  # handle events

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  # parts

  partHandler.tick()
  partHandler.draw(win)

  # flip

  pygame.display.flip()
  fpsClock.tick(60)