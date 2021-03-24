from Src.GameObjects.GameObject import GameObject
import pygame

class Pickup(GameObject):

    def __init__(self, game, position, size, speed, texture, collision):
        super().__init__(game, position, size, texture, collision)
        self.on_hit_sound = pygame.mixer.Sound("Assets/pickup.mp3")
        self.speed = speed

    def onTick(self):
        if self.position[1] > 600 - 48:
            self.onDestroy(True)
        self.move((0, self.speed))
        if self.game.scene.player.isCollided(self):
            self.onHit()
            self.onDestroy()

    def onHit(self):
        pass
    
    def onRender(self, surface: pygame.Surface):
        surface.blit(self.object_texture, self.position)

    def onDestroy(self, muted=False):
        if not muted:
            self.on_hit_sound.set_volume(0.1)
            self.on_hit_sound.play()
        self.game.scene.destroyObject(self)