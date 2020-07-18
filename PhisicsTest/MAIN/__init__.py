#!/usr/bin/python3.7
#   Copyright 2020 Aragubas
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#

from ENGINE import SPRITE as sprite
from ENGINE import TaiyouMain as taiyouMain
from PhisicsTest.MAIN import objects
import pygame

Player = objects.Player
ColideableObjectCollection = list()
NichinCollection = list()
CameraX = 0
CameraY = 0


def Initialize(DISPLAY):
    global Player
    global ColideableObjectCollection
    global NichinCollection

    Player = objects.Player()
    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(0, 400, 170, 16)))
    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(240, 350, 100, 16)))
    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(390, 350, 100, 16)))
    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(170, 350, 20, 128)))

    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(0, 0, 16, 400)))
    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(100, 0, 16, 330)))


def EventUpdate(event):
    global Player

    Player.EventUpdate(event)

def Update():
    global Player
    global ColideableObjectCollection
    global NichinCollection

    Player.Update()
    # -- Update the ColiableList -- #
    Player.ColideableCollection = ColideableObjectCollection

    for i, nichin in enumerate(NichinCollection):
        nichin.Index = i
        nichin.Update()

def GameDraw(DISPLAY):
    DISPLAY.fill((0, 101, 237))
    global Player
    global ColideableObjectCollection
    global NichinCollection

    # -- Render Platforms -- #
    for obj in ColideableObjectCollection:
        obj.Render(DISPLAY)

    # -- Render Player -- #
    Player.Render(DISPLAY)

    # -- Render Nichin -- #
    for nichin in NichinCollection:
        nichin.Draw(DISPLAY)


def Unload():
    pass
