import pygame
import images
import bullet
import hero
import knight
import copter
import random
import overlay
import abilities
import bomb
import database
import cv2
#import copterai


class Game:
    pygame.init()
    screen_width = None
    screen_height = None
    highscore = None
    hero_cascade = cv2.CascadeClassifier('work/haar/classifier/cascade.xml')

    def __init__(self):
        Game.screen_width = database.Database.screen_width
        Game.screen_height = database.Database.screen_height
        Game.highscore = database.Database.highscore
        self.score = 0
        self.run = True
        self.pause = False
        self.game_over = False
        self.frame_counter = 0
        self.abilities_recharge = 0
        self.difficulty_spawn = database.Database.spawn_rate_on_start
        self.window = None
        self.background = None
        self.bullets = []
        self.knights = []
        self.copters = []
        self.bombs = []
        self.player = hero.Hero()
        #############
        self.window = pygame.display.set_mode((Game.screen_width, Game.screen_height))
#        self.cop_ai = copterai.AI()
        pygame.display.set_caption("Game by Meleron")
        images.Images()
        self.launch_game()

    def draw_frame(self):
        self.window.blit(images.Images.background, (0, 0))
        for shot in self.bullets:
            shot.draw(self.window)
        for enemy in self.knights:
            enemy.draw(self.window)
        for enemy in self.copters:
            enemy.draw(self.window)
        for shot in self.bombs:
            shot.draw(self.window)
        overlay.Overlay.draw_info(self)
        self.player.draw(self.window)
        pygame.display.update()

    def end_game(self):
        if self.score > Game.highscore:
            Game.highscore = self.score
        self.window.blit(images.Images.background, (0, 0))
        overlay.Overlay.draw_text(self.window, "Game over!", 80,
                                  Game.screen_width / 2, Game.screen_height / 2 - 80, (0, 0, 0))
        overlay.Overlay.draw_text(self.window, "Your score: " + str(self.score), 80,
                                  Game.screen_width / 2, Game.screen_height / 2, (0, 0, 0))
        overlay.Overlay.draw_text(self.window, "Highscore: " + str(Game.highscore), 50,
                                  Game.screen_width / 2, Game.screen_height / 2 + 120, (77, 77, 77))
        pygame.display.update()

    def move_entities(self):
        for shot in self.bullets:
            if 0 - bullet.Bullet.bullet_width < shot.x < Game.screen_width:
                shot.move_bullet(self)
            else:
                shot.destroy_bullet(self)
        for enemy in self.knights:
            if enemy.x < Game.screen_width + knight.Knight.knight_width:
                enemy.move_knight(self.player)
            else:
                enemy.destroy_knight(self)
        for enemy in self.copters:
            if enemy.x < Game.screen_width + copter.Copter.copter_width:
                enemy.move_copter(self.player, self)
            else:
                enemy.destroy_copter(self)
        for shot in self.bombs:
            if shot.y < 585 - bomb.Bomb.bomb_height:
                shot.move_bomb()
            else:
                shot.destroy_bomb(self)

    def key_handler(self):
        keys = pygame.key.get_pressed()
        self.player.on_key_tapped_hero(keys, self)
        bullet.Bullet.on_key_tapped_bullet(keys, self.player, self)
        #knight.Knight.on_key_tapped_knight(keys)
        copter.Copter.on_key_tapped_copter(keys, self)
        abilities.Abilities.on_key_tapped_abilities(self.player, keys)

    def increase_difficulty(self):
        if self.difficulty_spawn - 15 > 10:
            self.difficulty_spawn -= 15
        else:
            self.difficulty_spawn = 20
            if knight.Knight.base_reaction - 4 > 4:
                knight.Knight.base_reaction -= 4
            elif knight.Knight.knight_speed + 2 < 15:
                knight.Knight.knight_speed += 2
            elif bullet.Bullet.shot_speed + 1 < 7:
                bullet.Bullet.shot_speed += 1

        print("[game] Difficulty increased (spawn: " + str(self.difficulty_spawn) + ", knight reaction: "
              + str(knight.Knight.knight_speed) + ", knight speed: " + str(knight.Knight.knight_speed)
              + ", shot speed: " + str(bullet.Bullet.shot_speed) + ")")

    def launch_game(self):
        #knight.Knight.spawn_knight("left" if random.randint(0, 1) == 0 else "", self)
        while self.run:
            pygame.time.Clock().tick(30)
            if self.frame_counter == 30:
                self.frame_counter = 0
                self.player.was_shot = False
            if self.abilities_recharge == 300:
                self.abilities_recharge = 0
                self.increase_difficulty()
                abilities.Abilities.activate_abilities()
                copter.Copter.spawn_copter(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    if self.score > Game.highscore:
                        Game.highscore = self.score
                    database.Database.save_data()
            if self.game_over:
                self.end_game()
                continue
            self.move_entities()
            if self.abilities_recharge % self.difficulty_spawn == 0:
                knight.Knight.spawn_knight("left" if random.randint(0, 1) == 0 else "", self)
            self.key_handler()
            self.draw_frame()
            self.frame_counter += 1
            self.abilities_recharge += 1
