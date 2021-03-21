from Src.Scenes.Scene import Scene
from Src.Gui.Label import Label
import os
import pygame

class Options(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.gameWidth, self.gameHeight = self.game.windowSize
        self.results = []
        self.offset = 0
        self.perPage = 22
        self.guiElements = [
            [Label((0, 0), (self.gameWidth, 65), "Ranking", (15, 15), (0, 0, 0), None, 54, (255, 255, 255), None, True), None],
            [Label((10, self.gameHeight - 60), (250, 50), "Powrót", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 0, 0), True), "self.onBackClick()"]
        ]
        self.resultsGui = []
        self.loadRecords()
        self.getRecord()

    def loadRecords(self):
        with open(os.getcwd() + "\\results.txt") as results:
            lines = results.readlines()
            for line in lines:
                result = line.split("|")
                self.results.append(result)

    def getRecord(self):
        self.results.sort(key = lambda x: int(x[1]), reverse=True)
        try:
            offset = 0
            for i in range(len(self.results)):
                if i % 2:
                    self.resultsGui.append(
                        Label((50 / 2, 80 + (i % self.perPage) * 20), (750, 20), "{0}. {1} ({2})".format(i+1, str(self.results[i][0]), int(self.results[i][1])), (0, 0), (255, 255, 255), (255, 255, 255), 15, (0, 0, 0), (85, 15, 15), False)
                    )
                else:
                    self.resultsGui.append(
                        Label((50 / 2, 80 + (i % self.perPage) * 20), (750, 20), "{0}. {1} ({2})".format(i+1, str(self.results[i][0]), int(self.results[i][1])), (0, 0), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (85, 15, 15), False)   
                    )                    
        except(Exception):
            pass

    def onBackClick(self):
        self.game.changeScene("MainMenu")

    def eventHandle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for element in self.guiElements:
                    if element[0].handleHover():
                        if element[1]: eval(element[1])
            if event.button == 4:
                if(self.offset <= 0):
                    return
                self.offset -= 1
            if event.button == 5:
                if(self.offset * self.perPage + self.perPage >= len(self.resultsGui)):
                    return
                self.offset += 1

    def onRender(self):
        for lab in self.guiElements:
            lab[0].onRender(self.game.screen)
        try:
            for i in range(self.offset * self.perPage - self.offset, self.offset * self.perPage + self.perPage):
                print(i)
                self.resultsGui[i+self.offset].onRender(self.game.screen)
        except(Exception):
            pass
        
    def onTick(self):
        pass