import pygame, sys
from pygame.locals import *

from backgrounds import draw_tool

# Gets mouse position
mousex, mousey = 0, 0

# Ctrl on
use_ctrl = False
# Shift on
use_shift = False


# Events while game is being played
def event_handler(board):
	global use_ctrl
	global use_shift

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
			
			elif event.key == K_LCTRL or event.key == K_RCTRL:
				use_ctrl = not use_ctrl
			
			# Arrow keys, for CTRL pressed
			if use_ctrl == True:
				if event.key == K_UP:
					print "UP: 0, -32"
					board.move(0, -32)
				elif event.key == K_DOWN:
					print "DOWN: 0, 32"
					board.move(0, 32)
				elif event.key == K_LEFT:
					print "LEFT: -32, 0"
					board.move(-32, 0)
				elif event.key == K_RIGHT:
					print "RIGHT: 32, 0"
					board.move(32, 0)
			
			# Arrow keys, SHIFT pressed once
			elif use_shift == True:
				pass


# The actual game
def play_nrc(surface, fpsClock, board):
	whiteColor = pygame.Color(255, 255, 255)
	
	while True:
		
		surface.fill(whiteColor)
		#draw_tool.draw_grid(50, 50, surface)
		board.draw_grid()
		surface.blit(board.board_surface, (0, 0))
		
		# Event handler
		event_handler(board)
		
		pygame.display.update()
		fpsClock.tick(60)
