from Src.GameObjects.GameObject import GameObject
import pygame
import random

class Alien(GameObject):

    speed: int
    side: int

    def __init__(self, game, position: tuple, size: tuple, texture: str, collision: bool):
        super().__init__(game, position, size, texture, collision)
        self.speed = 4
        self.side = 1

    def onTick(self):
        rng = random.randrange(1000)
        if rng < 1:
            self.game.scene.createBullet(self.position, (0, 1), ["Player"], 2)
        if self.game.scene.player.isCollided(self):
            self.onDestroy()
            self.game.scene.player.onHit(1)
            return
        x = self.position[0] + self.speed * self.side
        if x > 800 - 64:
            self.side = -1
            y = self.position[1] + 32
        elif x < 256:
            self.side = 1
            y = self.position[1] + 32            
        else:
            y = self.position[1]
        self.position = (x, y)

    def onRender(self, surface: pygame.Surface):
        surface.blit(self.object_texture, self.position)
    
    def onDestroy(self):
        self.game.scene.destroyObject(self)
        self.game.scene.createPickup(self.position, 2)