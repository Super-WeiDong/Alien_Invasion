import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        #基础属性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,38)
        self.prep_score()
        self.prep_high_score()
        self.prep_grade()
        self.prep_ship()

    def prep_score(self):
        round_score = round(self.stats.score)
        score_str = 'Score: ' + "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = self.screen_rect.top + 20

    def prep_high_score(self):
        round_high_score = round(self.stats.high_score)
        high_score_str = 'Highest Score: '+"{:,}".format(round_high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.screen_rect.top + 20

    def prep_grade(self):
        grade_str = 'Level: ' + "{:,}".format(self.stats.grade)
        self.grade_image = self.font.render(grade_str,True,self.text_color,self.ai_settings.bg_color)
        self.grade_image_rect = self.grade_image.get_rect()
        self.grade_image_rect.right = self.screen_rect.right - 20
        self.grade_image_rect.top = self.screen_rect.top + 50

    def show_score(self):
        self.screen.blit(self.score_image,self.score_image_rect)
        self.screen.blit(self.high_score_image,self.high_score_image_rect)
        self.screen.blit(self.grade_image,self.grade_image_rect)
        self.ships.draw(self.screen)

    def prep_ship(self):
        self.ships = Group()
        print(self.ai_settings.ship_limit)
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        print('1')
