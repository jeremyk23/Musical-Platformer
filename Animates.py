__author__ = 'jeremyk23SR'

__author__ = 'jeremyk23SR'

import pygame, sys
from pygame.locals import *
import colorsys
from strategy import LinearFade
from sound_states import *
from config import *
from math import *

screen = pygame.display.set_mode((1000, 640),0,32)

class Animate(object):
    def __init__(self, color = None, x = None, y = None, w = None, h = None):
        self.x = x
        self.y = y
        self.originalColor = color
        self.color = color
        self.w = w
        self.h = h
        self.HSV = colorsys.rgb_to_hsv(*[i/255 for i in self.color])
        self.fade = None
        self.isFading = False
        self.trackCreation = None

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
            return self.originalColor

    def setOriginalColor(self):
        self.color = self.originalColor
        self.HSV = colorsys.rgb_to_hsv(*[i/255 for i in self.color])


    def performFade(self):
        self.fade.ramp(self.HSV)
        self.changeBrightness()

#Each soundObject class gets an instance of this sound rectangle, its a platform
class SoundRectangle(Animate):
     def __init__(self,color,x,y,w,h):
         super(SoundRectangle, self).__init__(color,x,y,w,h)
         self.isPlaying = False
         self.fade = ExponentialFade()

     def drawOnScreen(self):
         self.rectangle = pygame.draw.rect(screen, self.color, Rect((self.x, self.y), (self.w, self.h)))
         self.w = self.rectangle.width
         self.h = self.rectangle.height

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

     def acceptVisitor(self, v, ball):
         #if the ball collides with me
         if v.collisionDetection(self, ball):
             if not self.isPlaying:
                self.isPlaying = True
                return True
         else:
             return False


class Ball(Animate):
    def __init__(self,color):
        self.vy = 0
        self.vx = 0
        self.prevX = 0
        self.prevY = 0
        self.gravity = 2
        self.friction = 1
        self.frictionApplied = True
        self.ball = None
        self.isJumping = False
        self.loopCount = 0
        super(Ball, self).__init__(color,0, 640, 10,0)
        self.originalColor = color
        self.HSV = colorsys.rgb_to_hsv(*[i/255 for i in self.color])
        self.originalHSV = colorsys.rgb_to_hsv(*[i/255 for i in self.color])

        #states for changing color of ball based on whether travelling up or down
        self.currentState = None
        self.goingUp = TravellingUpward(self)
        self.goingDown = TravellingDownward(self)

    def moveBall(self,pushSpeed):
        #don't apply friction while key is pressed
        self.frictionApplied = False
        self.vx = pushSpeed

    def applyFriction(self):
        #if traveling to right apply friction to left
        if self.vx > 0:
            self.vx += -self.friction
        #if traveling to left apply friction to the right
        if self.vx < 0:
            self.vx += self.friction

    def jumpBall(self, jumpSpeed):
        if not self.isJumping:
            self.vy = jumpSpeed + self.gravity
            self.isJumping = True
    def setUpState(self):
        self.currentState = self.goingUp
    def setDownState(self):
        self.currentState = self.goingDown
    def performFade(self):
        self.currentState.performFade()

    def drawOnScreen(self):
        #if ball is moving downwards, make it ok to jump again
        self.prevY = self.y
        self.y = self.y + (self.vy + self.gravity)
        if (self.prevY - self.y < 2):
            self.isJumping=False
        #move x position and keep track of its last place
        self.prevX = self.x
        self.x += self.vx

        self.ball = pygame.draw.circle(screen, self.color, (self.x,self.y), self.w )

        #dumb hack to slow down gravity, increment every-other loop iteration
        if self.loopCount == 0:
            self.vy = self.vy + self.gravity
            if self.frictionApplied:
                self.applyFriction()
                self.x += self.vx
        if self.loopCount < 4:
            self.loopCount += 1
        else:
            self.loopCount = 0
        #set fade state based on whether travelling up or down
        if self.vy > 2:
            self.setDownState()
            self.currentState.changeBrightness()
        if self.vy < 0:
            self.setUpState()
            self.currentState.changeBrightness()
        if self.vy is 2:
            self.setOriginalColor()

    def checkWallBounds(self):
        #if ball hits floor or ceiling
        if self.y > screenHeight - self.w:
            self.y = screenHeight - self.w
            #prevents ball from getting stuck on floor
            if self.vy > 0:
                self.vy = 0
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy

        #if ball hits walls
        if self.x > screenWidth - self.w:
            self.x = screenWidth - self.w
            self.vx = -self.vx
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx

class Visitor(pygame.Rect):
    def __init__(self):
        pass
    def collisionDetection(self, soundRect, ball):
        collisionRect = pygame.Rect(soundRect.x, soundRect.y, soundRect.w, soundRect.h)
        if ball.y <= collisionRect.bottom and ball.y >= collisionRect.top:
            #ball moving to right hits left side of rect
            if ball.x > collisionRect.left and ball.prevX < collisionRect.left:
                ball.x = collisionRect.left
                ball.vx = -ball.vx
                return True
            #ball moving to left, hits right side
            if ball.x < collisionRect.right and ball.prevX > collisionRect.right:
                ball.x = collisionRect.right
                ball.vx = -ball.vx
                return True
        if ball.x <= collisionRect.right and ball.x >= collisionRect.left:
            #ball moving down and hits top of rect
            if ball.y > collisionRect.top and ball.prevY < collisionRect.top:
                ball.y = collisionRect.top
                ball.vy = -ball.vy
                return True
            #ball moving up and hits bottom of rect
            if ball.y < collisionRect.bottom and ball.prevY > collisionRect.bottom:
                ball.y = collisionRect.bottom
                ball.vy = -ball.vy
                return True
        else: return False