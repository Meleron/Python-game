import pygame
import bullet


class Abilities:

    is_shield_available = False
    is_power_bullet_available = False

    @staticmethod
    def on_key_tapped_abilities(player, keys):
        if keys[pygame.K_z] and Abilities.is_shield_available:
            Abilities.is_shield_available = False
            player.activate_shield()
        if keys[pygame.K_a] and Abilities.is_power_bullet_available:
            Abilities.is_power_bullet_available = False
            bullet.Bullet.is_next_power_bullet = True

    @staticmethod
    def activate_abilities():
        Abilities.is_shield_available = True
        Abilities.is_power_bullet_available = True
