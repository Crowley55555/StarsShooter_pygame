# enemy.py
import pygame
from settings import ENEMY_SIZES, ENEMY_SPEED, ENEMY_HP
from utils import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type):
        """
        Инициализирует врага.

        :param x: Координата x начальной позиции.
        :param y: Координата y начальной позиции.
        :param enemy_type: Тип врага ('weak', 'medium', 'strong', 'asteroid').
        """
        super().__init__()
        self.type = enemy_type
        self.image = load_image(f'enemy_{enemy_type}.png', ENEMY_SIZES[enemy_type])
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = ENEMY_SPEED[enemy_type]
        self.hp = ENEMY_HP[enemy_type]

    def update(self):
        """
        Обновляет состояние врага.
        """
        self.rect.y += self.speed
        if self.rect.y > 1024:
            self.kill()

    def take_damage(self, damage):
        """
        Уменьшает HP врага.

        :param damage: Количество урона.
        """
        self.hp -= damage
        if self.hp <= 0:
            self.kill()


class Asteroid(Enemy):
    def __init__(self, x, y):
        """
        Инициализирует астероид.

        :param x: Координата x начальной позиции.
        :param y: Координата y начальной позиции.
        """
        super().__init__(x, y, 'asteroid')