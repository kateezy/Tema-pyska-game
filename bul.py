import pygame

class Bul(pygame.sprite.Sprite):

    def __init__(self, screen, tema):
        super(Bul, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 1, 7, 16)
        self.colors = 84, 255, 159
        self.speed = 1.5
        self.rect.centerx = tema.rect.centerx
        self.rect.top = tema.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colors, self.rect)