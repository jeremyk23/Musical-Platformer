__author__ = 'jeremyk23SR'
import pygame, sys
from pygame.locals import *
from config import *
from Animates import *
from MixerClass import *
from animate_decorators import *
from background import *

#Text display setup
pygame.font.init()
font = pygame.font.Font(None, 36)
text = font.render("Sound Platforming", 1, (201, 171, 220))
textpos = text.get_rect(centerx=screen.get_width()/2)

#music and mixer setup
pygame.mixer.init()
pygame.mixer.music.load('sounds/CIS_BackTrack.ogg')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#initalize musical sounds...TODO (wrap this all in a function call and make it automatic any time a new sound is added)
soundsList = []
chordC = soundObject('sounds/MusicalFX/Jump_C.ogg',3,1)
chordC.rectangle = LightPurpleDecorator(chordC.rectangle)
soundsList.append(chordC)
chordE = soundObject('sounds/MusicalFX/Jump_E.ogg',3,2)
chordE.rectangle = LightPurpleDecorator(chordE.rectangle)
soundsList.append(chordE)
chordF = soundObject('sounds/MusicalFX/Jump_F.ogg',3,3)
chordF.rectangle = LightPurpleDecorator(chordF.rectangle)
soundsList.append(chordF)
chordG = soundObject('sounds/MusicalFX/Jump_G.ogg',3,4)
chordG.rectangle = LightPurpleDecorator(chordG.rectangle)
soundsList.append(chordG)
chordA = soundObject('sounds/MusicalFX/Jump_A.ogg',3,5)
chordA.rectangle = LightPurpleDecorator(chordA.rectangle)
soundsList.append(chordA)
chordBb = soundObject('sounds/MusicalFX/Jump_Bb.ogg',3,6)
chordBb.rectangle = LightPurpleDecorator(chordBb.rectangle)
soundsList.append(chordBb)
#initialize sound effects
waterBubble = soundObject('sounds/FX/WaterBubble.ogg',3,6)
waterBubble.rectangle = DarkPurpleDecorator(waterBubble.rectangle)
soundsList.append(waterBubble)
waterGong = soundObject('sounds/FX/WaterGong.ogg',3,6)
waterGong.rectangle = DarkPurpleDecorator(waterGong.rectangle)
soundsList.append(waterGong)
bellSwirl = soundObject('sounds/FX/BellSwish.ogg',3,6)
bellSwirl.rectangle = DarkPurpleDecorator(bellSwirl.rectangle)
soundsList.append(bellSwirl)
noise = soundObject('sounds/FX/NoiseBuildUp.ogg',3,6)
noise.rectangle = DarkPurpleDecorator(noise.rectangle)
soundsList.append(noise)

#initialize objects
circle = Ball(DARK_BEIGE)
collidableRect = Visitor()
background = WallColor(BLACK)

def shuffleScreen(switch, soundsList):
    if switch is 1:
        for s in soundsList:
            xpos = random.randrange(0, int(screenWidth-s.rectangle.w))

            ypos = random.randrange(0, int(screenHeight-s.rectangle.h))
            s.rectangle.x = xpos
            s.rectangle.y = ypos

            if isinstance(s.rectangle, RectangleDecorator):
                s.rectangle.decorated.x = xpos
                s.rectangle.decorated.y = ypos

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
        #arrow key moves
            if event.key == K_LEFT:
                circle.moveBall(-5)
            elif event.key == K_RIGHT:
                circle.moveBall(5)
            elif event.key == K_UP:
                circle.jumpBall(-13)

        if event.type == KEYUP:
            if event.key == K_LEFT:
                circle.frictionApplied = True
            if event.key == K_RIGHT:
                circle.frictionApplied = True

    circle.checkWallBounds()
    screen.fill(background.color)
    screen.blit(text, textpos)
    for s in soundsList:
        #redraws rectangles on screen
        s.rectangle.drawOnScreen()

        #if ball collides with rectangle, play sound
        if s.rectangle.acceptVisitor(collidableRect, circle):
            s.sound.play()
            s.rectangle.isPlaying = True
            s.notifyEnd()

        #check to see if the sound has ended yet and hack to fix constant alerting
        if event.type == s.end and s.rectangle.isPlaying is not False:
                pygame.time.set_timer(s.end, 0)
                s.rectangle.isPlaying = False
                s.rectangle.setOriginalColor()
                background.shouldFade = True
        if s.rectangle.isPlaying: #if the sounds playing, perform fade
            s.rectangle.performFade()
            #prevents background from repeatedly fading while sound is still playing
            if background.shouldFade is True:
                background.performFade()

        #Spacebar events for Screen Shuffling
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                shuffleScreen(1, soundsList)
        if event.type == KEYUP:
            if event.key == K_SPACE:
                shuffleScreen(0, soundsList)


    circle.drawOnScreen()
    pygame.display.update()