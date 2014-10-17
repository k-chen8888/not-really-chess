import pygame, sys
from pygame.locals import *

from backgrounds import game_board as gb
from sprites import generate_clan as gc
from combat import action_queue as aq
from player import profile as p


mousex, mousey = 0, 0

# Parses a document for tile images
def get_bg_imgs(infile):
	pass

# Takes a list of background images and loads them as surfaces
def load_bg(dim, bg_imgs):
	# 0 is world
	# 1 is board
	bg = []
	bg.append(pygame.image.load('world_bg.png').convert())
	bg.append([])
	
	for i in range(0, dim[0] - dim[0] % 2):
		bg[1].append([])

		for j in range(0, dim[1] - dim[1] % 2):
			bg[1][i].append(pygame.image.load(bg_imgs[i][j]).convert())

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
