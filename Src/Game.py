from Src.Scenes.MainMenu import MainMenu
from Src.Scenes.Options import Options
from Src.Scenes.InGame import InGame
from Src.Scenes.EndGame import EndGame
import pygame

class Game(object):

    def __init__(self):
        pygame.init()
        self.windowSize = (800, 600)
        self.fullscreen = True
        self.title = "Space Invaders"
        self.clock = pygame.time.Clock()
        self.paused = True
        self.pauseTime = 0
        self.version = 0.1
        self.scene = MainMenu(self)
        pygame.display.set_caption(self.title)

    def changeScene(self, scene):
        if scene == "Options":
            self.paused = True
            self.scene = Options(self)
        elif scene == "MainMenu":
            self.paused = True
            self.scene = MainMenu(self)
        elif scene == "InGame":
            self.paused = False
            self.scene = InGame(self)
        elif scene == "EndGame":
            self.paused = True
            player = self.scene.player
            self.scene = EndGame(self, player)

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
                self.scene.eventHandle(event)
            self.screen.fill(pygame.Color(0, 0, 0))
            self.scene.onTick()
            self.scene.onRender()
            pygame.display.update()
