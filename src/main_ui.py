import pygame, sys
from pygame.locals import *

# Game local files
from backgrounds import *
from combat import *
from player import *
from sprites import *
from sprites.basis import *


pygame.init()

# Prepare display
DISPLAYSURF = pygame.display.set_mode()
pygame.display.set_caption("Not Really Chess")

# Prepare player information


# Main game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	pygame.display.update()
