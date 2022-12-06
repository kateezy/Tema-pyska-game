import pygame
import sys
from tema import Tema

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("傻瓜主題")
    rgb = (45, 0, 100)
    tema = Tema(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(rgb)
        tema.output()
        pygame.display.flip()
run()