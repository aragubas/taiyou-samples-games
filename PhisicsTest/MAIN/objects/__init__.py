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

import pygame
from ENGINE import SPRITE as sprite
from ENGINE import DEBUGGING as debug
from PhisicsTest import MAIN as gameMain


class Player:
    def __init__(self):
        self.Rectangle = pygame.Rect(64, 16, 32, 32)
        self.ColideableCollection = list()

        self.Gravity = 7
        self.IsInAir = True
        self.IsJumping = False
        self.JumpingDelta = 0
        self.JumpingDeltaMax = 10
        self.Speed = 5
        self.JumpForce = 0
        self.JumpAllowed = True
        self.TimesJumped = 0
        self.TimesJumpedMax = 2

    def Render(self, Surface):
        sprite.Shape_Rectangle(Surface, (120, 50, 75), pygame.Rect(gameMain.CameraX + self.Rectangle[0], gameMain.CameraY + self.Rectangle[1], self.Rectangle[2], self.Rectangle[3]))

    def Update(self):
        debug.Set_Parameter("IsInAir", self.IsInAir)
        debug.Set_Parameter("IsJumping", self.IsJumping)
        debug.Set_Parameter("JumpingDelta", self.JumpingDelta)
        debug.Set_Parameter("TimesJumped", self.TimesJumped)
        debug.Set_Parameter("TimesJumpedMax", self.TimesJumpedMax)
        debug.Set_Parameter("JumpAllowed", self.JumpAllowed)
        debug.Set_Parameter("Rectangle", self.Rectangle)

        # -- Center Player on Camera -- #
        gameMain.CameraX = 800 / 2 - (self.Rectangle[0] + self.Rectangle[2])
        gameMain.CameraY = 600 / 2 - (self.Rectangle[1] + self.Rectangle[3])

        # -- if player is jumping -- #
        if self.IsJumping:
            self.JumpingDelta += 1

            self.JumpForce = (self.Gravity * 2.3)
            self.Rectangle[1] -= self.JumpForce + (self.JumpingDelta - self.JumpingDeltaMax)

            self.IsInAir = False

            if self.JumpingDelta >= self.JumpingDeltaMax:
                self.JumpingDelta = 0
                self.IsJumping = False
                self.IsInAir = True

            if self.JumpAllowed:
                if self.TimesJumped >= self.TimesJumpedMax:
                    self.JumpAllowed = False

        # -- If player is falling -- #
        if self.IsInAir:
            self.Rectangle[1] += self.Gravity

        # -- Check Colision -- #
        ColideablesSelected = list()
        for colideable in self.ColideableCollection:
            if colideable.Rectangle.colliderect(pygame.Rect(self.Rectangle[0], self.Rectangle[1], self.Rectangle[2], self.Rectangle[3])):
                ColideablesSelected.append(colideable)

        for colide in ColideablesSelected:
            LeftColision = False
            BottomColision = False
            RightColision = False

            if self.Rectangle[1] + self.Rectangle[3] < colide.Rectangle[1] + colide.Rectangle[3]:
                BottomColision = True

            if self.Rectangle[0] - self.Rectangle[2] < colide.Rectangle[0] - colide.Rectangle[2]:
                LeftColision = True

            if self.Rectangle[0] - self.Rectangle[2] < colide.Rectangle[0] + colide.Rectangle[2] and not LeftColision:
                RightColision = True

            debug.Set_Parameter("LeftColision", LeftColision)
            debug.Set_Parameter("BottomColision", BottomColision)
            debug.Set_Parameter("RightColision", RightColision)

            if LeftColision:
                print("Left Colision")
                self.Rectangle[0] = (colide.Rectangle[0] + colide.Rectangle[2])

            if RightColision:
                print("Right Colision")
                #self.Rectangle[0] = (colide.Rectangle[0] + colide.Rectangle[2])

            if BottomColision:
                print("Bottom Colision")
                self.IsInAir = False

        self.IsInAir = len(ColideablesSelected) == 0

        debug.Set_Parameter("ColideablesSelected", len(ColideablesSelected))

        # -- Check Keypresses -- #
        if pygame.key.get_pressed()[pygame.K_a]:
            if not self.IsJumping:
                self.Rectangle[0] -= self.Speed
            else:
                self.Rectangle[0] -= self.Speed * 2

        if pygame.key.get_pressed()[pygame.K_d]:
            if not self.IsJumping:
                self.Rectangle[0] += self.Speed
            else:
                self.Rectangle[0] += self.Speed * 2

        if pygame.key.get_pressed()[pygame.K_e]:
            gameMain.NichinCollection.append(Nichin(self.Rectangle[0] + self.Rectangle[2], self.Rectangle[1]))


    def EventUpdate(self, event):
        # -- Reset Button -- #
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            self.Rectangle[0] = 64
            self.Rectangle[1] = 64
            self.IsInAir = True

        # -- Jump -- #
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            if not self.IsInAir and not self.JumpAllowed:
                self.JumpAllowed = True
                self.TimesJumped = 0

            if self.JumpAllowed:
                self.IsJumping = True
                self.TimesJumped += 1


class ColideableObject:
    def __init__(self, rect=pygame.Rect(0, 256, 500, 32)):
        self.Rectangle = rect

    def Render(self, Surface):
        sprite.Shape_Rectangle(Surface, (10, 0, 50), pygame.Rect(gameMain.CameraX + self.Rectangle[0], gameMain.CameraY + self.Rectangle[1], self.Rectangle[2], self.Rectangle[3]))

class Nichin:
    def __init__(self, X, Y):
        self.Rectangle = pygame.Rect(X, Y, 5, 5)
        self.NichinMultiplier = 0
        self.InicialX = X
        self.ShotDistance = 800
        self.Index = -1

    def Draw(self, Surface):
        sprite.Shape_Rectangle(Surface, (230, 9, 5), pygame.Rect(gameMain.CameraX + self.Rectangle[0], gameMain.CameraY + self.Rectangle[1], self.Rectangle[2], self.Rectangle[3]))

    def Update(self):
        debug.Set_Parameter("Nichin.Instance:", self)
        debug.Set_Parameter("Nichin.X", self.Rectangle[0])

        self.NichinMultiplier += 5

        self.Rectangle[0] += self.NichinMultiplier

        if self.Rectangle[0] >= self.InicialX + self.ShotDistance:
            gameMain.NichinCollection.pop(self.Index)
