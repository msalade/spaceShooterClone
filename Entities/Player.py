import pygame
from os import path
from Entities.Bullet import Bullet
from Services.SoundService import SoundService

images_folder = path.join(path.dirname(__file__), '..', 'assets/images')


class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.bullets_group = pygame.sprite.Group()
        spaceship = pygame.image.load(path.join(images_folder, 'rocket.png')).convert()
        self.image = pygame.transform.scale(spaceship, (40, 70))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 450
        self.rect.bottom = 570
        self.speedx = 0
        self.speedy = 0
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 250
        self.lives = 3

    def update(self):
        self.speedx = 0
        self.speedy = 0

        self.control()
        self.moves_limit()

        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def control(self):
        current_key = pygame.key.get_pressed()
        if current_key[pygame.K_LEFT]:
            self.speedx = -10
        elif current_key[pygame.K_RIGHT]:
            self.speedx = 10
        elif current_key[pygame.K_UP]:
            self.speedy = -10
        elif current_key[pygame.K_DOWN]:
            self.speedy = 10

        if current_key[pygame.K_SPACE]:
            self.shoot()

    def moves_limit(self):
        if self.rect.right > 900:
            self.rect.right = 900
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > 600:
            self.rect.bottom = 600
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.all_sprites.add(bullet)
            self.bullets_group.add(bullet)
            SoundService().play_sound('pew.wav')

    def bullets(self):
        return self.bullets_group

    def delete(self):
        self.kill()

    def hide(self):
        self.lives = 3
        self.rect.center = (450, 550)

    def hit(self):
        self.lives -= 1
