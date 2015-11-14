

# import pygame
# import random
# from spritesheet import Spritesheet


# class Character:
# 	def __init__(self, name, filename, sounds, rowLength):
# 		self.name = name
# 		self.rowL = rowLength
		


# 	def load_sprites(self):
# 		self.lines = []
# 		for s in self.rowL:
# 			rect = pygame.Rect((0,s*(SPRITE_GUTTER+LINK_SPRITE),LINK_SPRITE,LINK_SPRITE))
# 	        lines.append(sheet.load_irregular_strip(rect,LINK_SPRITE+SPRITE_GUTTER, LINK_STATE[s], (255,255,255)))

import pygame
import random
from display.spritesheet import *
from config import *
import os



class Character:
	def __init__(self, name, sounds, filename, rowLength):
		self.name = name
		self.rowL = rowLength
		self.spritesheet = Spritesheet(filename)
		self.load_sprites()
		print"thishas happened"
		
		


	def load_sprites(self):
		self.lines = []
		print self.rowL
		print len(self.rowL)

		# for s in range(len(self.rowL)):
		for s in range(10):
			rect = pygame.Rect((0,s*(SPRITE_GUTTER+LINK_SPRITE),LINK_SPRITE,LINK_SPRITE))
			print rect
	        self.lines.append(self.spritesheet.load_irregular_strip(rect,LINK_SPRITE+SPRITE_GUTTER, self.rowL[s], (255,255,255)))

	def find_sprite_direction(self, rot, step):
		print self.lines
		if rot >=325 or rot< 45:
			img = self.lines[0][step]
# else:
#     img = self.char[3][0]
		if rot >=45 and rot <135:
			img = self.lines[0][step]

		if rot >= 135 and rot <225:
			img = self.lines[0][step]

		if rot >= 225 and rot<325:
			img = self.lines[0][step]
		return img

	def get_row(self, row):
		print "row has been gotten"
		return self.rowL[row]

	def load_sounds(self):
		for i in self.sounds:
			i = pygame.mixer.Sound('i')





