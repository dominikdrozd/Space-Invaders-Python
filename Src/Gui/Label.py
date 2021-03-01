from Src.Gui.GuiElement import GuiElement
import pygame

class Label(GuiElement):

    def __init__(self, position: tuple, size: tuple, text: str, padding: tuple, color: tuple, hoverColor: tuple, fontSize: int, background: tuple, hoverBackground: tuple, center: bool=False):
        super().__init__(position, size)
        self.text = text
        self.padding = padding
        self.color = [color, hoverColor]
        self.fontSize = fontSize
        self.background = [background, hoverBackground]
        self.center = center
    
    def renderFont(self):
        font = pygame.font.SysFont("Arial", self.fontSize)
        render = font.render(self.text, True, self.getColor(), None)
        return render

    def getTextPosition(self, fontRender):
        if self.center:
            textX, textY = fontRender.get_size()
            x = self.position[0] + (self.size[0] / 2) - (textX / 2)
            y = self.position[1] + (self.size[1] / 2) - (textY / 2)
            return (x, y)
        x = self.position[0] + self.padding[0]
        y = self.position[1] + self.padding[1]
        return (x, y)

    def handleHover(self):
        mousePosition = pygame.mouse.get_pos()
        return (
            self.position[0] < mousePosition[0] + 1 and
            self.position[0] + self.size[0] > mousePosition[0] and
            self.position[1] < mousePosition[1] + 1 and
            self.position[1] + self.size[1] > mousePosition[1]
        )

    def onTick(self):
        pass

    def getBackground(self):
        if not self.background[1]:
            return self.background[0]
        return self.background[int(self.handleHover())]

    def getColor(self):
        if not self.color[1]:
            return self.color[0]
        return self.color[int(self.handleHover())]

    def onRender(self, screen):
        fontRender = self.renderFont()
        if self.background[0]:
            pygame.draw.rect(screen, self.getBackground(), (self.position + self.size))
        screen.blit(fontRender, (self.getTextPosition(fontRender) + self.size))