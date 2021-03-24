from Src.GameObjects.Pickup import Pickup
import pygame

class WeaponUpgradePickup(Pickup):

    def __init__(self, game, position, size, speed, collision):
        super().__init__(game, position, size, speed, "Assets/bullet+.png", collision)

    def onHit(self):
        self.game.scene.player.weapon.upgradeWeapon()