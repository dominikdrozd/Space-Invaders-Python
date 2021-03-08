from Src.GameObjects.GameObject import GameObject
import pygame

class Player(GameObject):

    def __init__(self, game, position: tuple, size: tuple, texture: str, collision: bool):
        super().__init__(game, position, size, texture, collision)
        self.moveLeft = False
        self.moveRight = False
        self.health = 6
        self.points = 0
        self.level = 0
        self.money = 0
        self.fire = False
        self.onFire = pygame.mixer.Sound("Assets/shot.mp3")
        self.onFire.set_volume(0.1)
        self.shotCooldown = 0
        self.speed = 8

    def onHit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.game.changeScene("EndGame")

    def onTick(self):
        if self.moveLeft and self.position[0] > 256:
            self.move((-self.speed, 0))
        if self.moveRight and self.position[0] < 800 - 64:
            self.move((self.speed, 0))
        if self.fire and not self.shotCooldown:
            self.shotCooldown = 5
            self.onFire.play()
            bulletX = self.position[0] + self.size[0] / 2 - 2
            bulletY = self.position[1] + 2
            self.game.scene.createBullet((bulletX, bulletY), -1, ["Alien"])
        if self.shotCooldown > 0: self.shotCooldown -= 1
        return

    def onRender(self, surface: pygame.Surface):
        surface.blit(self.objectTexture, self.position)
    
    def onDestroy(self):
        pass