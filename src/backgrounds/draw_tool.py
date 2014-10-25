import pygame
from pygame.locals import *

'''
Draws an octagonal grid on a surface

	(i+32, j)		(i+96, j)

(i, j+32)				(i+128, j+32)


(i, j+96)				(i+128, j+96)

	(i+32, j+128)	(i+96, j+128)
'''
def draw_grid(width, height, surface):
	j = 0
	w_off = 0
	h_off = 0
	
	# Octagons on every row
	while j < height:
		h_off = j*128
		
		for i in range(0, width):
			w_off = i*128
			pygame.draw.polygon(surface, pygame.Color(0, 0, 0), ( (w_off+32, h_off), (w_off+96, h_off), (w_off+128, h_off+32), (w_off+128, h_off+96), (w_off+96, h_off+128), (w_off+32, h_off+128), (w_off, h_off+96), (w_off, h_off+32) ), 1)
		
		j = j + 1
