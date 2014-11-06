import pygame, sys
from pygame.locals import *

from backgrounds import draw_tool

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
			
			# Arrow keys, SHIFT pressed once
			elif use_shift == True:
				pass


# The actual game
def play_nrc(surface, fpsClock):
	whiteColor = pygame.Color(255, 255, 255)

	while True:
		
		surface.fill(whiteColor)
		draw_tool.draw_grid(50, 50, surface)
		
		# Event handler
		event_handler()
		
		pygame.display.update()
		fpsClock.tick(60)
