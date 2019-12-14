import pygame
from os import path
from Entities.Laser import Laser

images_folder = path.join(path.dirname(__file__), '..', 'assets/images')


class UFO(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.lazer_groupe = pygame.sprite.Group()
        spaceship = pygame.image.load(path.join(images_folder, 'ufo.png')).convert()
        self.image = pygame.transform.scale(spaceship, (60, 70))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 450
        self.rect.bottom = 30
        self.speedx = -5
        self.speedy = 1
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 500
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        self.shoot()
        self.moves_patter()

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.bottom > 600:
            self.kill()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            laser = Laser(self.rect.centerx, self.rect.bottom)
            self.lazer_groupe.add(laser)
            self.all_sprites.add(laser)

    def laser_group(self):
        return self.lazer_groupe

    def moves_patter(self):
        if self.rect.x == 870:
            self.speedx = -5
        if self.rect.x == 10:
            self.speedx = 5
