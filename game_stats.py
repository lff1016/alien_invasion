class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.score = 0
        # 最高分，任何情况下都不会被重置
        self.high_score = 0
        # 游戏等级
        self.level = 1
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
