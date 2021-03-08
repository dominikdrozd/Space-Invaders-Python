class Weapon(object):
    
    def __init__(self, name, damage, speed_ratio, bullet_speed, upgrade_bullets=1, bullets=-1):
        self.name = name
        self.damage = damage
        self.speed_ratio = speed_ratio
        self.bullet_speed = bullet_speed
        self.upgrade_bullets = upgrade_bullets
        self.bullets = bullets
