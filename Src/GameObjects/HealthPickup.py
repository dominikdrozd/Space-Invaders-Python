from Src.GameObjects.Pickup import Pickup
import pygame

class HealthPickup(Pickup):

    def __init__(self, game, position, size, speed, collision):
        super().__init__(game, position, size, speed, "Assets/health-full.png", collision)

    def onHit(self):
        self.game.scene.player.addHealth(1)
