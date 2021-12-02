class Settings():
    #储存《Alien Invasion》所有设置的类
    def __init__(self):
        #静态设置
        #屏幕设置
        self.screen_width = 1440
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #子弹设置
        self.bullet_width = 20
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5
        #外星人设置
        self.fleet_direction = 1
        self.ship_limit = 5
        self.up_scale = 1.1
        self.up_point = 30

    def initialize_dynamic_factor(self):
        #动态设置
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #飞船设置
        self.speed_factor = 1
        #子弹设置
        self.bullet_speed_factor = 1.5
        self.alien_points = 50

    def increase_grade(self,stats,scoreboard):
        #外星人设置
        self.alien_speed_factor *= self.up_scale
        self.fleet_drop_speed *= self.up_scale
        #飞船设置
        self.speed_factor *= self.up_scale
        #子弹设置
        self.bullet_speed_factor *= self.up_scale
        self.alien_points += self.up_point
        stats.grade += 1
        scoreboard.prep_grade()
