import pygame, sys
from bul import Bul

def events(screen, tema, bullets):
    """обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                tema.mright = True
            elif event.key == pygame.K_a:
                tema.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bul(screen, tema)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                tema.mright = False
            elif event.key == pygame.K_a:
                tema.mleft = False

def update(colors, screen, tema, bullet):
    screen.fill(colors)
    for bul in bullet.sprites():
        bul.draw_bullet()
    tema.output()
    pygame.display.flip()









































































# import pygame, sys
#
# def events(tema):
#     """обработка событий"""
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_s:
#                     tema.mright = True
#             elif event.key == pygame.K_w:
#                     tema.mtop = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_s:
#                 tema.mbottom = False
#             elif event.key == pygame.K_w:
#                 tema.mtop = False
#                 # tema.rect.centerx += 1