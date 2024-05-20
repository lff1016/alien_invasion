class Settings:

    def __init__(self):
        """初始化游戏配置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 舰队的移动方向，1 = 向右移动，-1 = 向左移动
        self.fleet_direction = 1
