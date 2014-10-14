__author__ = 'jeremyk23SR'
import pygame, sys
from pygame.locals import *
from Animates import *
from config import *
import random


class soundObject(object):
    def __init__(self,name,intensity,chNum):
        self.intensity = intensity
        self.rectangle = None
        self.channelNum = chNum
        self.end = events[chNum]
        self.name = name

        #initialize as pygame sound
        self.load_sound(name)
        #initialize a pygame rectangle
        self.determineProperties()

    def load_sound(self, name):
        self.sound = pygame.mixer.Sound(name)
        self.sound.set_volume(0.2)

    def notifyEnd(self):
        #a timer is set for the length of the sound. when the timer finishes, it fires a pygame.event
        length = int(1000*self.sound.get_length())
        pygame.time.set_timer(self.end, length)


    def determineProperties(self):
        #determine height and width by sound length
        soundLength = self.sound.get_length() * 30

        #makes sure box is not too small
        if soundLength < 20:
            soundLength = 50

        boxWidth = soundLength
        boxHeight = boxWidth /2
        self.rectangle = SoundRectangle(LIGHT_BEIGE, 0, 0, boxWidth, boxHeight)

        #determine position on screen randomly
        xpos = random.randrange(0, int(screenWidth-boxWidth))

        ypos = random.randrange(0, int(screenHeight-boxHeight))
        self.rectangle.x = xpos
        self.rectangle.y = ypos

        self.rectangle = SoundRectangle(LIGHT_BEIGE, xpos, ypos, boxWidth, boxHeight)





