import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_function as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    bg_color = (ai_settings.bg_color)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建子弹编组
    bullets = Group()
    #创建外星人编组
    aliens = Group()
    gf.creat_fleet(ai_settings,screen,aliens,ship)
    play_button = Button(ai_settings,screen,"Play")
    scoreboard = Scoreboard(ai_settings,screen,stats)
    #游戏主循环开始
    while True:
        #监视键盘和鼠标事件
        gf.check_event(ai_settings,screen,ship,bullets,stats,play_button,aliens,scoreboard)

        #根据操作或设置更新各元素位置
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings,aliens)
            gf.update_bullets(bullets)
            gf.check_bullets_aliens_collission(ai_settings,screen,bullets,aliens,ship,stats,scoreboard)
            gf.check_aliens_ship_collision(aliens,ship,bullets,ai_settings,screen,stats,scoreboard)
            gf.check_aliens_bottom(aliens,ship,bullets,ai_settings,screen,stats,scoreboard)
            gf.update_bullets(bullets)
        #把更新完的元素画上去
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,scoreboard)

run_game()
