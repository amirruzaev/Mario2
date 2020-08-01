import pygame
from Player import Player
from Generate_level import generateLevel

print("hello")

PW = 32
PH = 32
level = ["---------------------",
         "-           --      -",
         "-     --            -",
         "-               --  -",
         "-         ----      -",
         "- --                -",
         "-                   -",
         "-    --             -",
         "-             --    -",
         "-         -         -",
         "-            ---    -",
         "-     --            -",
         "---------------------"]
WHITE = (255, 255, 255)
GREEN = (55, 200, 0)
RED = (200, 0, 55)
FPS = 60
SIZE = (675, 415)
player = Player(50, 50)
left = False
right = False
clock = pygame.time.Clock()
sc = pygame.display.set_mode(SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False

    sc.fill(GREEN)
    generateLevel(PW, PH, level, sc, RED)

    player.update(left, right)
    player.draw(sc)
    pygame.display.update()
    clock.tick(FPS)