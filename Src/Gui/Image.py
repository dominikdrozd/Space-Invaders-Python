from Src.Gui.GuiElement import GuiElement
import pygame

class Image(GuiElement):

    def __init__(self, position: tuple, size: tuple, image: str):
        super().__init__(position, size)
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, self.size)

    def onRender(self, screen):
        screen.blit(self.image, (self.position + self.size))