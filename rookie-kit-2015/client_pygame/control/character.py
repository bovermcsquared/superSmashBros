import pygame
import random
from spritesheet import Spritesheet


class Character:
	def __init__(self, name, filename, sounds, rowLength):
		self.name = name
		self.rowL = rowLength
		


	def load_sprites(self):
		self.lines = []
		for s in self.rowL:
			rect = pygame.Rect((0,s*(SPRITE_GUTTER+LINK_SPRITE),LINK_SPRITE,LINK_SPRITE))
	        lines.append(sheet.load_irregular_strip(rect,LINK_SPRITE+SPRITE_GUTTER, LINK_STATE[s], (255,255,255)))