from Src.Scenes.Scene import Scene
from Src.Gui.Label import Label
from Src.Gui.Image import Image
import pygame

class MainMenu(Scene):

    def __init__(self, game):
        super().__init__(game)
        gameWidth, gameHeight = self.game.windowSize
        self.background = Image((0, 0), self.game.windowSize, "Assets/menu-background.png")
        self.logo = Image((gameWidth / 2 - 800 / 2, 10), (800, 120), "Assets/menu-logo.png")
        self.guiElements = [
            [Label((gameWidth / 2 - 250 / 2, gameHeight - 180), (250, 55), "Start", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (25, 25, 25), True), "self.onPlayClick()"],
            [Label((gameWidth / 2 - 250 / 2, gameHeight - 120), (250, 55), "Ranking", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (25, 25, 25), True), "self.onOptionsClick()"],
            [Label((gameWidth / 2 - 250 / 2, gameHeight - 60), (250, 55), "Wyjdź", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (25, 25, 25), True), "self.onExitClick()"],
            [Label((gameWidth - 50, gameHeight - 16), (50, 16), "Alpha v{0}".format(self.game.version), (0, 0), (255, 255, 255), None, 10, None, None, True), None],
            [Label((5, gameHeight - 60), (125, 55), "Wyłącz muzykę", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 0, 0), True), "self.onMuteClick()"]
        ]

    def onPlayClick(self):
        self.game.changeScene("InGame")

    def onOptionsClick(self):
        self.game.changeScene("Options")

    def onExitClick(self):
        self.game.quit()

    def onMuteClick(self):
        if self.guiElements[4][0].text == "Wyłącz muzykę":
            self.guiElements[4][0].text = "Włącz muzykę"
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
            self.guiElements[4][0].text = "Wyłącz muzykę"

    def eventHandle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for element in self.guiElements:
                    if element[0].handleHover():
                        if element[1]: eval(element[1])

    def onRender(self):
        self.game.clock.tick(60)
        self.background.onRender(self.game.screen)
        self.logo.onRender(self.game.screen)
        for element in self.guiElements:
            element[0].onRender(self.game.screen)

    def onTick(self):
        pass