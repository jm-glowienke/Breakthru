# Import necessary libraries
import numpy as np
import sys
import time
import pygame
from pygame.locals import *

##### DECLARE GLOBAL VARIABLES

# storing whose turn it is
### Not sure if this is needed in such a way, since only move figures
turn = 'gold'
# 2 = gold, 1 = silver, 3 = flagship

# check if game is draw
draw = None

# check if there is a winner
winner = None

# set width and height of game window
width = 500
height = 500

# set colors
white = (255,255,255)
black = (0,0,0)
silver = (192,192,192)
gold = (255,223,0)

# setting up the board
#board = np.zeros(11,11)
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
                       [0,0,0,0,0,0,0,0,0,0,0]])


###### INITIALIZE GAME WINDOW
pygame.init()
fps = 30

# clock for tracking time
CLOCK = pygame.time.Clock()

# this method is used to build the infrastructure of the display
screen = pygame.display.set_mode((width, height + 100), 0, 32)
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



def game_initiate_window():

    # drawing vertical lines
    pygame.draw.line(screen, black, (width / 11, 0), (width / 11, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 2, 0), (width / 11 * 2, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 3, 0), (width / 11 * 3, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 4, 0), (width / 11 * 4, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 5, 0), (width / 11 * 5, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 6, 0), (width / 11 * 6, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 7, 0), (width / 11 * 7, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 8, 0), (width / 11 * 8, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 9, 0), (width / 11 * 9, height), 7)
    pygame.draw.line(screen, black, (width / 11 * 10, 0), (width / 11 * 10, height), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, black, (0, height / 11), (width, height / 11), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 2), (width, height / 11 * 2), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 3), (width, height / 11 * 3), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 4), (width, height / 11 * 4), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 5), (width, height / 11 * 5), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 6), (width, height / 11 * 6), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 7), (width, height / 11 * 7), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 8), (width, height / 11 * 8), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 9), (width, height / 11 * 9), 7)
    pygame.draw.line(screen, black, (0, height / 11 * 10), (width, height / 11 * 10), 7)
    draw_status()

def draw_status():

    global draw

    if winner is None:
        message = turn.upper() + "'s turn"
    else:
        message = turn.upper + "won!"
    if draw:
        message = "Game Draw!"


game_initiate_window()
