import pygame, sys
from pygame.locals import *

from backgrounds import game_board as gb
from sprites import generate_clan as gc
from combat import action_queue as aq
from player import profile as p


mousex, mousey = 0, 0
fieldx, fieldy = 0, 0


# Parses a document for background info
def get_field_info(infile):
	f = open(infile)
	
	bg_imgs = {}
	bg_imgs['tile_imgs'] = []
	
	for line in f:
		if 'Dimensions: ' in line:
			# Pull map dimensions out of the file
			temp = [int(s) for s in str.split() if s.isdigit()]
			
			# Minimum map size is 200 by 200
			fieldx = temp[0] if temp[0] > 200 else 200
			fieldy = temp[1] if temp[1] > 200 else 200
		
		elif 'World: ' in line:
			bg_imgs['world_img'] = s for s in str.split() if '.png' in s
		
		elif 'Tile: ' in line:
			# Pull tile coordinates out of the file
			temp = [int(s) for s in str.split() if s.isdigit()]
			
			# Pull tile background image out of the file	
			bg_imgs['tile_imgs'].append([[temp[0], temp[1]], s for s in str.split() if '.png' in s])
		else:
			# All other types of lines are comments
			pass
	
	f.close()
	
	return bg_imgs


# Processes bg_imgs dictionary
def load_bg(bg_imgs):
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
