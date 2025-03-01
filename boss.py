# boss.py
import pygame
from settings import BOSS_SIZE, BOSS_HP, BOSS_SHOOT_INTERVAL
from utils import load_image


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        """
        Инициализирует босса.
        """
        super().__init__()
        self.image = load_image('boss.png', BOSS_SIZE)
        self.rect = self.image.get_rect(center=(512, 100))
        self.speed = 2
        self.hp = BOSS_HP
        self.shoot_interval = BOSS_SHOOT_INTERVAL
        self.last_shot_time = 0

    def update(self):
        """
        Обновляет состояние босса.
        """
        self.rect.y += self.speed
        if self.rect.y > 1024:
            self.kill()

    def take_damage(self, damage):
        """
        Уменьшает HP босса.

        :param damage: Количество урона.
        """
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def shoot(self, bullet_group):
        """
        Создает пулю босса.

        :param bullet_group: Группа спрайтов для пуль.
        """
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > self.shoot_interval * 1000:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, 1)
            bullet_group.add(bullet)
            self.last_shot_time = now