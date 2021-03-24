import pygame

class GameObject(object):

    position: tuple
    size: tuple
    texture: str
    collision: bool

    def __init__(self, game, position: tuple, size: tuple, texture: str, collision: bool):
        self.game = game
        self.position = position
        self.size = size
        self.texture = texture
        object_texture = pygame.image.load(self.texture)
        self.object_texture = pygame.transform.scale(object_texture, size)
        self.collision = collision

    def move(self, pos):
        x = self.position[0] + pos[0]
        y = self.position[1] + pos[1]
        self.position = (x, y)

    def isCollided(self, otherObject: 'GameObject'):
        if not self.collision: return False
        return (
            self.position[0] < otherObject.position[0] + otherObject.size[0] and
            self.position[0] + self.size[0] > otherObject.position[0] and
            self.position[1] < otherObject.position[1] + otherObject.size[1] and
            self.position[1] + self.size[1] > otherObject.position[1]
        )