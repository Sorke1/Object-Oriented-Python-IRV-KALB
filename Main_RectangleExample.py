import pygame
import sys
from pygame.locals import *
from Rectangle import *

# Set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'

# Set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()
rectanglesList = []

# Create rectangles and add them to the rectanglesList
for i in range(N_RECTANGLES):
    oRectangle = Rectangle(window)
    rectanglesList.append(oRectangle)

whichRectangle = FIRST_RECTANGLE
oFirstRectangle = None
oSecondRectangle = None

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oRectangle in rectanglesList:
                if oRectangle.clickedInside(event.pos):
                    print('Clicked on', whichRectangle, 'rectangle.')
                    if whichRectangle == FIRST_RECTANGLE:
                        oFirstRectangle = oRectangle
                        whichRectangle = SECOND_RECTANGLE
                    elif whichRectangle == SECOND_RECTANGLE:
                        oSecondRectangle = oRectangle

                    # User has chosen 2 rectangles, let's compare
                    if oFirstRectangle and oSecondRectangle:
                        size1 = oFirstRectangle.getSize()
                        size2 = oSecondRectangle.getSize()

                        print('First rectangle:', size1)
                        print('Second rectangle:', size2)

                        if size1 == size2:
                            print('Rectangles are the same size.')
                        elif size1 < size2:
                            print('First rectangle is smaller than second rectangle.')
                        else:
                            print('First rectangle is larger than second rectangle.')

                        # Reset for next comparison
                        whichRectangle = FIRST_RECTANGLE
                        oFirstRectangle = None
                        oSecondRectangle = None

    # Clear the window and draw all rectangles
    window.fill(WHITE)
    for oRectangle in rectanglesList:
        oRectangle.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
