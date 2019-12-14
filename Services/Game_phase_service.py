from Services.SoundService import SoundService
from Services.WindowService import WindowService
from Entities.Enums import GameStatus
from Entities.Player import Player
from Entities.Rock import Rock
from Entities.UFO import UFO
from Services.ScoreService import ScoreService
import pygame


class GamePhaseService:
    def __init__(self):
        pygame.font.init()
        self.score = 0
        self.window_service = None
        self.sprites = pygame.sprite.Group()
        self.player = None
        self.ufo = None
        self.rocks = pygame.sprite.Group()
        self.rocks_bullets_colision = None
        self.laser_player_colision = None
        self.ufo_bullets_colision = None
        self.sound_service = SoundService()

    def init_window(self, width, height):
        self.window_service = WindowService(width, height)

    def main_menu(self):
        if self.player is not None:
            self.player.delete()
        self.sound_service.play_soundtrack('menu_soundtrack.ogg')
        self.window_service.load_background('menu.jpg')
        return GameStatus.MAIN_MENU

    def pause(self):
        self.sound_service.play_soundtrack('menu_soundtrack.ogg')
        self.window_service.load_background('pause.jpg')
        return GameStatus.PAUSE

    def play(self):
        if self.player is None:
            self.score = 0
            self.player = Player(self.sprites)
            self.sprites.add(self.player)
            self.draw_score()
        self.sound_service.play_soundtrack('game_soundtrack.ogg')
        self.window_service.load_background('space.jpg')
        return GameStatus.GAME_START

    def game(self):
        self.generate_rocks()
        self.generate_ufo()
        self.rocks_player_colision = pygame.sprite.spritecollide(self.player, self.rocks, True, pygame.sprite.collide_circle)
        self.rocks_bullets_colision = pygame.sprite.groupcollide(self.rocks, self.player.bullets(), True, True)
        self.player_rocks_events()
        self.rocks_players_bullets_events()

        if self.ufo is not None:
            self.ufo_bullets_colision = pygame.sprite.spritecollide(self.ufo, self.player.bullets(), True, pygame.sprite.collide_circle)
            self.laser_player_colision = pygame.sprite.spritecollide(self.player, self.ufo.laser_group(), True)
            self.ufo_bullets_events()
            self.player_ufo_lasers_events()

    def generate_rocks(self):
        if self.rocks.__len__() < 10:
            for i in range(2):
                self.new_rock()

    def generate_ufo(self):
        if self.ufo is None and self.score % 20 == 0:
            self.ufo = UFO(self.sprites)
            self.sprites.add(self.ufo)

    def player_rocks_events(self):
        for hit in self.rocks_player_colision:
            self.player_hit()

    def rocks_players_bullets_events(self):
        for hit in self.rocks_bullets_colision.items():
            self.sound_service.play_sound('expl6.wav')
            self.score += 1
            self.new_rock()

    def player_ufo_lasers_events(self):
        for hit in self.laser_player_colision:
            self.player_hit()

    def player_hit(self):
        if self.player.lives >= 1:
            self.sound_service.play_sound('expl3.wav')
            self.player.hit()

    def ufo_bullets_events(self):
        for hit in self.ufo_bullets_colision:
            self.sound_service.play_sound('expl6.wav')
            self.score += 4
            self.ufo.kill()
            self.ufo = None

    def game_over(self):
        if self.ufo is not None:
            self.ufo.kill()
            self.ufo = None
        ScoreService().save_best_result(self.score)
        self.sound_service.play_soundtrack('menu_soundtrack.ogg')
        self.window_service.load_background('game_over.jpg')
        return GameStatus.PLAYER_DOWN

    def draw_sprites(self):
        self.sprites.update()
        self.sprites.draw(self.window_service.get__window())
        self.draw_score()

    def new_rock(self):
        rock = Rock()
        self.sprites.add(rock)
        self.rocks.add(rock)

    def life(self):
        if self.player is not None:
            return self.player.lives

    def draw_score(self):
        self.window_service.draw(self.score, (255, 255, 255), (450, 10), 40)

    def draw_lives(self):
        self.window_service.draw("Life:" + str(self.player.lives), (255, 0, 0), (50, 10), 40)

    def draw_best_results(self, results):
        self.window_service.draw("Best result:", (255, 2, 2), (350, 300))
        self.window_service.draw(results, (255, 2, 2), (450, 330))

    def draw_end_results(self, results):
        self.window_service.draw(results, (255, 2, 2), (450, 330))
