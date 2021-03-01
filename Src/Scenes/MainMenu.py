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
            [Label((gameWidth / 2 - 250 / 2, gameHeight - 180), (250, 50), "Uruchom Grę", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 0, 0), True), "self.onPlayClick()"],
            [Label((gameWidth / 2 - 250 / 2, gameHeight - 120), (250, 50), "Opcje", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 0, 0), True), "self.onOptionsClick()"],
            [Label((gameWidth / 2 - 250 / 2, gameHeight - 60), (250, 50), "Wyjdź", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 0, 0), True), "self.onExitClick()"]
        ]

    def onPlayClick(self):
        print("Uruchamiam")

    def onOptionsClick(self):
        self.game.changeScene("Options")

    def onExitClick(self):
        self.game.quit()

    def onRender(self):
        self.background.onRender(self.game.screen)
        self.logo.onRender(self.game.screen)
        for lab in self.guiElements:
            lab[0].onRender(self.game.screen)

    def onTick(self):
        self.game.clickCooldown -= 1
        if self.game.clickCooldown > 0:
            return
        for lab, callback in self.guiElements:
            if(lab.handleHover()):
                if pygame.mouse.get_pressed()[0]:
                    if callback:
                        eval(callback)
                        self.game.clickCooldown = 10