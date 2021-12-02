import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        #初始化飞船的屏幕和设置，加载图像，矩形化
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #飞船放置于底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #用小数值变量调控不能储存小数的rect值
        self.center =float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        #绘制飞船
        self.screen.blit(self.image,self.rect)
