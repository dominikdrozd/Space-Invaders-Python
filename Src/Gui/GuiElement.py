class GuiElement(object):

    position: tuple
    size: tuple

    def __init__(self, position: tuple, size: tuple):
        self.position = position
        self.size = size

    