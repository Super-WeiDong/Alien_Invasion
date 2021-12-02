import sys
#用于退出游戏的模块

import pygame
#包含游戏主要功能的模块

from bullet import Bullet
from alien import Alien
from time import sleep

def fire_bullet(ai_settings,screen,ship,bullets):
    #创建一颗子弹，加入bullet编组
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_key_down_event(event,ai_settings,screen,ship,bullets,stats,play_button,aliens,scoreboard):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(stats,play_button,aliens,bullets,ship,ai_settings,screen,scoreboard)

def check_key_up_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ai_settings,screen,ship,bullets,stats,play_button,aliens,scoreboard):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event,ai_settings,screen,ship,bullets,stats,play_button,aliens,scoreboard)
        elif event.type == pygame.KEYUP:
            check_key_up_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not stats.game_active:
                mouse_x,mouse_y =pygame.mouse.get_pos()
                check_paly_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ship,ai_settings,screen,scoreboard)
                pygame.mouse.set_visible(False)

def start_game(stats,play_button,aliens,bullets,ship,ai_settings,screen,scoreboard):
    ai_settings.initialize_dynamic_factor()
    aliens.empty()
    bullets.empty()
    creat_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()
    stats.reset_stats()
    stats.game_active = True
    stats.score = 0
    stats.grade = 0
    scoreboard.prep_score()
    scoreboard.prep_grade()
    scoreboard.prep_ship()
    sleep(0.5)

def check_paly_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ship,ai_settings,screen,scoreboard):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        start_game(stats,play_button,aliens,bullets,ship,ai_settings,screen,scoreboard)
#计算横向外星人个数
def get_number_alien_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,alien_height,ship_height):
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    row_number = int(available_space_y/(2*alien_height))
    return row_number

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(ai_settings,screen,aliens,ship):
    alien = Alien(ai_settings,screen)
    #创建第一行横坐标不同的外星人
    number_aliens_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,alien.rect.height,ship.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)

def update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,scoreboard):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    scoreboard.show_score()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def check_bullets_aliens_collission(ai_settings,screen,bullets,aliens,ship,stats,scoreboard):
    #检查击中
    collissions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collissions:
        for aliens in collissions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            if stats.score >= stats.high_score:
                stats.high_score = stats.score
            scoreboard.prep_score()
            scoreboard.prep_high_score()
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(ai_settings,screen,aliens,ship)
        ai_settings.increase_grade(stats,scoreboard)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def check_aliens_ship_collision(aliens,ship,bullets,ai_settings,screen,stats,scoreboard):
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(aliens,ship,bullets,ai_settings,screen,stats,scoreboard)

def ship_hit(aliens,ship,bullets,ai_settings,screen,stats,scoreboard):
    stats.ships_left -= 1
    scoreboard.prep_ship()
    if stats.ships_left > 0:
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(aliens,ship,bullets,ai_settings,screen,stats,scoreboard):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(aliens,ship,bullets,ai_settings,screen,stats,scoreboard)
            break
