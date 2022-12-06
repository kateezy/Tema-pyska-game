import pygame

class Tema():

    def __init__(self, screen):
        """"инициализация к пушке"""
        self.screen = screen
        self.image = pygame.image.load('pyska/pixil-frame-0.png')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 10
        self.rect.y = 300
        # self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)
