import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """初始化外星人设置和位置"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像
        origin_image = pygame.image.load('./images/aline.bmp')
        size = origin_image.get_size()
        self.image = pygame.transform.scale(
            origin_image, (int(size[0] / 4), int(size[1] / 4)))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精准位置
        self.x = float(self.rect.x)

    # 检查外星人是否移动到了屏幕边缘
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        # 向右移动外星人
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
