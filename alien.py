import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        #初始化外星人的屏幕和设置，加载图像，矩形化
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #储存位置为小数
        self.x = float(self.rect.x)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        #绘制外星人
        self.screen.blit(self.image,self.rect)
