from Src.GameObjects.GameObject import GameObject
from Src.Gui.GuiElement import GuiElement
from Src.Gui.Label import Label
from Src.Scenes.MainMenu import MainMenu
from Src.Scenes.Options import Options
import pygame

class Game(object):

    def __init__(self):
        pygame.init()
        self.windowSize = (800, 600)
        self.fullscreen = True
        self.title = "Space Invaders"
        self.clock = pygame.time.Clock()
        self.clickCooldown = 0
        self.scene = MainMenu(self)
        pygame.display.set_caption(self.title)

    def changeScene(self, scene):
        if scene == "Options":
            self.scene = Options(self)
        elif scene == "MainMenu":
            self.scene = MainMenu(self)

    def quit(self):
        self.inGame = False
        pygame.quit()
        exit(0)

    def run(self):
        self.screen = pygame.display.set_mode(self.windowSize, pygame.DOUBLEBUF)
        self.inGame = True
        while self.inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.inGame = False
            self.clock.tick(30)
            self.screen.fill(pygame.Color(0, 0, 0))
            self.scene.onTick()
            self.scene.onRender()
            pygame.display.update()
            