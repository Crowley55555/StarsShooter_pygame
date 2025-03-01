# player.py
import pygame
from settings import PLAYER_SIZE, PLAYER_SPEED, PLAYER_LIVES
from utils import load_image


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

    def update(self, dt):
        """
        Обновляет состояние игрока.

        :param dt: Время с прошлого кадра в секундах.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt

        self.rect.clamp_ip(pygame.Rect(0, 0, 1024, 1024))

        if self.damage_timer > 0:
            self.damage_timer -= dt
            if self.damage_timer <= 0:
                self.image = self.original_image

        if self.bullet2_cooldown > 0:
            self.bullet2_cooldown -= dt

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
        self.damage_timer = 0.5  # Время показа поврежденного спрайта