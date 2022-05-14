
import math
import pygame

class Part:

  def __init__(self, x, y, r, d, m, h, l):
    self.x = x
    self.y = y
    self.r = r
    self.d = d
    self.m = m
    self.h = h
    self.l = l
    self.t = 0
    self.dead = False

  def die(self):
    self.dead = True

  def tick(self):

    self.d += 0.05

    self.m -= 0.05
    if self.m < 0:
      self.die()

    self.x += self.m * math.cos(self.d)
    self.y += self.m * math.sin(self.d)

    width, height = pygame.display.get_window_size()
    xx = self.x - width / 2
    yy = self.y - height / 2
    if xx * xx + yy * yy > 100000:
      self.l = 50
    else:
      self.l = 0

  def draw(self, win):
    c = pygame.Color(255, 255, 255)
    c.hsla = (self.h, 100, self.l, 100)
    # s = pygame.Surface((self.r, self.r))
    # s.fill(c)
    # win.blit(s, (self.x, self.y), special_flags=pygame.BLEND_RGB_ADD)
    pygame.draw.rect(win, c, (self.x, self.y, self.r, self.r))
