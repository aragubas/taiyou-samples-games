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

def Initialize(DISPLAY):
    global Player
    global ColideableObjectCollection
    global NichinCollection

    Player = objects.Player()
    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(0, 400, 150, 16)))
    ColideableObjectCollection.append(objects.ColideableObject(pygame.Rect(240, 350, 100, 16)))

    NichinCollection.append(objects.Nichin(32, 32))

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

    for nichin in NichinCollection:
        nichin.Update()

def GameDraw(DISPLAY):
    DISPLAY.fill((55, 55, 55))
    global Player
    global ColideableObjectCollection
    global NichinCollection

    Player.Render(DISPLAY)

    for obj in ColideableObjectCollection:
        obj.Render(DISPLAY)

    for nichin in NichinCollection:
        nichin.Draw(DISPLAY)


def Unload():
    pass
