'''
Created on 27/02/2015

@author: Sam Hunt
'''

import sys, pygame, random
from pygame.locals import *
from pygame.constants import *

pygame.init()

size = width, height = 800, 600
blocksize = 2
red, white, black = (255, 0, 0), (255,255,255), (0,0,0)
colors = [red, white]
screen = pygame.display.set_mode(size)

def drawflag(surface, flaglist):
    for y in xrange (height/blocksize):
        for x in xrange(width/blocksize):
            pygame.draw.rect(surface, colors[flaglist[y*width/blocksize + x]], pygame.Rect((x*blocksize,y*blocksize),(blocksize,blocksize)))
            
def drawcell_xy(surface, flaglist, x, y):            
    pygame.draw.rect(surface, colors[flaglist[y*width + x]], pygame.Rect((x*blocksize,y*blocksize),(blocksize,blocksize)))
    
def drawcell_i(surface, flaglist, i):
    x, y = i % width, (i - (i % width))/width  
    pygame.draw.rect(surface, colors[flaglist[i]], pygame.Rect((x*blocksize,y*blocksize),(blocksize,blocksize)))

def process2(listn):
    i, j = 0, len(listn)-1
    while i <= j :
        tempi, tempj = listn[i], listn[j] 
        listn[i], listn[j] = tempj, tempi

        while listn[i] == 1: #white
            i+=1
        while listn[j] == 0: #red
            j-=1
    return True
        
        
flagarray = [random.randint(0, 1) for _ in xrange(0, width/blocksize * height/blocksize)]
drawflag(screen, flagarray)
if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("N - new,  SPACE - sort", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, pygame.Rect(50,50, 200,100))
pygame.display.flip()

finished = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()
        elif event.type == KEYDOWN and event.key == K_n: 
            flagarray = [random.randint(0, 1) for _ in xrange(0, width/blocksize * height/blocksize)]
            screen.fill(black)
            drawflag(screen, flagarray)
            pygame.display.flip()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            finished = False
        
    if finished == False:
        finished = process2(flagarray)
        drawflag(screen, flagarray)
        pygame.display.flip()