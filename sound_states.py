__author__ = 'jeremyk23SR'

#states: is playing______isNotPlaying
#actions: start playing, stopPlaying
from strategy import *

class SoundState(object):
    def __init__(self, parent):
        self.parent = parent
        self.fade = None
    def changeBrightness(self):
        pass


class TravellingUpward(SoundState):
    def __init__(self, parent):
        super(TravellingUpward, self).__init__(parent)
        self.fade = SlowBrightFade()

    def changeBrightness(self):
         if self.parent.HSV[2] <= 0.9:
             r,g,b, self.parent.HSV = self.fade.ramp(self.parent.HSV)
             self.parent.color = r,g,b
             return self.parent.color


class TravellingDownward(SoundState):
    def __init__(self, parent):
        super(TravellingDownward, self).__init__(parent)
        self.fade = SlowDimFade()
    def changeBrightness(self):
         if self.parent.HSV[2] >= 0.05:
             r,g,b, self.parent.HSV = self.fade.ramp(self.parent.HSV)
             self.parent.color = r,g,b
             return self.parent.color