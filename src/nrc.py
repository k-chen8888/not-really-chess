import pygame, sys
from pygame.locals import *


# Backgrounds
from backgrounds import game_board as gb
from backgrounds import board_builder as bb
from backgrounds import draw_tool

# Sprites
from sprites import generate_clan as gc

# Combat system
from combat import action_queue as aq

# Player info
from player import profile as p


# Gets mouse position
mousex, mousey = 0, 0
# Current position of upper left corner
cornerx, cornery = 0, 0

# Ctrl on
use_ctrl = False
# Shift on
use_shift = False


# Events while game is being played
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
		
		elif event.type == K_LCTRL or event.type == K_RCTRL:
			use_ctrl = not use_ctrl
			
		elif event.type == KEYDOWN && use_ctrl == True:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
			elif event.key == K_UP:
				cornery = cornery - 10
				if cornery < 0:
					cornery = 0
			elif event.key == K_DOWN:
				cornery = cornery + 10
				if cornery < 0:
					cornery = 0
			elif event.key == K_LEFT:
				cornerx = cornerx - 10
				if cornerx < 0:
					cornerx = 0	
			elif event.key == K_RIGHT:
				cornerx = cornerx + 10
				if cornerx < 0:
					cornerx = 0


# The actual game
def play_nrc(surface):
	while True:
		
		surface.fill(whiteColor)
		draw_tool.draw_grid(50, 50, surface)
		
		# Event handler
		event_handler()
		
		pygame.display.update()
		fpsClock.tick(60)


# The menu screen
def main_menu():
	pass


if __name__ == "__main__":
	
	pygame.init()
	fpsClock = pygame.time.Clock()
	
	whiteColor = pygame.Color(255, 255, 255)
	
	windowSurfaceObj = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
	pygame.display.set_caption('Not Really Chess')
	
	play_nrc(windowSurfaceObj)
