# Import necessary libraries
import numpy as np
import sys
import time
import pygame
from pygame.locals import *

##### DECLARE GLOBAL VARIABLES

# storing whose turn it is
### Not sure if this is needed in such a way, since only move figures
turn = '2'
# 2 = gold, 1 = silver, 3 = flagship
# check if game is draw
draw = None

# set width and height of game window
width = 500
height = 500

# set colors
white = (255,255,255)
black = (0,0,0)
silver = (192,192,192)
gold = (255,223,0)

# setting up the board
board = np.zeros(11,11)
# 1 = silver, 2 = gold, 3 = flagship
board_initial = np.array([[0,0,0,0,0,0,0,0,0,0,0], # possible initial setup to start from
                       [0,0,0,1,1,1,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0],
                       [0,1,0,0,2,2,2,0,0,1,0],
                       [0,1,0,2,0,0,0,2,0,1,0],
                       [0,1,0,2,0,3,0,2,0,1,0],
                       [0,1,0,2,0,0,0,2,0,1,0],
                       [0,1,0,0,2,2,2,0,0,1,0],
                       [0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,1,1,1,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0]]


###### INITIALIZE GAME WINDOW
pygame.init()
fps = 30

# clock for tracking time
CLOCK = pygame.time.Clock()

# this method is used to build the infrastructure of the display
screen = pygagme.display.set_mode((width, height + 100), 0, 32)
# set caption for game window
pygame.display.set_caption("Let's play Breakthru!")

# load images as python objects
ship_gold = pygame.image.load("ship_gold.png")
ship_silver = pygame.image.load("ship_silver.png")
ship_flag = pygame.image.load("ship_flag.png")

# resize images
ship_gold = pygame.transform.scale(ship_gold,(80,80))
ship_silver = pygame.transform.scale(ship_silver,(80,80))
ship_flag = pygame.transform.scale(ship_flag,(80,80))
