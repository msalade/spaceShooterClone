import pygame, sys
from Services.Game_phase_service import GamePhaseService
from Entities.Enums import GameStatus
from Services.ScoreService import ScoreService


class GameEngine:
    def __init__(self):
        self.game_phase = GamePhaseService()
        self.start = False
        self.game_status = GameStatus.MAIN_MENU
        self.running = True
        self.scores = ScoreService().get_best_results()

    def start_game(self):
        self.game_phase.init_window(900, 600)
        self.game_phase.main_menu()
        self.engine()

    def clean_screen(self):
        self.game_phase.window_service.clean_screen()
        self.game_phase.window_service.repaint_screen()

    def draw(self):
        if (self.game_status != GameStatus.MAIN_MENU) and (self.game_status != GameStatus.PAUSE) and (self.game_status != GameStatus.PLAYER_DOWN):
            self.game_phase.game()
            self.clean_screen()
            self.game_phase.draw_sprites()
            self.game_phase.draw_lives()
        if self.game_phase.life() == 0 and self.game_status != GameStatus.PLAYER_DOWN:
            self.clean_screen()
            self.game_status = self.game_phase.game_over()
        if self.game_status == GameStatus.MAIN_MENU:
            self.game_phase.draw_best_results(self.scores)
        if self.game_status == GameStatus.PLAYER_DOWN:
            self.game_phase.draw_end_results(self.game_phase.score)
        pygame.display.flip()

    def pause(self):
        if (self.game_status == GameStatus.GAME_START) and (self.game_status != GameStatus.PLAYER_DOWN) and (pygame.key.get_pressed()[pygame.K_ESCAPE]):
            self.clean_screen()
            self.game_status = self.game_phase.pause()

    def play_again(self):
        if self.game_status == GameStatus.PLAYER_DOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
            self.game_phase.score = 0
            self.game_status = self.game_phase.play()
            self.game_phase.player.hide()

    def play(self):
        if (self.game_status == GameStatus.MAIN_MENU or self.game_status == GameStatus.PAUSE) and \
                pygame.key.get_pressed()[pygame.K_SPACE]:
            self.game_status = self.game_phase.play()

    def engine(self):
        while self.running:
            pygame.time.Clock().tick(60)
            self.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                self.pause()
                self.play_again()
            self.draw()
