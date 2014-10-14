__author__ = 'jeremyk23SR'
import colorsys
from strategy import *

#TODO: one day wrap this all with the animates into a big super class of "Displayables"
class WallColor(object):
    def __init__(self,color):
        self.originalColor = color
        self.color = color
        self.HSV = colorsys.rgb_to_hsv(*[i/255 for i in self.color])
        self.originalHSV = colorsys.rgb_to_hsv(*[i/255 for i in self.color])

        self.fade = None
        self.brightFade = BrightFade()
        self.dimFade = DimFade()
        self.setBrightFade()
        self.isFading = False
        self.shouldFade = True
        self.peakBrightness = False

    def changeBrightness(self):
        if self.HSV[2] <= 0.7 and self.originalHSV[2] <= self.HSV[2]:

            self.isFading = True
            if  not self.fade.ramp(self.HSV):
                self.isPlaying = False
            r,g,b, self.HSV = self.fade.ramp(self.HSV)
            #if its ramping up brightness and hits peak level, switch to the dim fader
            if self.HSV[2] >= .6 and self.peakBrightness is False:
                self.setDimFade()
                self.peakBrightness = True
            self.color = r,g,b
            return self.color
        else:
            self.isFading = False
            self.shouldFade = False
            self.setOriginalColor()
            self.peakBrightness = False
            self.setBrightFade()
            return self.originalColor

    def setDimFade(self):
        self.fade = self.dimFade
    def setBrightFade(self):
        self.fade = self.brightFade

    def setOriginalColor(self):
        self.color = self.originalColor
        self.HSV = self.originalHSV

    def performFade(self):
        self.fade.ramp(self.HSV)
        self.changeBrightness()
