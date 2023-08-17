import pygame
class Ship:
    def __init__(self,ai_game) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.update_ship_lo()

    def update_ship_lo(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left  and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_up    and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down  and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        