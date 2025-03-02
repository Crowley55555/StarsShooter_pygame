# player.py
import pygame
from settings import PLAYER_SIZE, PLAYER_SPEED, PLAYER_LIVES, FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils import load_image
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self,  screen_width, screen_height):
        """
        Инициализирует игрока.

        :param x: Координата x начальной позиции.
        :param y: Координата y начальной позиции.
        """
        super().__init__()
        print(f"Screen Width: {screen_width}, Screen Height: {screen_height}")  # Вывод размеров экрана
        self.original_image = load_image('player.png', PLAYER_SIZE).convert_alpha()
        self.damaged_image = load_image('player_damaged.png', PLAYER_SIZE)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - self.rect.height)
        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.last_shot_time = 0
        self.bullet2_cooldown = 0
        self.damage_timer = 0  # Инициализация damage_timer
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def update(self):
        """
        Обновляет состояние игрока.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()


        min_x = self.rect.width // 2# Минимальное значение (левая граница)
        max_x = self.screen_width - self.rect.width // 2  # Максимальное значение (правая граница)
        # Устанавливаем центр корабля между минимумом и максимумом
        self.rect.centerx = max(min(mouse_x, max_x), min_x)


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