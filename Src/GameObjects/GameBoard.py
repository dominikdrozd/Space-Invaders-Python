from Src.GameObjects.GameObject import GameObject
import pygame

class GameBoard(GameObject):

    def __init__(self, game, position: tuple, size: tuple, texture: str, collision: bool):
        super().__init__(game, position, size, texture, collision)
        self.moveLeft = False
        self.moveRight = False

    def onTick(self):
        return

    def onRender(self, surface: pygame.Surface):
        x, y = self.position
        width, height = self.size
        surface.blit(self.objectTexture, self.position)
        pygame.draw.line(surface, (125, 125, 125), (x, y), (x + width, y))
        pygame.draw.line(surface, (125, 125, 125), (x, y), (x, y + height))
        pygame.draw.line(surface, (125, 125, 125), (x + width, y), (x + width, y + height))
        pygame.draw.line(surface, (125, 125, 125), (x, y + height), (x + width, y + height))
    
    def onDestroy(self):
        pass