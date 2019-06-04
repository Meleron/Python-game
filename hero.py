import images
import pygame
import game
import knight
import abilities
import database


class Hero:

    width = None  # Ширина игрока
    height = None  # Высота игрока
    is_training = False

    def __init__(self):
        Hero.width = database.Database.hero_width
        Hero.height = database.Database.hero_height
        self.x = 640  # Координата игрока по x
        #self.x = 1280  # Координата игрока по x
        self.y = 505  # Координата игрока по y
        self.aix = 0
        self.speed = 15  # Скорость передвижения игрока
        self.is_jump = False
        self.jump_state = 10
        self.is_right = True
        self.is_left = False
        self.is_standing = False
        self.animation_counter = 0
        self.was_shot = False
        self.shot_frame = 0
        self.health = database.Database.start_hero_health
        self.shield = 0

    def on_key_tapped_hero(self, keys, game_window):
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
            self.is_left = True
            self.is_right = False
            self.is_standing = False
        elif (keys[pygame.K_RIGHT] and self.x + self.width + self.speed < game.Game.screen_width) or Hero.is_training:
            self.x += self.speed
            self.is_right = True
            self.is_left = False
            self.is_standing = False
        else:
            self.is_standing = True
            self.animation_counter = 4
        if keys[pygame.K_SPACE]:
            self.is_jump = True
        if self.is_jump:
            if self.jump_state == -11:
                self.jump_state = 10
                self.is_jump = False
            else:
                self.y -= 3 * self.jump_state
                self.jump_state -= 1

        for enemy in game_window.knights:
            if self.shield > 0:
                self.shield -= 1
                break
            if not self.y + Hero.height < enemy.y:
                if enemy.x - (self.x + Hero.width) < 0 < (enemy.x + knight.Knight.knight_width) - (self.x + Hero.width):
                    self.hero_damaged(game_window)
        for shot in game_window.bombs:
            if self.shield > 0:
                self.shield -= 1
                break
            if self.y < shot.y and self.x < shot.x < self.x + Hero.width:
                self.hero_damaged(game_window)

    def hero_damaged(self, game_window):
        abilities.Abilities.is_shield_available = False
        self.activate_shield()
        self.health -= 1
        print("[hero] Hero damaged, health: " + str(self.health))
        if self.health == 0:
            game_window.game_over = True

    def activate_shield(self):
        self.shield = 30

    def draw(self, window):
        if self.animation_counter >= 29:
            self.animation_counter = 0
        if self.is_left:
            window.blit(images.Images.left_sprites[self.animation_counter // 2], (self.x, self.y))
        if self.is_right:
            window.blit(images.Images.right_sprites[self.animation_counter // 2], (self.x, self.y))
        if not self.is_standing:
            self.animation_counter += 1
