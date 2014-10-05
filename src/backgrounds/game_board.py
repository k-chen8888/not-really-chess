"""
Tile on the board
Tiles have elevation and can contain a single piece
Stores a pre-loaded background image
"""
class Tile(object):
	def __init__(self, elev, bg):
		self.elev = elev
		self.bg = bg

class OctTile(Tile):
	def __init__(self, elev, bg):
		Tile.__init__(self, elev, bg)
		self.has_piece = False

class SqTile(Tile):
	def __init(self, elev, bg):
		Tile.__init__(self, elev, bg)
		self.has_flag = False

class Board(object):
	def __init__(self, dim, elev_table, bg_table):
		# Boards must have even dimensions; check elsewhere
		self.length = dim[0]
		self.width = dim[1]
		
		# Generate the board
		self.tiles = []
		for i in range(0, self.length):
			tiles.append([])

			for j in range(0, self.width):
				# Octagons in even tiles on even rows
				if j % 2 == 0 and i % 2 == 0:
					tiles[i].append(OctTile(elev_table[i][j], bg_table[i][j]))
				# Squares in odd tiles on even rows
				elif j % 2 == 1 and i % 2 == 0:
					tiles[i].append(SqTile(elev_table[i][j], bg_table[i][j]))
				# Squares in even tiles on odd rows
				elif j % 2 == 0 and i % 2 == 1:
					tiles[i].append(SqTile(elev_table[i][j], bg_table[i][j]))
				# Octagons in odd tiles on odd rows
				else:
					tiles[i].append(OctTile(elev_table[i][j], bg_table[i][j]))
		
		# Generate something to draw the board on
		self.board_surface = pygame.Surface((self.width * 32, self.length * 32))
		
		# Draw the board onto the surface
		for i in range(0, self.length):
			for j in range(0, self.width):
				self.board_surface.blit(self.tiles[i][j], (i * 32 + 16, j * 32 + 16))
