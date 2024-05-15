from FCL import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.x = 920
        self.y = 1000
        self.rect = pygame.Rect(self.x, self.y, 80, 140)
        self.last_vector = 'DOWN'
        self.on_ground = False
        self.rotation = 'RIGHT'
        self.jump_tick = 0

    def move(self, vector):
        if vector == 'UP':
            self.rect.y -= 14
        elif vector == 'DOWN':
            self.rect.y += 4
        elif vector == 'LEFT':
            self.rotation = 'LEFT'
            self.rect.x -= 8
        elif vector == 'RIGHT':
            self.rotation = 'RIGHT'
            self.rect.x += 8
        self.last_vector = vector
        self.check()

    def update(self):
        im = pygame.image.load(r'data\textures\mainhero.png').convert_alpha()
        im = pygame.transform.scale(im, (80, 140))
        if self.rotation == 'LEFT':
            im = pygame.transform.flip(im, 1, 0)
        if self.jump_tick:
            self.jump_tick -= 1
            self.move('UP')
        self.move('DOWN')
        screen.blit(im, self.rect)

    def check(self):
        while pygame.sprite.spritecollideany(self, borders):
            if self.last_vector == 'LEFT':
                self.rect.x += 1
            if self.last_vector == 'RIGHT':
                self.rect.x -= 1
            if self.last_vector == 'UP':
                self.rect.y += 1
            if self.last_vector == 'DOWN':
                self.on_ground = True
                self.rect.y -= 1

    def jump(self):
        self.on_ground = False
        self.jump_tick = 14

