from Src.Scenes.Scene import Scene
from Src.Gui.Label import Label
import pygame

class Options(Scene):

    def __init__(self, game):
        super().__init__(game)
        gameHeight = self.game.windowSize[1]
        self.guiElements = [
            [Label((10, gameHeight - 120), (250, 50), "WORK IN PROGRESS", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 0, 0), True), None],
            [Label((10, gameHeight - 60), (250, 50), "Powrót", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 0, 0), True), "self.onBackClick()"]
        ]

    def onPlayClick(self):
        print("Uruchamiam")

    def onOptionsClick(self):
        print("Opcje")

    def onBackClick(self):
        self.game.changeScene("MainMenu")

    def eventHandle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event)
                for element in self.guiElements:
                    if element[0].handleHover():
                        if element[1]: eval(element[1])

    def onRender(self):
        for lab in self.guiElements:
            lab[0].onRender(self.game.screen)

    def onTick(self):
        pass