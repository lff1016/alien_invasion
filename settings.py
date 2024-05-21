class Settings:

    def __init__(self):
        """初始化游戏的静态配置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置

        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏的节奏
        self.speedup_scale = 1.1
        # 得分提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.bullet_speed = 2.0
        # 舰队的移动方向，1 = 向右移动，-1 = 向左移动
        self.fleet_direction = 1

        # 记分设置
        self.alien_point = 50

    # 提高游戏速度
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
