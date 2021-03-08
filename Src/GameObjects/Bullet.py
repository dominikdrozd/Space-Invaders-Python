from Src.GameObjects.GameObject import GameObject
from Src.GameObjects.Alien import Alien
import pygame

class Bullet(GameObject):

    def __init__(self, game, position: tuple, size: tuple, speed: float, texture: str, collision: bool, side: tuple, collisionWith):
        super().__init__(game, position, size, texture, collision)
        self.side = side
        self.bulletSound = pygame.mixer.Sound("Assets/explosion.mp3")
        self.collisionWith = collisionWith
        self.speed = speed

    def onTick(self):
        try:
            if "Player" in self.collisionWith and self.isCollided(self.game.scene.player):
                self.onDestroy()
                self.game.scene.player.onHit(1)
            for alien in self.game.scene.gameObjects:
                if self.isCollided(alien) and alien.__class__.__name__ in self.collisionWith:
                    self.game.scene.player.points += 1
                    self.onDestroy()
                    alien.onDestroy()
            if self.position[1] <= 32 + 8:
                self.onDestroy(True)
            if self.position[1] > 600 - 48:
                self.onDestroy(True)
            if self.position[0] < self.game.scene.boardPosX + 10:
                self.onDestroy(True)
            if self.position[0] > self.game.scene.boardPosX + self.game.scene.boardWidth - 10:
                self.onDestroy(True)
            self.move((self.speed * self.side[0], self.speed * self.side[1]))
        except(Exception):
            pass

    def onRender(self, surface: pygame.Surface):
        surface.blit(self.objectTexture, self.position)
    
    def onDestroy(self, muted=False):
        if not muted:
            self.bulletSound.set_volume(0.1)
            self.bulletSound.play()
        self.game.scene.destroyObject(self)