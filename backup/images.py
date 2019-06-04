import pygame
from termcolor import colored


class Images:

    left_sprites = None
    right_sprites = None
    left_bullet_sprites = None
    right_bullet_sprites = None
    background = None

    def __init__(self):
        Images.left_sprites = Images.load_images_set("pics\Left_Armature_RUN_", 16)
        Images.right_sprites = Images.load_images_set("pics\Right_Armature_RUN_", 16)
        Images.left_bullet_sprites = Images.load_images_set("pics\\bullet\\left\\LeftArmature_Bullet-Flyng_", 15)
        Images.right_bullet_sprites = Images.load_images_set("pics\\bullet\\right\\RightArmature_Bullet-Flyng_", 15)
        Images.background = Images.load_image("pics\Flat Nature Art.png")


    @staticmethod
    def load_images_set(name, amount):
        result = []
        for i in range(amount):
            try:
                result.append(pygame.image.load(name + str(i) + '.png'))
                print('[images] loaded image "' + name + str(i) + '.png"')
            except pygame.error:
                print(colored('[images] error loading image "' + name + str(i) + '.png"', 'red'))
        return result

    @staticmethod
    def load_image(name):
        #try:
            result = pygame.image.load(name).convert()
            print('[images] loaded image "' + name + '"')
            return result
        #except pygame.error:
        #    print(colored('[images] error loading image "' + name, 'red'))
