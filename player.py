# player.py
import pygame
from settings import PLAYER_SIZE, PLAYER_SPEED, PLAYER_LIVES, FPS
from utils import load_image
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Инициализирует игрока.

        :param x: Координата x начальной позиции.
        :param y: Координата y начальной позиции.
        """
        super().__init__()
        self.original_image = load_image('player.png', PLAYER_SIZE)
        self.damaged_image = load_image('player_damaged.png', PLAYER_SIZE)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.last_shot_time = 0
        self.bullet2_cooldown = 0
        self.damage_timer = 0

    def update(self):
        """
        Обновляет состояние игрока.
        """
        mouse_x, _ = pygame.mouse.get_pos()
        screen_width = 1024  # Предполагаемая ширина экрана

        # Перемещение игрока влево или вправо в зависимости от положения мыши
        if mouse_x < self.rect.centerx:
            self.rect.x -= self.speed
        elif mouse_x > self.rect.centerx:
            self.rect.x += self.speed

        # Ограничение перемещения игрока внутри экрана
        self.rect.clamp_ip(pygame.Rect(0, 0, screen_width, 1024))

        if self.damage_timer > 0:
            self.damage_timer -= 1 / FPS
            if self.damage_timer <= 0:
                self.image = self.original_image

        if self.bullet2_cooldown > 0:
            self.bullet2_cooldown -= 1 / FPS

    def shoot(self, bullet_group, bullet_type):
        """
        Создает пулю игрока.

        :param bullet_group: Группа спрайтов для пуль.
        :param bullet_type: Тип пули (1 или 2).
        """
        now = pygame.time.get_ticks()
        if bullet_type == 1:
            bullet = Bullet(self.rect.centerx, self.rect.top, 1)
            bullet_group.add(bullet)
        elif bullet_type == 2 and self.bullet2_cooldown <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.top, 2)
            bullet_group.add(bullet)
            self.bullet2_cooldown = 10  # 10 секунд перезарядки

    def take_damage(self):
        """
        Уменьшает жизни игрока и меняет спрайт на поврежденный.
        """
        self.lives -= 1
        self.image = self.damaged_image
        self.damage_timer = 0.5 * FPS  # Время показа поврежденного спрайта