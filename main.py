import pygame, control
from tema import Tema
from pygame.sprite import Group
def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("傻瓜主題")
    # image = pygame.image.load('pyska/background.png')
    colors = (45, 0, 100)
    tema = Tema(screen)
    bullets = Group()


    while True:
        control.events(screen, tema, bullets)
        tema.update_tema()
        bullets.update()
        control.update(colors, screen, tema, bullets)


run()