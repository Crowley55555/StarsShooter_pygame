# powerup.py
import pygame
from settings import POWERUP_SIZE, POWERUP_TYPES
from utils import load_image
import random

class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Инициализирует усилитель.

        :param x: Координата x начальной позиции.
        :param y: Координата y начальной позиции.
        """
        super().__init__()
        self.type = random.choice(POWERUP_TYPES)
        self.image = load_image(f'powerup_{self.type}.png', POWERUP_SIZE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2

    def update(self):
        """
        Обновляет состояние усилителя.
        """
        self.rect.y += self.speed
        if self.rect.y > 1024:
            self.kill()