import pygame
import images
import bullet


class Game:
    pygame.init()
    screen_width = 1280
    screen_height = 720
    width = 86  # Ширина игрока
    height = 88  # Высота игрока
    x = 1  # Координата игрока по x
    y = 505  # Координата игрока по y
    speed = 10  # Скорость передвижения игрока
    is_jump = False
    run = True
    jump_state = 10
    is_right = False
    is_left = False
    is_standing = False
    animation_counter = 0
    frame_counter = 0
    window = None
    left_sprites = None
    right_sprites = None
    background = None
    bullets = []
    was_shot = False
    shot_frame = 0

    @staticmethod
    def __init__():
        Game.window = pygame.display.set_mode((Game.screen_width, Game.screen_height))
        pygame.display.set_caption("Game by Meleron")
        #Game.left_sprites = images.Images.load_images_set("pics\Left_Armature_RUN_", 16)
        #Game.right_sprites = images.Images.load_images_set("pics\Right_Armature_RUN_", 16)
        #Game.background = images.Images.load_image("pics\Flat Nature Art.png")
        images.Images()
        Game.left_sprites = images.Images.left_sprites
        Game.right_sprites = images.Images.right_sprites
        Game.background = images.Images.background
        Game.launch_game()

    @staticmethod
    def draw_frame():
        Game.window.blit(Game.background, (0, 0))
        for shot in Game.bullets:
            shot.draw(Game.window)
        if Game.animation_counter >= 29:
            Game.animation_counter = 0
        if Game.is_left:
            Game.window.blit(Game.left_sprites[Game.animation_counter // 2], (Game.x, Game.y))
        if Game.is_right:
            Game.window.blit(Game.right_sprites[Game.animation_counter // 2], (Game.x, Game.y))
        if not Game.is_standing:
            Game.animation_counter += 1
        pygame.display.update()

    @staticmethod
    def launch_game():
        while Game.run:
            pygame.time.Clock().tick(30)
            if Game.frame_counter == 30:
                Game.frame_counter = 0
                Game.was_shot = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.run = False

            for shot in Game.bullets:
                if 0 - bullet.Bullet.bullet_width < shot.x < Game.screen_width:
                    shot.x += shot.speed
                else:
                    #shot.pop(Game.bullets.index(shot))
                    Game.bullets.remove(shot)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_x] and (Game.frame_counter - Game.shot_frame > 5 or not Game.was_shot):
                Game.bullets.append(bullet.Bullet(Game.x, Game.y, 1 if Game.is_right else -1))
                Game.shot_frame = Game.frame_counter
                Game.was_shot = True
            if keys[pygame.K_LEFT] and Game.x - Game.speed > 0:
                Game.x -= Game.speed
                Game.is_left = True
                Game.is_right = False
                Game.is_standing = False
            elif keys[pygame.K_RIGHT] and Game.x + Game.width + Game.speed < Game.screen_width:
                Game.x += Game.speed
                Game.is_right = True
                Game.is_left = False
                Game.is_standing = False
            else:
                Game.is_standing = True
                Game.animation_counter = 4
            if keys[pygame.K_SPACE]:
                Game.is_jump = True
            if Game.is_jump:
                if Game.jump_state == -11:
                    Game.jump_state = 10
                    Game.is_jump = False
                else:
                    Game.y -= 3 * Game.jump_state
                    Game.jump_state -= 1
            Game.draw_frame()
            Game.frame_counter += 1
