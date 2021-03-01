class GameObject(object):

    position: tuple
    size: tuple
    texture: str
    collision: bool

    def __init__(self, position: tuple, size: tuple, texture: str, collision: bool):
        self.position = position
        self.size = size
        self.texture = texture
        self.collision = collision

    def handleCollision(self, otherObject: 'GameObject'):
        if not self.collision: return self.collision
        return (
            self.position[0] < otherObject.position[0] + otherObject.size[0] and
            self.position[0] + self.size[0] > otherObject.position[0] and
            self.position[1] < otherObject.position[1] + otherObject.size[1] and
            self.position[1] + self.size[1] > otherObject.position[1]
        )