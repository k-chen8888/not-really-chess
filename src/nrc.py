import pygame, sys
from pygame.locals import *

from backgrounds import game_board as gb
from backgrounds import board_builder as bb
from sprites import generate_clan as gc
from combat import action_queue as aq
from player import profile as p


mousex, mousey = 0, 0
fieldx, fieldy = 0, 0


# Events within game
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
		
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))


if __name__ == "__main__":
	
	pygame.init()
	fpsClock = pygame.time.Clock()
	
	whiteColor = pygame.Color(255, 255, 255)
	
	windowSurfaceObj = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('Not Really Chess')
	
	while True:
		
		windowSurfaceObj.fill(whiteColor)
		
		# Event handler
		event_handler()
		
		pygame.display.update()
		fpsClock.tick(30)
