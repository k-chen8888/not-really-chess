"""
Represents the player
Players are composed of:
	ID: Unique identifier for player. Load from db
	Queue: Action queue; cannot be modified except by current player
	Game Master Abilities: Up to 3 special abilities that a player picks before a game
	Pieces: A list of pieces that the player has available
	Kills: A dictionary of lists of opponent's pieces that player has killed
"""
class Player(object):
	def __init__(self, player_id):
		self.player_id = player_id
		self.queue = ActionQueue()
		
		"""
		Set of abilities that the player is allowed to put on the stack
		Player selects these before game begins

		This dictionary also contains local variables needed to monitor cooldowns, etc. for these abilities
		"""
		self.gm_abilities = {}
		
		"""
		List of pieces that the player still has alive
		Dead pieces are marked but not removed
		"""
		self.pieces = []
		
		"""
		Dictionary of lists of pieces that player has killed
		Indexed by opponent's player_id
		"""
		self.kills = {}


"""
Return player's pieces to starting positions instantaneously
Recall rules:
	Recalling uses up one space on the stack/queue
	Only affects pieces still alive
	Cooldown: 20 move actions
"""
def recall():
	pass


"""
Drops a piece defeated by a player on the board to serve the player
Drop rules:
	Dropping uses up one space on the stack/queue
	A piece can only be dropped if it exists in the player's kills list
	Dropped piece has 25% reduced stats and cannot level up
	Pieces may only be dropped in spaces adjacent to flags
	The same piece may not be re-dropped after it dies
	Cooldown: 20 turns at each flag
"""
def drop(xcoord, ycoord):
	pass


"""
Revive a piece with half health
Revive rules:
	Revival uses up one space on the stack/queue
	A revived piece reappears in a random empty space close to death area but on side of player's base camp
		   XR
		  XXRR
		 XXXRRR
		XXXDRRRR
		 XXXRRR
		  XXRR
		   XR
	A revived piece is removed from the opponent's kills list
	Revived piece continues play as if it did not die (can level up, etc.)
	Cooldown: 4 piece deaths
		Game starts with this spell on cooldown
"""
def revive(piece):
	pass

"""
Protects a piece for one turn
Barrier rules:
	Does not use a space on the stack/queue
	Protects against 50% of calculated damage
		Keeps piece at 1HP if that attack would kill the piece
	Cooldown: 15 attack actions
"""
def barrier(piece):
	pass

"""
Heals all pieces on board
Heal rules:
	Does not use a space on the stack/queue
	Heals 25% of missing health
	Cooldown: 100 damage taken
"""
def heal():
	pass


"""
Takes 4 pieces and teleports them to a banner
Rally rules:
	Recall must be useable or not present as a command
		Sets the cooldown for recall on use
	Cooldown: 20 move actions
"""
def rally(pieces):
	pass
