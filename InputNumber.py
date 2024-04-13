import pygame
from pygame.locals import *
import pygwidgets

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tuple of legal editing keys
LEGAL_KEYS_TUPLE = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_HOME, pygame.K_BACKSPACE,
                    pygame.K_END, pygame.K_DELETE, pygame.K_RETURN, pygame.K_KP_ENTER)

# Legal keys to be typed
LEGAL_UNICODE_CHARS = '0123456789.-'

class InputNumber(pygwidgets.InputText):
    def __init__(self, window, loc, value='', fontName=None, callback=None, fontSize=24,
                 width=200, textColor=BLACK, backgroundColor=WHITE, focusColor=BLACK,
                 initialFocus=False, nickName=None, mask=None, keepFocusOnSubmit=False,
                 allowFloatingNumber=True, allowNegativeNumber=True):
        self.allowFloatingNumber = allowFloatingNumber
        self.allowNegativeNumber = allowNegativeNumber
        # Call the __init__ method of the base class
        super().__init__(self.new_method(window), loc, value, fontName, fontSize, callback, width,
                         textColor, backgroundColor, focusColor, initialFocus,
                         nickName, mask, keepFocusOnSubmit)

    def new_method(self, window):
        return window

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            # If it's not an editing or numeric key, ignore
            allowableKey = (event.key in LEGAL_KEYS_TUPLE) or (event.unicode in LEGAL_UNICODE_CHARS)
            if not allowableKey:
                return False

            if event.unicode == '-':  # User typed a minus
                if not self.allowNegativeNumber:
                    return False
                if self.cursorPosition > 0 or '-' in self.text:
                    return False  # Can't put minus sign after 1st char or multiple times

            if event.unicode == '.':
                if not self.allowFloatingNumber:
                    return False
                if '.' in self.text:
                    return False  # Can't enter a second period

        return super().handleEvent(event)

    def getValue(self):
        userString = super().getValue()
        try:
            if self.allowFloatingNumber:
                returnValue = float(userString)
            else:
                returnValue = int(userString)
        except ValueError:
            raise ValueError('Entry is not a number, needs to have at least one digit.')
        return returnValue
import pygame
from pygame.locals import *

class InputText:
    def __init__(self, window, loc, value='', fontName=None, fontSize=24,
                 callback=None, width=200, textColor=(0, 0, 0),
                 backgroundColor=(255, 255, 255), focusColor=(0, 0, 255),
                 initialFocus=False, nickName=None, mask=None,
                 keepFocusOnSubmit=False):
        self.window = window
        self.loc = loc
        self.value = value
        self.fontName = fontName
        self.fontSize = fontSize
        self.callback = callback
        self.width = width
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.focusColor = focusColor
        self.initialFocus = initialFocus
        self.nickName = nickName
        self.mask = mask
        self.keepFocusOnSubmit = keepFocusOnSubmit

        self.rect = pygame.Rect(self.loc[0], self.loc[1], self.width, self.fontSize + 4)
        self.text = self.value
        self.font = pygame.font.SysFont(self.fontName, self.fontSize)
        self.focus = False
        self.cursorVisible = False
        self.cursorPosition = len(self.text)

        if self.initialFocus:
            self.focus = True

    def draw(self):
        pygame.draw.rect(self.window, self.focusColor if self.focus else self.backgroundColor, self.rect)
        rendered_text = self.font.render(self.text, True, self.textColor)
        self.window.blit(rendered_text, (self.rect.x + 2, self.rect.y + 2))

        if self.focus and self.cursorVisible:
            cursor_x = self.font.size(self.text[:self.cursorPosition])[0] + 2
            pygame.draw.line(self.window, (0, 0, 0), (self.rect.x + cursor_x, self.rect.y + 2),
                             (self.rect.x + cursor_x, self.rect.y + self.fontSize + 2), 2)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.focus = True
            else:
                self.focus = False
        elif event.type == pygame.KEYDOWN:
            if self.focus:
                if event.key == pygame.K_BACKSPACE:
                    if self.cursorPosition > 0:
                        self.text = self.text[:self.cursorPosition - 1] + self.text[self.cursorPosition:]
                        self.cursorPosition -= 1
                elif event.key == pygame.K_DELETE:
                    if self.cursorPosition < len(self.text):
                        self.text = self.text[:self.cursorPosition] + self.text[self.cursorPosition + 1:]
                elif event.key == pygame.K_LEFT:
                    if self.cursorPosition > 0:
                        self.cursorPosition -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.cursorPosition < len(self.text):
                        self.cursorPosition += 1
                elif event.key == pygame.K_HOME:
                    self.cursorPosition = 0
                elif event.key == pygame.K_END:
                    self.cursorPosition = len(self.text)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if self.callback is not None:
                        self.callback()
                    if not self.keepFocusOnSubmit:
                        self.focus = False
                else:
                    if event.unicode.isprintable():
                        self.text = self.text[:self.cursorPosition] + event.unicode + self.text[self.cursorPosition:]
                        self.cursorPosition += 1

    def getValue(self):
        return self.text
