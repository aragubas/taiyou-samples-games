from ENGINE import SPRITE as sprite
from ENGINE import REGISTRY as reg
import pygame
from TileEditor.MAIN.SCREEN import Editor as editorScreen
from TileEditor.MAIN.SCREEN import Menu as menuScreen
from math import *

# -- Game Engine Vars -- #
Messages = list()

DefaultDisplay = pygame.Surface((0,0))
Cursor_Position = 0, 0

CurrentFileName = "Map.txt"

CurrentScreen = 0
def Initialize(DISPLAY):
    global CurrentFileName
    # -- Initialize Screens -- #
    menuScreen.Initialize(DISPLAY)
    Messages.append("SET_FPS:60")
    Messages.append("RESIZIABLE_WINDOW:True")

def GameDraw(DISPLAY):
    global CurrentScreen
    global DefaultDisplay
    DISPLAY.fill((22, 22, 22))
    DefaultDisplay = DISPLAY

    if CurrentScreen == 0:
        menuScreen.GameDraw(DISPLAY)
    if CurrentScreen == 1:
        editorScreen.GameDraw(DISPLAY)

    sprite.ImageRender(DISPLAY, "/0.png", Cursor_Position[0], Cursor_Position[1])

def EventUpdate(event):
    global Cursor_Position
    global CurrentScreen

    # -- Detect Mouse Motion -- #
    if event.type == pygame.MOUSEMOTION:
        Cursor_Position = pygame.mouse.get_pos()

    if event.type == pygame.KEYUP and event.key == pygame.K_F5:
        sprite.Reload()

    if CurrentScreen == 0:
        menuScreen.EventUpdate(event)
    if CurrentScreen == 1:
        editorScreen.EventUpdate(event)


def Update():
    global CurrentScreen
    global CurrentFileName

    if CurrentScreen == 0:
        menuScreen.Update()
    if CurrentScreen == 1:
        editorScreen.Update()
    pygame.display.set_caption("Tile Editor [{0}]".format(CurrentFileName))

# -- Send the messages on the Message Quee to the Game Engine -- #
def ReadCurrentMessages():
    try:
        for x in Messages:
            Messages.remove(x)
            print("Game : MessageSent[" + x + "]")
            return x
    except:
        return ""
