import pygame
from sprites import *
from config import *
import sys

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HECIGHT))