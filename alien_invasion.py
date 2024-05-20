import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """"管理游戏资源和行为的类"""

    def __init__(self):
        pygame.init()
        # 用来控制帧率
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星入侵")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # 创建外星人舰队
        self._create_fleet()

    def run_game(self):
        while True:
            # 监听按键
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._update_alien()
            self.__update_screen()
            # 让时钟进行倒计时，确保循环恰好每秒运行60次
            self.clock.tick(60)

    # ———— 辅助函数 ————
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.__check_event_keyDown(event)
            elif event.type == pygame.KEYUP:
                self.__check_event_keyUp(event)

    def __check_event_keyDown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def __check_event_keyUp(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # 检查外星舰队是否到达边缘
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    # 到达边缘区域向下移动，并改变方向
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    # —————— 各种方法 ——————
    # 开火
    def _fire_bullet(self):
        # 创建一颗子弹并加入编组
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    # 创建一个外星人并添加到当前行中
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    # 创建外星人舰队
    def _create_fleet(self):
        alien = Alien(self)
        # 不断添加外星人直到没有空间
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 10 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 添加了一行外星人后，重置 x ，并加 y
            current_x = alien_width
            current_y += 2 * alien_height

    # ———— 更新相关逻辑————
    # 更新屏幕
    def __update_screen(self):
        # 每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    # 更新子弹
    def _update_bullet(self):
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 检查子弹是否击中了外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)

    # 更新外星人
    def _update_alien(self):
        # 检查是否超边缘，超边缘更新位置
        self._check_fleet_edges()
        self.aliens.update()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
