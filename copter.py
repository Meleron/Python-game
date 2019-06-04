import pygame
import hero
import bomb
import images
import database


class Copter:

    copter_width = None
    copter_height = None
    spawned = False

    def __init__(self):
        Copter.copter_width = database.Database.copter_width
        Copter.copter_height = database.Database.copter_height
        self.x = 1
        self.y = 100
        self.speed = 10
        self.shot = False
        self.animation_counter = 0

    @staticmethod
    def on_key_tapped_copter(keys, game_window):
        if keys[pygame.K_c] and not Copter.spawned:
            Copter.spawn_copter(game_window)
            Copter.spawned = True

    @staticmethod
    def spawn_copter(game_window):
        game_window.copters.append(Copter())
        print("[copter] Copter spawned")

    def move_copter(self, player, game_window):
        self.x += self.speed
        if player.x <= self.x <= player.x + hero.Hero.width and not self.shot:
            bomb.Bomb.spawn_bomb(self, game_window)
            self.shot = True

    def draw(self, window):
        if self.animation_counter >= 29:
            self.animation_counter = 0
        #pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, Copter.copter_width, Copter.copter_height)) #Hitbox
        window.blit(images.Images.right_copter_sprites[self.animation_counter // 15], (self.x, self.y))
        self.animation_counter += 1

    def destroy_copter(self, game_window):
        game_window.copters.remove(self)
        Copter.spawned = False
        print("[copter] Copter destroyed")
