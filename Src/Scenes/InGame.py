from Src.Scenes.Scene import Scene
from Src.Gui.Label import Label
from Src.Gui.Image import Image
from Src.GameObjects.Player import Player
from Src.GameObjects.GameBoard import GameBoard
from Src.GameObjects.Bullet import Bullet
import pygame

class InGame(Scene):

    def __init__(self, game):
        super().__init__(game)
        gameWidth, gameHeight = self.game.windowSize
        boardPosX = 256
        boardPosY = 32
        boardWidth = gameWidth - 288
        boardHeight = gameHeight - 64
        self.guiElements = [
            Image((32, 32), (32, 32), "Assets/health-full.png"),
            Image((64, 32), (32, 32), "Assets/health-full.png"),
            Image((96, 32), (32, 32), "Assets/health-full.png"),
            Image((128, 32), (32, 32), "Assets/health-empty.png"),
            Image((160, 32), (32, 32), "Assets/health-empty.png"),
            Image((192, 32), (32, 32), "Assets/health-empty.png"),
            Image((32, 64 + 8), (32, 32), "Assets/coin.png"),
            Label((64, 64 + 8), (128, 32), "0", (5, 0), (255, 255, 255), None, 27, None, None, False),
            Label((32, 96 + 16), (192, 32), "Punkty: 0", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, 128), (192, 32), "Level: 1", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, gameHeight - 64), (192, 32), "Broń: Podstawowa", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, gameHeight - 46), (192, 32), "Pocisków: 30/30", (5, 0), (255, 255, 255), None, 14, None, None, False),
        ]
        self.gameObjects = [
            Player(self.game, (gameWidth / 2 + boardPosX / 2, gameHeight - 64), (32, 32), "Assets/alien1.png", True),
            GameBoard(self.game, (boardPosX, boardPosY), (boardWidth, boardHeight), "Assets/alien1.png", True)
        ]

    def createBullet(self, position):
        bullet = Bullet(self.game, position, (4, 8), "Assets/coin.png", True)
        self.gameObjects.append(bullet)
        return True

    def destroyObject(self, destroyedObject):
        self.gameObjects.remove(destroyedObject)

    def eventHandle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if not self.gameObjects[0].moveLeft: 
                    self.gameObjects[0].moveLeft = True
            elif event.key == pygame.K_d:
                if not self.gameObjects[0].moveRight: 
                    self.gameObjects[0].moveRight = True
            elif event.key == pygame.K_SPACE:
                    self.gameObjects[0].fire = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.gameObjects[0].moveLeft = False
            elif event.key == pygame.K_d:
                self.gameObjects[0].moveRight = False
            elif event.key == pygame.K_SPACE:
                self.gameObjects[0].fire = False

    def onRender(self):
        self.game.clock.tick(60)
        for gameObject in self.gameObjects:
            gameObject.onRender(self.game.screen)
        for element in self.guiElements:
            element.onRender(self.game.screen)

    def onTick(self):
        if self.game.paused: return
        for gameObject in self.gameObjects:
            gameObject.onTick()