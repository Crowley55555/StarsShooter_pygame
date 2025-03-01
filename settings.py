# settings.py
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'music')

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
FPS = 60

PLAYER_SIZE = (100, 100)
PLAYER_SPEED = 5
PLAYER_LIVES = 3

ENEMY_SIZES = {
    'weak': (50, 50),
    'medium': (75, 75),
    'strong': (100, 100),
    'asteroid': (60, 60)  # Размер астероида
}
ENEMY_SPEED = {
    'weak': 2,
    'medium': 2.5,
    'strong': 3,
    'asteroid': 1.5  # Скорость астероида
}
ENEMY_HP = {
    'weak': 1,
    'medium': 2,
    'strong': 3,
    'asteroid': 1  # HP астероида
}

BULLET1_SIZE = (20, 20)
BULLET2_SIZE = (30, 30)
BULLET1_SPEED = 10
BULLET2_SPEED = 15
BULLET2_COOLDOWN = 10  # секунды

POWERUP_SIZE = (50, 50)
POWERUP_INTERVAL = 60  # секунды
POWERUP_TYPES = ['damage', 'speed', 'life']

BOSS_SIZE = (200, 200)
BOSS_HP = 20
BOSS_SHOOT_INTERVAL = 2  # секунды

SCORE_PER_ENEMY = {
    'weak': 10,
    'medium': 20,
    'strong': 30,
    'boss': 200,
    'asteroid': 5  # Очки за астероид
}