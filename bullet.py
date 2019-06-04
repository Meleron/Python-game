import pygame
import images
import game
import hero
import knight
from termcolor import colored


class Bullet:
    bullet_height = 45
    bullet_width = 111
    shot_speed = 5
    is_next_power_bullet = False

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.speed = 20 * direction
        self.power_bullet = False
        self.frame_counter = 0

    @staticmethod
    def on_key_tapped_bullet(keys, player, game_window):
        if keys[pygame.K_x] and (game_window.frame_counter - player.shot_frame > Bullet.shot_speed or not player.was_shot):
            if player.is_right:
                bullet = Bullet(player.x + hero.Hero.width - 10, player.y + 10, 1 if player.is_right else -1)
            else:
                bullet = Bullet(player.x - hero.Hero.width - 10, player.y + 10, 1 if player.is_right else -1)
            if Bullet.is_next_power_bullet:
                bullet.power_bullet = True
                Bullet.is_next_power_bullet = False
            game_window.bullets.append(bullet)
            player.shot_frame = game_window.frame_counter
            player.was_shot = True

    def move_bullet(self, game_window):
        self.x += self.speed
        for enemy in game_window.knights:
            if self.speed > 0:
                if enemy.x < self.x + Bullet.bullet_width / 1.5 < enemy.x + knight.Knight.knight_width and self.y >= enemy.y:
                    if self.power_bullet:
                        enemy.damage(2, game_window)
                    else:
                        self.destroy_bullet(game_window)
                        enemy.damage(1, game_window)
            else:
                if enemy.x + knight.Knight.knight_width > self.x + Bullet.bullet_width / 3 > enemy.x and self.y >= enemy.y:
                    if self.power_bullet:
                        enemy.damage(2, game_window)
                    else:
                        self.destroy_bullet(game_window)
                        enemy.damage(1, game_window)

    def destroy_bullet(self, game_window):
        if self in game_window.bullets:
            game_window.bullets.remove(self)

    def activate_power_bullet(self):
        self.power_bullet = True

    def draw(self, window):
        if self.speed < 0:
            window.blit(images.Images.left_bullet_sprites[self.frame_counter // 2], (self.x, self.y))
        else:
            window.blit(images.Images.right_bullet_sprites[self.frame_counter // 2], (self.x, self.y))
