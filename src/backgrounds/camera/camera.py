import pygame
from pygame.locals import *


"""
Cameras always start in the upper left corner
Camera range is screen size
"""
class Camera(object):
	def __init__(self, startx, starty, boarddims, cameradims):
		# Location of top left corner of camera screen
		self.toplx = startx
		self.toply = starty
		
		# Size of game board
		self.board = boarddims
		
		# Camera dimension is screen size
		self.lens = cameradims
	
	
	"""
	Move the camera by offset
	"""
	def move(self, incx, incy):
		# Set upper left x coordinate
		# Move back if it exceeds board bounds
		self.toplx += incx
		if self.toplx < 0:
			self.toplx = 0
		elif self.toplx + self.lens[0] > self.board[0]:
			self.toplx = self.board[0] - self.lens[0]
		
		# Set upper left y coordinate
		# Move back if it exceeds board bounds
		self.toply += incy
		if self.toplx < 0:
			self.toplx = 0
		elif self.toplx + self.lens[i0] > self.board[0]:
			self.toplx = self.board[0] - self.lens[0]
		
		# Update camera lens
		self.update()
	
	
	"""
	Update the camera screen on move
	"""
	def update():
		pass
