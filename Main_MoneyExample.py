import pygame
from pygame.locals import *
import sys
import pygwidgets  # Assuming pygwidgets is a valid GUI library

# Custom classes (replace with your actual implementations)
from DisplayMoney import DisplayMoney
from InputNumber import InputNumber

# Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Initialize Pygame and create the window
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# Define GUI elements using pygwidgets
title = pygwidgets.DisplayText(window, (0, 40),
                               'Demo of InputNumber and DisplayMoney fields',
                               width=WINDOW_WIDTH, justified='center')
inputCaption = pygwidgets.DisplayText(window, (20, 150),
                                      fontSize=24,
                                      'Input money amount:',
                                      width=190,
                                      justified='right')
inputField = InputNumber(window, (230, 150), '', width=150)
okButton = pygwidgets.TextButton(window, (430, 150), 'OK')
outputCaption1 = pygwidgets.DisplayText(window, (20, 300),
                                        'Output dollars & cents: ', fontSize=24,
                                        width=190,
                                        justified='right')
moneyField1 = DisplayMoney(window, (230, 300), '',
                           textColor=BLACK,
                           backgroundColor=WHITE, width=150)
outputCaption2 = pygwidgets.DisplayText(window, (20, 400),
                                        'Output dollars only: ', fontSize=24,
                                        width=190,
                                        justified='right')
moneyField2 = DisplayMoney(window, (230, 400), '',
                           textColor=BLACK,
                           backgroundColor=WHITE, width=150,
                           showCents=False)

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        okButton.handleEvent(event)  # Handle OK button click

        if event.type == KEYDOWN and event.key == K_RETURN:
            try:
                theValue = inputField.getValue()
            except ValueError:  # Any remaining error
                inputField.setValue('(not a number)')
            else:  # Input was OK
                theText = str(theValue)
                moneyField1.setValue(theText)
                moneyField2.setValue(theText)

    # Clear the window and draw elements
    window.fill(BACKGROUND_COLOR)
    title.draw()
    inputCaption.draw()
    inputField.draw()
    okButton.draw()
    outputCaption1.draw()
    moneyField1.draw()
    outputCaption2.draw()
    moneyField2.draw()

    # Update the display and limit frame rate
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
