__author__ = 'jeremyk23SR'

import colorsys

class MixerFade:
    def ramp(self, hsv):
        pass

class BrightFade(MixerFade):
    def ramp(self, hsv):
        hsv = hsv[:-1] + (hsv[-1]*1.03,)
        r,g,b = colorsys.hsv_to_rgb(*hsv)
        return r*255, g*255, b*255, hsv

class DimFade(MixerFade):
    def ramp(self, hsv):
        hsv = hsv[:-1] + (hsv[-1]*.97,)
        r,g,b = colorsys.hsv_to_rgb(*hsv)
        return r*255, g*255, b*255, hsv

class SlowBrightFade(MixerFade):
    def ramp(self, hsv):
        hsv = hsv[:-1] + (hsv[-1]*1.02,)
        r,g,b = colorsys.hsv_to_rgb(*hsv)
        return r*255, g*255, b*255, hsv

class SlowDimFade(MixerFade):
    def ramp(self, hsv):
        hsv = hsv[:-1] + (hsv[-1]*0.98,)
        r,g,b = colorsys.hsv_to_rgb(*hsv)
        return r*255, g*255, b*255, hsv

class LinearFade(MixerFade):
    def ramp(self, hsv):
        if hsv == 0:
            return False
        hsv = hsv[:-1] + (hsv[-1]-.003,)
        r,g,b = colorsys.hsv_to_rgb(*hsv)
        return r*255, g*255, b*255, hsv

class ExponentialFade(MixerFade):
    def ramp(self, hsv):
        if hsv == 0:
            return False
        hsv = hsv[:-1] + (hsv[-1]*0.98,)
        r,g,b = colorsys.hsv_to_rgb(*hsv)
        return r*255, g*255, b*255, hsv