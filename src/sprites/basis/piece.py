"""
All actions use up one stack/queue space
"""
action_bindings = [
	'q', # Use normal attack
	'w', # Use strong attack
	'e', # Use special attack, only available after 1/3 of all allied pieces dead and on certain units
	'a', # Move, click to determine coordinates
	's', # Drop flag
	'd'  # Special action for king, only available after 2/3 of all allied pieces dead (not including dropped pieces)
]


"""
A piece class
Basis for all combat pieces on the board
Piece consists of:
	Position: (xcoord, ycoord)
	Level: 0-2
	Stats: A dictionary of all stats for the piece
	Sprite: Location of sprite in folder
	Actions: Function pointers that define a piece's unique abilities
"""
class Piece(dict):
	def __init__(self, xcoord, ycoord, level, stats, sprite):
		self.level = level
		self.stats = stats
		self.sprite = sprite
		self.position = [xcoord, ycoord]
		
		"""
		Dictionary of actions
		Actions are added based on clan
		Bind actions using action_bindings list
		"""
		self.actions = {}


"""
Object created by flag drop
Flag consists of:	
	Position: (xcoord, ycoord)
	Stats: A dictionary of all stats for the piece
	Sprite: Location of sprite in folder
"""
class Flag(object):
	def __init__(self, xcoord, ycoord, stats, sprite):
		self.sprite = sprite
		self.stats = stats
		self.position = [xcoord, ycoord]
