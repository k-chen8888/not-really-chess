"""
Tile on the board
Tiles have elevation and can contain a single piece
Stores a pre-loaded background image
"""
class Tile(object):
	def __init__(self, elev, bg, coords):
		self.centerx = coords[0]
		self.centery = coords[1]
		self.elev = elev
		self.bg = bg

'''
Pieces traverse octagonal tiles
'''
class OctTile(Tile):
	def __init__(self, elev, bg, coords):
		Tile.__init__(self, elev, bg, coords)
		self.has_piece = False

'''
Flags are placed on square tiles
'''
class SqTile(Tile):
	def __init__(self, elev, bg, coords):
		Tile.__init__(self, elev, bg, coords)
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
		
		# Generate the board
		self.tiles = []
		for i in range(0, self.length):
			tiles.append([])
			
			for j in range(0, self.width):
				# Octagons in even tiles on even rows
				if j % 2 == 0 and i % 2 == 0:
					tiles[i].append(OctTile(0, (i*128+64, j*128+64))
				# Squares in odd tiles on even rows
				elif j % 2 == 1 and i % 2 == 0:
					tiles[i].append(SqTile(0, None))
				# Squares in even tiles on odd rows
				elif j % 2 == 0 and i % 2 == 1:
					tiles[i].append(SqTile(0, None))
				# Octagons in odd tiles on odd rows
				else:
					tiles[i].append(OctTile(0, None))
		
		for sp_tile in bg_dict['tile_imgs']:
			# Update the special tiles' images by looking them up by coordinates
			tilex = sp_tile[0][0]
			tiley = sp_tile[0][1]
			
			# Load tiles, prepare for blitting
			tiles[tilex][tiley] = pygame.image.load(sp_tile[1]).convert_alpha()
		
		# Generate something to draw the board on
		self.board_surface = pygame.Surface((self.width * 128, self.length * 128))
		
		# Draw the board onto the surface
		for i in range(0, self.length):
			for j in range(0, self.width):
				if self.tiles[i][j].bg != None:
					self.board_surface.blit(self.tiles[i][j], (i * 32 + 16, j * 32 + 16))
