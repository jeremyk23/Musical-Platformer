__author__ = 'jeremyk23SR'
import pygame, sys
from pygame.locals import *
from MixerClass import *
from Animates import *
from config import *

class RectangleDecorator(SoundRectangle):
    def __init__(self, decorated):
        super(RectangleDecorator, self).__init__(decorated.color,decorated.x,
        decorated.y,decorated.w, decorated.h)
        self.decorated = decorated
        self.newShape = None
    def changeBrightness(self):

         if self.HSV[2] >= 0.05:
             self.isFading = True
             if  not self.fade.ramp(self.HSV):
                 self.isPlaying = False
             r,g,b, self.HSV = self.fade.ramp(self.HSV)
             self.color = r,g,b
             pygame.draw.rect(screen, self.color, Rect((self.x,self.y), (self.w, self.h)))
             return self.color
         else:
             self.isFading = False
    def drawOnScreen(self):

        self.decorated = pygame.draw.rect(screen, self.decorated.color,
        Rect((self.decorated.x, self.decorated.y), (self.decorated.w, self.decorated.h)))

class LightPurpleDecorator(RectangleDecorator):
    def __init__(self, decorated):
        super(RectangleDecorator, self).__init__(decorated.color,decorated.x,
        decorated.y,decorated.w, decorated.h)
        self.decorated = decorated
        self.newShape = None
    def drawOnScreen(self):
        #color has to be hardcoded? To-Do Why?
        self.decorated = pygame.draw.rect(screen, LIGHT_BEIGE,
        Rect((self.decorated.x, self.decorated.y), (self.decorated.w, self.decorated.h)))

        xpos = self.decorated.x + (self.decorated.w/2)
        ypos = self.decorated.y - (self.decorated.h/2)
        self.newShape = pygame.draw.rect(screen,LIGHT_PURPLE,
        Rect((xpos, ypos), (self.decorated.h-25, self.decorated.w+25)))


class DarkPurpleDecorator(RectangleDecorator):
    def __init__(self, decorated):
        super(RectangleDecorator, self).__init__(decorated.color,decorated.x,
        decorated.y,decorated.w, decorated.h)
        self.decorated = decorated
        self.newShape = None
    def drawOnScreen(self):
        #color has to be hardcoded? To-Do Why?
        self.decorated = pygame.draw.rect(screen, LIGHT_BEIGE,
        Rect((self.decorated.x, self.decorated.y), (self.decorated.w, self.decorated.h)))

        xpos = self.decorated.x + (self.decorated.w/2)
        ypos = self.decorated.y - (self.decorated.h/2)
        self.newShape = pygame.draw.rect(screen,DARK_PURPLE,
        Rect((xpos, ypos), (self.decorated.h-25, self.decorated.w+25)))