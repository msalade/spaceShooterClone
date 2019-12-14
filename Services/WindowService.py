import pygame
from os import path

images_folder = path.join(path.dirname(__file__), '..', 'assets/images')


class WindowService:
    def __init__(self, width, height):
        self.weight = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        self.background = None

    def get__window(self):
        return self.window

    def load_background(self, image):
        self.background = pygame.image.load(path.join(images_folder, image)).convert()
        self.window.blit(pygame.transform.scale(self.background, (self.weight, self.height), self.window), (0, 0))
        pygame.display.update()

    def clean_screen(self):
        self.window.fill((0, 0, 0))

    def repaint_screen(self):
        self.window.blit(self.background, self.background.get_rect())

    def draw(self, text, color=(255, 255, 255), position=(450, 300), size=30):
        font = pygame.font.SysFont("monospace", size)
        result_text = font.render(str(text), 1, color)
        self.window.blit(result_text, position)
