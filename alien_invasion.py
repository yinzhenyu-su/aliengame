import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_state import GameStates
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 外星人
    aliens = Group()
    # 创建一个用于游戏统计的实例
    stats = GameStates(ai_settings)
    pygame.display.set_caption("Alien Invasion")
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始按钮
    play_button = Button(ai_settings, screen, "Play")
    # 记分版
    sb = Scoreboard(ai_settings, screen, stats)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets, sb, stats, play_button)


run_game()
