# utils.py
import pygame
import os
from settings import ASSETS_DIR, SOUNDS_DIR


def load_image(name, size=None):
    """
    Загружает изображение из файла и преобразует его в формат с прозрачностью.

    :param name: Имя файла изображения.
    :param size: Размер изображения (ширина, высота).
    :return: Загруженное изображение.
    """
    full_path = os.path.join(ASSETS_DIR, name)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"No such file or directory: '{full_path}'")
    image = pygame.image.load(full_path).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image


def load_sound(name):
    """
    Загружает звуковой файл.

    :param name: Имя файла звука.
    :return: Загруженный звуковой объект.
    """
    full_path = os.path.join(SOUNDS_DIR, name)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"No such file or directory: '{full_path}'")
    sound = pygame.mixer.Sound(full_path)
    return sound


def load_explosion_frames(prefix, num_frames, size=None):
    """
    Загружает последовательность изображений для анимации взрыва.

    :param prefix: Префикс имени файлов изображений.
    :param num_frames: Количество кадров в анимации.
    :param size: Размер кадра (ширина, высота).
    :return: Список загруженных кадров анимации.
    """
    frames = []
    for i in range(1, num_frames + 1):
        filename = f"{prefix}_{i}.png"
        frame = load_image(filename, size)
        frames.append(frame)
    return frames