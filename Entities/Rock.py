import pygame
from os import path
import random

images_folder = path.join(path.dirname(__file__), '..', 'assets/images')
rocks_sizes = [(40, 40), (50, 50), (70, 70), (90, 90)]


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(pygame.image.load(path.join(images_folder, 'asteroid.png')).convert(), self.get_rand_size())
        self.image_orig.set_colorkey((0, 0, 0))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 900)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(3, 10)
        self.speedx = random.randrange(-5, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.bottom > 600:
            self.kill()

    def get_rand_size(self):
        index = random.randrange(0, 3)
        return rocks_sizes[index]
