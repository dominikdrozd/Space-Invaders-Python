from Src.Scenes.Scene import Scene
from Src.Gui.Label import Label
import os
import pygame

class EndGame(Scene):

    def __init__(self, game, player):
        super().__init__(game)
        self.player = player
        self.results = []
        self.gameWidth, self.gameHeight = self.game.windowSize
        self.guiElements = [
            [Label((260, self.gameHeight - 60), (280, 55), "", (15, 15), (255, 255, 255), None, 15, (25, 25, 25), None, True), None],
            [Label((260, self.gameHeight - 95), (280, 25), "Pseudonim:", (5, 12), (255, 255, 255), (255, 255, 255), 15, None, None, False), None],
            [Label((0, 0), (self.gameWidth, 65), "Koniec Gry", (15, 15), (0, 0, 0), None, 54, (255, 255, 255), None, True), None],
            [Label((self.gameWidth / 2 - 250 / 2, 120), (250, 55), "Punkty: {0}".format(self.player.points), (0, 0), (255, 255, 255), None, 22, None, None, True), None],     
            [Label((0, 180), (self.gameWidth, 60), "Top 10", (15, 15), (0, 0, 0), None, 54, (255, 255, 255), None, True), None],                   
            [Label((self.gameWidth - 255, self.gameHeight - 60), (250, 55), "Zapisz Wynik", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (25, 25, 25), True), "self.onSaveClick()"],
            [Label((5, self.gameHeight - 60), (250, 55), "Wyjdź", (15, 15), (0, 0, 0), (255, 255, 255), 15, (255, 255, 255), (25, 25, 25), True), "self.onBackClick()"]
        ]
        self.loadRecords()
        print(self.results)
        self.getRecord()
        #self.addResult()

    def getRecord(self):
        if len(self.results) <= 0:
            return

        self.results.sort(key = lambda x: x[1])
        
        if self.player.points > int(self.results[0][1]):
            self.guiElements.append([Label((0, 65), (self.gameWidth, 50), "NOWY REKORD", (15, 15), (255, 255, 255), None, 22, (85, 0, 0), None, True), None])

        try:
            for i in range(10):
                self.guiElements.append(
                    [Label((self.gameWidth / 2 - 350 / 2, 240 + i * 20), (350, 55), "{0}. {1} {2}".format(i, str(self.results[i][0]), int(self.results[i][1])), (15, 15), (255, 255, 255), None, 15, None, None, False), None],
                )
        except(Exception):
            pass

    def loadRecords(self):
        with open(os.getcwd() + "\\results.txt") as results:
            lines = results.readlines()
            for line in lines:
                result = line.split("|")
                self.results.append(result)

    def onBackClick(self):
        self.game.changeScene("MainMenu")

    def onSaveClick(self):
        if len(self.guiElements[0][0].text) <= 0:
            return
        with open(os.getcwd() + "\\results.txt", "a") as results:
            results.write("{0}|{1}\n".format(self.guiElements[0][0].text, self.player.points))
        self.onBackClick()

    def eventHandle(self, event):
        buttons = {
            pygame.K_a : "a",
            pygame.K_b : "b",
            pygame.K_c : "c",
            pygame.K_d : "d",
            pygame.K_e : "e",
            pygame.K_f : "f",
            pygame.K_g : "g",
            pygame.K_h : "h",
            pygame.K_i : "i",
            pygame.K_j : "j",
            pygame.K_k : "k",
            pygame.K_l : "l",
            pygame.K_m : "m",
            pygame.K_n : "n",
            pygame.K_o : "o",
            pygame.K_p : "p",
            pygame.K_q : "q",
            pygame.K_r : "r",
            pygame.K_s : "s",
            pygame.K_t : "t",
            pygame.K_u : "u",
            pygame.K_v : "v",
            pygame.K_w : "w",
            pygame.K_x : "x",
            pygame.K_y : "y",
            pygame.K_z : "z",
            pygame.K_SPACE : " "
        }
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.guiElements[0][0].text = self.guiElements[0][0].text[:-1]
            if event.key in buttons:
                if len(self.guiElements[0][0].text) <= 0:
                    self.guiElements[0][0].text = self.guiElements[0][0].text + buttons[event.key].upper()
                else:
                    self.guiElements[0][0].text = self.guiElements[0][0].text + buttons[event.key] 
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