import pygame
import images


class Bullet:
    bullet_height = 45
    bullet_width = 111

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.speed = 20 * direction
        self.frame_counter = 0

    def draw(self, window):
        if self.speed < 0:
            window.blit(images.Images.left_bullet_sprites[self.frame_counter // 2], (self.x, self.y))
        else:
            window.blit(images.Images.right_bullet_sprites[self.frame_counter // 2], (self.x, self.y))
