import pygame
import game
import images
import  database


class Knight:
    knight_width = None
    knight_height = None
    knight_speed = None
    base_reaction = None
    spawned = False

    def __init__(self):
        Knight.knight_width = database.Database.knight_width
        Knight.knight_height = database.Database.hero_height
        Knight.knight_speed = database.Database.start_knight_speed
        Knight.base_reaction = database.Database.start_knight_reaction
        self.x = -Knight.knight_width
        self.y = 505
        self.speed = Knight.knight_speed
        self.health = 3
        self.reaction = Knight.base_reaction
        self.right_direction = False
        self.direction_counter = 0
        self.last_direction = 0
        self.animation_counter = 0

    def move_knight(self, player):
        if self.x > player.x:
            if self.right_direction:
                self.direction_counter = self.reaction
            if self.direction_counter > 0:
                self.x += self.speed
                self.direction_counter -= 1
            else:
                self.x -= self.speed
            self.right_direction = False
        else:
            if not self.right_direction:
                self.direction_counter = self.reaction
            if self.direction_counter > 0:
                self.x -= self.speed
                self.direction_counter -= 1
            else:
                self.x += self.speed
            self.right_direction = True

    def draw(self, window):
        #pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, Knight.knight_width, Knight.knight_height)) #Hitbox
        if self.animation_counter >= 29:
            self.animation_counter = 0
        if self.right_direction:
            window.blit(images.Images.right_knight_sprites[self.animation_counter // 6], (self.x, self.y))
        else:
            window.blit(images.Images.left_knight_sprites[self.animation_counter // 6], (self.x, self.y))
        self.animation_counter += 1

    def damage(self, amount, game_window):
        self.health -= amount
        print("[knight] Knight damaged, health: " + str(self.health))
        if self.health <= 0:
            self.destroy_knight(game_window)
            game_window.score += 5

    def destroy_knight(self, game_window):
        game_window.knights.remove(self)
        Knight.spawned = False
        print("[knight] Knight destroyed")

    #@staticmethod
    #def on_key_tapped_knight(keys):
    #    if keys[pygame.K_s] and not Knight.spawned:
    #        Knight.spawn_knight("left")

    @staticmethod
    def spawn_knight(direction, game_window):
        knight_to_spawn = Knight()
        if direction == "left":
            knight_to_spawn.x = game.Game.screen_width
        #knight_to_spawn.x = game.Game.screen_width
        Knight.spawned = True
        game_window.knights.append(knight_to_spawn)
        print("[knight] Knight spawned")
