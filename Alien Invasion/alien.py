import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас що моделює прибульця"""
    def __init__(self,ai_game):
        """Ініціалізувати прибульця та задати його початкове положення"""
        super().__init__()
        self.screen = ai_game.screen

        # Завантажити картинку прибульця і зробити атрибутом
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Розмістити нового прибульця зліва екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Розмістити прибульців у горизонтальну позицію
        self.x = float(self.rect.x)
