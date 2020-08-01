import pygame
WIDTH = 20
HEIGHT = 20
COLOR = (0, 255, 0)
SPEED = 5


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(COLOR)
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right):
        if left:
            self.xvel = -SPEED
        if right:
            self.xvel = SPEED
        if not left and not right:
            self.xvel = 0
        self.rect.x += self.xvel

    def draw(self, sc):
        sc.blit(self.image, (self.rect.x, self.rect.y))