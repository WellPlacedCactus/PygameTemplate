
import pygame
from parts.part import Part

class PartHandler:

  def __init__(self, parts):
    self.parts = parts
    self.width, self.height = pygame.display.get_window_size()

  def add(self, p):
    if isinstance(p, Part):
      self.parts.append(p)

  def tick(self):
    for p in reversed(self.parts):
      p.tick()
      if p.dead or p.x < 0 or p.y < 0 or p.x > self.width or p.y > self.height:
        self.parts.remove(p)

  def draw(self, win):
    for p in reversed(self.parts):
      p.draw(win)