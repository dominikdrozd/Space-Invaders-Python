from Src.Scenes.Scene import Scene
from Src.Gui.Label import Label
from Src.Gui.Image import Image
from Src.GameObjects.Player import Player
from Src.GameObjects.GameBoard import GameBoard
from Src.GameObjects.Bullet import Bullet
from Src.GameObjects.Alien import Alien
import pygame

class InGame(Scene):

    def __init__(self, game):
        super().__init__(game)
        gameWidth, gameHeight = self.game.windowSize
        self.boardPosX = 256
        self.boardPosY = 32
        self.boardWidth = gameWidth - 288
        self.boardHeight = gameHeight - 64
        self.player = Player(self.game, (gameWidth / 2 + self.boardPosX / 2, gameHeight - 70), (32, 32), "Assets/ship.png", True)
        self.board = GameBoard(self.game, (self.boardPosX, self.boardPosY), (self.boardWidth, self.boardHeight), "Assets/map.png", True)
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
            Label((32, 128), (192, 32), "Poziom: 1", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, gameHeight - 64), (192, 32), "Broń: Podstawowa", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, gameHeight - 46), (192, 32), "Amunicja: -1", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, 256 - 8), (192, 32), "Sterowanie", (5, 0), (255, 255, 255), None, 22, None, None, False),
            Label((32, 256 + 18), (192, 32), "A - Lewo", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, 256 + 36), (192, 32), "D - Prawo", (5, 0), (255, 255, 255), None, 14, None, None, False),
            Label((32, 256 + 54), (192, 32), "SPACJA - Strzał", (5, 0), (255, 255, 255), None, 14, None, None, False),
        ]
        self.gameObjects = [
            Alien(self.game, self.calculateMapPosition((64, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((96, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((128, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((160, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((192, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((224, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((256, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((288, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((320, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((352, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((384, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((416, 32)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((64, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((96, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((128, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((160, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((192, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((224, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((256, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((288, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((320, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((352, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((384, 96)), (32, 32), "Assets/alien1.png", True),
            Alien(self.game, self.calculateMapPosition((416, 96)), (32, 32), "Assets/alien1.png", True),
        ]

    def calculateMapPosition(self, offset):
        x = self.boardPosX + offset[0]
        y = self.boardPosY + offset[1]
        return (x, y)

    def createBullet(self, position, side, targets):
        bullet = Bullet(self.game, position, (4, 8), "Assets/coin.png", True, side, targets)
        self.gameObjects.append(bullet)
        return True

    def destroyObject(self, destroyedObject):
        if destroyedObject in self.gameObjects: 
            self.gameObjects.remove(destroyedObject)

    def refreshAliens(self):
        aliens = [alien for alien in self.gameObjects if isinstance(alien, Alien)]
        bullets = [bullet for bullet in self.gameObjects if isinstance(bullet, Bullet)]
        if len(aliens) <= 0:
            for bullet in bullets:
                bullet.onDestroy()
            for j in range(5):
                for i in range(10):
                    alien = Alien(self.game, self.calculateMapPosition((32 + i * 32, 32 + 2 * j * 32)), (32, 32), "Assets/alien1.png", True)
                    self.gameObjects.append(alien)

    def updateHud(self):
        for i in range(0,6):
            if i < self.player.health:
                self.guiElements[i].changeImage("Assets/health-full.png")
            else:
                self.guiElements[i].changeImage("Assets/health-empty.png")
        self.guiElements[7].text = str(self.player.money)
        self.guiElements[8].text = "Punkty: " + str(self.player.points)

    def eventHandle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if not self.player.moveLeft: 
                    self.player.moveLeft = True
            elif event.key == pygame.K_d:
                if not self.player.moveRight: 
                    self.player.moveRight = True
            elif event.key == pygame.K_SPACE:
                    self.player.fire = True
            elif event.key == pygame.K_b:
                    self.player.onHit(999)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.player.moveLeft = False
            elif event.key == pygame.K_d:
                self.player.moveRight = False
            elif event.key == pygame.K_SPACE:
                self.player.fire = False

    def onRender(self):
        self.game.clock.tick(60)
        self.board.onRender(self.game.screen)
        self.player.onRender(self.game.screen)
        for gameObject in self.gameObjects:
            gameObject.onRender(self.game.screen)
        for element in self.guiElements:
            element.onRender(self.game.screen)

    def onTick(self):
        if self.game.paused: return
        self.refreshAliens()
        self.updateHud()
        self.board.onTick()
        self.player.onTick()
        for gameObject in self.gameObjects:
            gameObject.onTick()