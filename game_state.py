import json
class GameStates():
    """跟踪统计游戏信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 初始化分数
        self.score = 0
        # 在任何情况下都不应改重置最高分
        with open("settings.json") as fileobj:
            self.high_score = json.load(fileobj)
        

    def reset_stats(self):
        """重置状态"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
