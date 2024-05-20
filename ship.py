import pygame


class Ship:

    def __init__(self, ai_game):
        """初始化飞船并设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 加载飞船并获取其外接矩形
        origin_image = pygame.image.load('./images/ship.bmp')
        size = origin_image.get_size()
        self.image = pygame.transform.scale(
            origin_image, (int(size[0] / 4), int(size[1] / 4)))
        self.rect = self.image.get_rect()

        # 将飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 持续移动飞船的标志（一开始不移动）
        self.moving_right = False
        self.moving_left = False

        # 飞船属性x中存一个移动的浮点数
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据 self.x 更新 rect.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
