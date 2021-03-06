import pygame, sys
from pygame.locals import *
from pygame import *

tileMap = []
TILESIZE = 40
MAPWIDTH = 10
MAPHEIGHT = 10
displaySurf = None
norm = 0
wall = 1
chest = 2
black = (0, 0, 0)
gray  = (192, 192, 192)
yellow= (255, 255, 51)
	
colors = {norm: gray, wall: black, chest: yellow}
tileMap = []
for i in range(MAPHEIGHT):
    toAppend = []
    for j in range(MAPWIDTH):
        toAppend.append(norm)
    tileMap.append(toAppend)
    
	
	#size the tileMap
    
	#create wall
for i in range(MAPHEIGHT):
    for j in range(MAPWIDTH):
        if i==0 or i==MAPHEIGHT-1 or j==0 or j==MAPWIDTH-1:
            tileMap[i][j] = wall
	#create two chests
tileMap[1][1] = chest
tileMap[3][2] = chest
	
	#display map
pygame.init()
displaySurf = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
while True:
	pygame.init()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.exit()
			sys.exit()
	for row in range(MAPWIDTH):
		for col in range(MAPHEIGHT):
			pygame.draw.rect(displaySurf,colors[tileMap[row][col]],(col*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
	pygame.display.update()
	#createMap()
	#print(tileMap)