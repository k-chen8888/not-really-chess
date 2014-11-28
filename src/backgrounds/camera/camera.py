import pygame
from pygame.locals import *

# Import constants from parent directory
import sys
sys.path.append('../')
from constants import * 


"""
Cameras always start in the upper left corner
Camera range is screen size
"""
class Camera(object):
	def __init__(self, start, boarddims):
		# Location of top left corner of camera screen
		self.toplx = start[0]
		self.toply = start[1]
		
		# Size of game board
		self.board = boarddims
		
		# Camera dimension is screen size
		self.lens = SCREEN_DIMS
	
	
	"""
	Move the camera by offset

	Default is move by 0
	"""
	def move_corner(self, incx = 0, incy = 0):
		# Set upper left x coordinate
		# Move back if it exceeds board bounds, padding with some blank space
		self.toplx += incx
		if self.toplx < 0:
			self.toplx = 0
		elif self.toplx + self.lens[0] > self.board[0]:
			self.toplx = self.board[0] + OCT_0 - self.lens[0]
		print "x: " + str(self.toplx)
		
		# Set upper left y coordinate
		# Move back if it exceeds board bounds, padding with some blank space
		self.toply += incy
		if self.toply < 0:
			self.toply = 0
		elif self.toply + self.lens[1] > self.board[1]:
			self.toply = self.board[1] + OCT_0 - self.lens[1]
		print "y: " + str(self.toply)
