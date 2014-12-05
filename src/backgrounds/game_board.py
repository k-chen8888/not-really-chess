import pygame
from pygame.locals import *

# Import constants from parent directory
import sys
sys.path.append('../')
from constants import * 

# Import camera tool
from camera import camera as c


"""
Tile on the board
Tiles have elevation and can contain a single piece
Stores a pre-loaded background image
	In addition, draw assets on screen in tile
"""
class Tile(object):
	def __init__(self, elev, bg):
		self.elev = elev
		self.bg = bg


'''
Pieces traverse octagonal tiles
'''
class OctTile(Tile):
	def __init__(self, elev, bg):
		Tile.__init__(self, elev, bg)
		self.has_piece = False


'''
Flags are placed on square tiles
'''
class SqTile(Tile):
	def __init__(self, elev, bg):
		Tile.__init__(self, elev, bg)
		self.has_flag = False


'''
Take a dictionary of board elements
	'world_img' is the background for the entire board
	'tile_imgs' contains images for separate tiles
		Not all tiles have their own images
'''
class Board(object):
	def __init__(self, bg_dict):
		# Boards must have even dimensions (check outside of __init__)
		self.width = bg_dict['board_dim'][0]
		self.height = bg_dict['board_dim'][1]
		
		# Camera for calculating offsets
		self.cam = c.Camera([0, 0], [self.width * TILE_DIMS, self.height * TILE_DIMS])
		
		# Generate something to draw the board on
		self.board_surface = pygame.Surface((self.width * TILE_DIMS, self.height * TILE_DIMS))

		# Generate the board
		# self.height = # of OctTile rows = # SqTile rows - 1
		# self.width = # of OctTiles per row = # SqTiles per row - 1
		# Coordinates calculated based on camera offset and array index
		self.tiles = {}
		
		self.tiles['oct_tiles'] = []
		for i in range(0, self.height):
			self.tiles['oct_tiles'].append([])
			
			# Add OctTile tiles to list
			for j in range(0, self.width):
				self.tiles['oct_tiles'].append(OctTile(0, None))
		
		self.tiles['sq_tiles'] = []
		for i in range(0, self.height + 1):
			self.tiles['sq_tiles'].append([])
			
			# Add SqTile tiles to list
			for j in range(0, self.width + 1):
				self.tiles['sq_tiles'].append(SqTile(0, None))
		
		for sp_tile in bg_dict['tile_imgs']:
			# Update the special tiles' images by looking them up by coordinates
			tilex = sp_tile[0][0]
			tiley = sp_tile[0][1]
			
			# Load tiles, prepare for blitting
			tiles[tilex][tiley] = pygame.image.load(sp_tile[1]).convert_alpha()
		
		
	'''
	Changes the coordinates of the upper left corner

	Default is move by 0
	'''
	def move(self, incx = 0, incy = 0):
		self.cam.move_corner(incx, incy)
	
	'''
	Draws images onto a board
	Accounts for offset using the array indices of the tiles
	'''
	def draw_board(self):
		# Draw the board onto the surface
		for j in range(0, self.height):
			for i in range(0, self.width):
				if self.tiles[i][j].bg != None:
					# If images fall back by an offset, it will appear as if the board has moved
					coords = (i * 32 + 16 - self.cam.toplx, j * 32 + 16 - self.cam.toply)
					
					if not coords[0] < 0 and not coords[1] < 0:
						self.board_surface.blit(self.tiles[i][j], coords)
	
	'''
	Draws an octagonal grid on a surface
	
			(i+OCT_0, j)				(i+OCT_1, j)
	
	(i, j+OCT_0)								(i+TILE_DIMS, j+OCT_0)
	
	
	(i, j+OCT_1)								(i+TILE_DIMS, j+OCT_1)
	
		 	(i+OCT_0, j+TILE_DIMS)		(i+OCT_1, j+TILE_DIMS)
	
	Squares will appear as a consequence of the drawing
	Input the coordinates clockwise starting from (i+OCT_0, j)
	'''
	def draw_grid(self):
		j = 0
		w_off = 0
		h_off = 0
		
		# Remove the fill with white once there is proper testing
		self.board_surface.fill(pygame.Color(255, 255, 255))
		
		# Octagons on every row
		for j in range(0, self.height):
			h_off = j*TILE_DIMS - self.cam.toply
			
			for i in range(0, self.width):
				w_off = i*TILE_DIMS - self.cam.toplx
				
				pygame.draw.polygon(self.board_surface, pygame.Color(0, 0, 0), ( (w_off+OCT_0, h_off), (w_off+OCT_1, h_off), (w_off+TILE_DIMS, h_off+OCT_0), (w_off+TILE_DIMS, h_off+OCT_1), (w_off+OCT_1, h_off+TILE_DIMS), (w_off+OCT_0, h_off+TILE_DIMS), (w_off, h_off+OCT_1), (w_off, h_off+OCT_0) ), 1)
