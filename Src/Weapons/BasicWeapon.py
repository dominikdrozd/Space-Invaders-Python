from Src.Weapons.Weapon import Weapon

class BasicWeapon(Weapon):
    
    def __init__(self):
        super().__init__(
            "Basic Gun",
            1,
            15,
            5,
            1,
            -1
        )

    def canShot(self):
        if self.bullets == 0: return False
        return True

    def upgradeWeapon(self):
        if self.upgrade_bullets >= 3: return
        self.upgrade_bullets += 1

    def degradeWeapon(self):
        if self.upgrade_bullets <= 1: return
        self.upgrade_bullets -= 1

    def upgradeWeaponSpeed(self):
        if self.speed_ratio <= 5: return
        self.speed_ratio -= 2

    def degradeWeaponSpeed(self):
        if self.speed_ratio >= 30: return
        self.speed_ratio += 2
        
    def onShot(self, player):
        if not self.canShot(): return
        bulletX = player.position[0] + player.size[0] / 2 - 2
        bulletY = player.position[1] + 2
        if (self.upgrade_bullets == 1):
            self.bullets -= 1
            player.game.scene.createBullet((bulletX, bulletY), (0, -1), ["Alien"], self.bullet_speed)
        elif (self.upgrade_bullets == 2):
            self.bullets -= 2
            player.game.scene.createBullet((bulletX - 8, bulletY), (0, -1), ["Alien"], self.bullet_speed)
            player.game.scene.createBullet((bulletX + 8, bulletY), (0, -1), ["Alien"], self.bullet_speed)
        elif (self.upgrade_bullets == 3):
            self.bullets -= 3
            player.game.scene.createBullet((bulletX - 8, bulletY), (-0.2, -1), ["Alien"], self.bullet_speed)
            player.game.scene.createBullet((bulletX, bulletY), (0, -1), ["Alien"], self.bullet_speed)
            player.game.scene.createBullet((bulletX + 8, bulletY), (0.2, -1), ["Alien"], self.bullet_speed)