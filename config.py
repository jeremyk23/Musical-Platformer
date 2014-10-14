__author__ = 'jeremyk23SR'
import pygame, sys
from pygame.locals import *

#Sound Mixer
pygame.mixer.init()

#Ending up not using these channels...I'm still scared to delete them completely
pygame.mixer.set_num_channels(8)
# ch1 = pygame.mixer.Channel(0)
# ch2 = pygame.mixer.Channel(1)
# ch3 = pygame.mixer.Channel(2)
# channelList = [ch1,ch2,ch3]


events = {
        1 : USEREVENT + 2,
        2 : USEREVENT + 3,
        3 : USEREVENT + 4,
        4 : USEREVENT + 5,
        5 : USEREVENT + 6,
        6 : USEREVENT + 7,
        7 : USEREVENT + 8,
        8 : USEREVENT + 9,
        9 : USEREVENT + 10,
        10 : USEREVENT + 11,
        11 : USEREVENT + 12,
        12 : USEREVENT + 13,
        }

#Globals
screenWidth = 1000
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight),0,32)
pygame.display.set_caption('Sound Visualizations')
BLACK = (16.0, 0.0, 24.0)
WHITE = (255.0,255.0,255.0)
MUTED_PURPLE = (201.0,171.0, 220.0)
RED = (255, 0, 0)
DARK_PURPLE = (62.0,28.0,86.0)
GRAY_PURPLE = (34.0,26.0,29.0)
LIGHT_PURPLE = (201.0,171.0,220.0)
LIGHT_BEIGE = (255.0,226.0,179.0)
DARK_BEIGE = (209.0,151.0,117)
