import pygame, sys
from pygame.locals import *


# Constants
from constants import *

# Backgrounds
from backgrounds import board_builder as bb
from backgrounds import draw_tool

# Sprites
from sprites import generate_clan as gc

# Gameplay
from play_game import game_loop as gl

# Combat system
from play_game.combat import action_queue as aq

# Player info
from player import profile as p


if __name__ == "__main__":
	
	pygame.init()
	fpsClock = pygame.time.Clock()
	
	board = bb.load_bg(bb.get_field_info("backgrounds/boards/test/test_board.txt"))
	
	windowSurfaceObj = pygame.display.set_mode(SCREEN_DIMS)
	pygame.display.set_caption('Not Really Chess')
	
	gl.play_nrc(windowSurfaceObj, fpsClock, board)
