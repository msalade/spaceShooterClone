import pygame
from os import path

images_folder = path.join(path.dirname(__file__), '..', 'assets/images')


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(path.join(images_folder, 'laser.png')), (15, 40))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -8

    def update(self):
        self.rect.y -= self.speedy

        if self.rect.bottom > 600:
            self.kill()
