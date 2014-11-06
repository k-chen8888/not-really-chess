import pygame, sys
from pygame.locals import *


# Backgrounds
#from backgrounds import game_board as gb
from backgrounds import board_builder as bb
from backgrounds import draw_tool

# Sprites
from sprites import generate_clan as gc

# Gameplay
from play_game import game_loop as gl

# Combat system
from combat import action_queue as aq

# Player info
from player import profile as p


if __name__ == "__main__":
	
	pygame.init()
	fpsClock = pygame.time.Clock()
	
	windowSurfaceObj = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
	pygame.display.set_caption('Not Really Chess')
	
	gl.play_nrc(windowSurfaceObj, fpsClock)
