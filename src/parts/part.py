
import math
import pygame

class Part:

  def __init__(self):
    self.dead = False

  def die(self):
    self.dead = True

  def tick(self):
    pass

  def draw(self, win):
    pass
