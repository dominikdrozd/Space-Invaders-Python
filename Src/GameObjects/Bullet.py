from Src.GameObjects.GameObject import GameObject
import pygame

class Bullet(GameObject):

    def __init__(self, game, position: tuple, size: tuple, texture: str, collision: bool):
        super().__init__(game, position, size, texture, collision)
        self.moveLeft = False
        self.moveRight = False
        self.fire = False
        self.bulletSound = pygame.mixer.Sound("Assets/explosion.mp3")
        self.speed = 8

    def onTick(self):
        if self.position[1] <= 32 + 8: self.onDestroy()
        self.move((0, -self.speed))

    def onRender(self, surface: pygame.Surface):
        surface.blit(self.objectTexture, self.position)
    
    def onDestroy(self):
        self.bulletSound.set_volume(0.1)
        self.bulletSound.play()
        self.game.scene.destroyObject(self)