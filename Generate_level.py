import pygame


def generateLevel(PW, PH, level, sc, color):
    x = 0
    y = 0
    for row in level:
        for cell in row:
            if cell == "-":
                pygame.draw.rect(sc, color, (x, y, PW, PH))
            x += PW
        y += PH
        x = 0
