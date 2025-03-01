# bullet.py
import pygame
from settings import BULLET1_SIZE, BULLET2_SIZE, BULLET1_SPEED, BULLET2_SPEED
from utils import load_image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_type):
        """
        Инициализирует пулю.

        :param x: Координата x начальной позиции.
        :param y: Координата y начальной позиции.
        :param bullet_type: Тип пули (1 или 2).
        """
        super().__init__()
        if bullet_type == 1:
            self.image = load_image('bullet1.png', BULLET1_SIZE)
            self.speed = BULLET1_SPEED
        elif bullet_type == 2:
            self.image = load_image('bullet2.png', BULLET2_SIZE)
            self.speed = BULLET2_SPEED
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        """
        Обновляет состояние пули.
        """
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()