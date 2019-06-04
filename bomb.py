import pygame
import copter
import images

class Bomb:

    bomb_width = 20
    bomb_height = 20

    def __init__(self, bound_copter):
        self.x = bound_copter.x + copter.Copter.copter_width / 2
        self.y = bound_copter.y
        self.speed = 10

    @staticmethod
    def spawn_bomb(bound_copter, game_window):
        print("[bomb] Bomb spawned")
        game_window.bombs.append(Bomb(bound_copter))

    def move_bomb(self):
        self.y += self.speed
        self.speed += 1

    def draw(self, window):
        #pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, Bomb.bomb_width, Bomb.bomb_height)) #Hitbox
        window.blit(images.Images.bomb[0], (self.x, self.y))

    def destroy_bomb(self, game_window):
        game_window.bombs.remove(self)
        print("[bomb] Bomb destroyed")

