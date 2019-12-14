import pygame
from os import path

sound_folder = path.join(path.dirname(__file__), '..', 'assets/sounds')


class SoundService:
    def __init__(self):
        self.soundtrack = None
        pygame.mixer.init()

    def play_soundtrack(self, file):
        sound_path = path.join(sound_folder, file)
        self.soundtrack = pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(-1)

    def stop_soundtrack(self):
        pygame.mixer.music.stop()

    def play_sound(self, file):
        pygame.mixer.Sound(path.join(sound_folder, file)).play()
