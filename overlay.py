import pygame
import game
import abilities
import bullet


class Overlay:

    @staticmethod
    def draw_text(window, text, size, x, y, color):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        window.blit(text_surface, text_rect)

    @staticmethod
    def draw_info(game_window):
        #game info
        Overlay.draw_text(game_window.window, str(game_window.score), 40, game.Game.screen_width / 2, 20, (0, 0, 0))
        Overlay.draw_text(game_window.window, "Health: " + str(game_window.player.health), 40, 120, 10, (0, 0, 0))
        #shield
        if game_window.player.shield > 0:
            Overlay.draw_text(game_window.window, "Shield", 40, 120, 50, (255, 0, 0))
        elif abilities.Abilities.is_shield_available:
            Overlay.draw_text(game_window.window, "Shield", 40, 120, 50, (0, 255, 0))
        else:
            Overlay.draw_text(game_window.window, "Shield", 40, 120, 50, (140, 140, 140))
        #power bullet
        if bullet.Bullet.is_next_power_bullet:
            Overlay.draw_text(game_window.window, "Power bullet", 40, 120, 100, (255, 0, 0))
        elif abilities.Abilities.is_power_bullet_available:
            Overlay.draw_text(game_window.window, "Power bullet", 40, 120, 100, (0, 255, 0))
        else:
            Overlay.draw_text(game_window.window, "Power bullet", 40, 120, 100, (140, 140, 140))
