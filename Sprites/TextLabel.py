import pygame
from Colors import Colors
from Label import Label


class TextLabel(Label):

    def __init__(self, position, dims, color=Colors.WHITE, font=(None, 50)):
        super().__init__(position, dims)
        self.font = pygame.font.Font(*font)
        self.color = color

    def write(self, text) -> None:
        self.set_image(self.font.render(text, True, self.color), transform=False)
