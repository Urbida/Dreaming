import pygame
import asyncio
from pygame.locals import *


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(borders)
        if x1 == x2:
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

    def update(self):
        pygame.draw.rect(screen, 'BLACK', self.rect)


class Platform:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 + 1
        self.y2 = y2 + 1
        platforms.add(self)
        Border(x1, y1, x1, y2)
        Border(x1, y1, x2, y1)
        Border(x1, y2, x2, y2)
        Border(x2, y1, x2, y2)

    def update(self):
        pygame.draw.rect(screen, 'RED', (self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1))


def out():
    try:
        quit()
    except Exception as e:
        pass
    return False


def close_menu():
    return False


def button(click):
    ans = True
    for elem in buttons:
        if click[0] in range(elem[0][0], elem[0][1]) and click[1] in range(elem[1][0], elem[1][1]):
            ans = elem[2]()
    return ans


def lvl1():
    Platform(500, 1000, 620, 1020)
    Platform(430, 950, 500, 1000)


screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
platforms = set()
buttons = [
    [(780, 1140),
     (240, 380),
     out],
    [(780, 1140),
     (420, 560),
     close_menu]
]