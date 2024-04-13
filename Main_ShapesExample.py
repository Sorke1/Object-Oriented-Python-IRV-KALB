import pygame
import sys
import random
from pygame.locals import *
from Square import Square
from Circle import Circle
from Triangle import Triangle
import pygwidgets

# Set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 10

# Set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()
shapesList = []
shapeClassesTuple = (Square, Circle, Triangle)

# Create shapes and add them to the shapesList
for i in range(N_SHAPES):
    randomlyChosenClass = random.choice(shapeClassesTuple)
    oShape = randomlyChosenClass(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    shapesList.append(oShape)

oStatusLine = pygwidgets.DisplayText(window, (4, 4), fontSize=28)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            # Reverse order to check last drawn shape first
            for oShape in reversed(shapesList):
                if oShape.clickedInside(event.pos):
                    area = oShape.getArea()
                    area = str(area)
                    theType = oShape.getType()
                    newText = f'Clicked on a {theType} whose area is {area}'
                    oStatusLine.setValue(newText)
                    break  # only deal with topmost shape

    # Tell each shape to draw itself
    window.fill(WHITE)
    for oShape in shapesList:
        oShape.draw()
    oStatusLine.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
