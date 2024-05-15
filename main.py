import asyncio

import pygame

from pause_menu import pause_menu
from Player import Player
from FCL import *


async def main():
    pygame.init()
    player = Player()
    clock = pygame.time.Clock()
    width = 1920
    height = 1080
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
    lvl1()
    ml = False
    mr = False
    position_of_mouse = (-30, -30)
    while True:
        pygame.mouse.set_visible(False)
        screen.fill((0, 0, 70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu()
                if event.key == pygame.K_a:
                    ml = True
                if event.key == pygame.K_d:
                    mr = True
                if event.key == pygame.K_SPACE and player.on_ground:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    ml = False
                if event.key == pygame.K_d:
                    mr = False
            if event.type == pygame.MOUSEMOTION:
                position_of_mouse = event.pos
        im = pygame.image.load(r'data\textures\mouse.png').convert_alpha()
        screen.blit(im, position_of_mouse)
        if ml:
            player.move('LEFT')
        if mr:
            player.move('RIGHT')
        for elem in platforms:
            elem.update()
        for elem in borders:
            elem.update()
        player.update()
        pygame.display.flip()
        clock.tick(90)


if __name__ == '__main__':
    asyncio.run(main())
