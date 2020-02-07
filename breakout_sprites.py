import pygame


class Breakout_Sprite(pygame.sprite.Sprite):
    # parent class
    # load picture
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/' + image_file).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()


class Player(Breakout_Sprite):
    # player class
    def __init__(self, image_file, WINDOW_HEIGHT, WINDOW_WIDTH, PLAYER_SPEED):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.bottom = WINDOW_HEIGHT
        self.width = WINDOW_WIDTH
        self.speed = PLAYER_SPEED
        self.rect.left = (WINDOW_WIDTH - self.image.get_width()) / 2

    # move with buttons
    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.move_ip(self.speed, 0)

    # move with mouse
    def move_mouse(self, x):
        self.rect.x = x


class Brick(Breakout_Sprite):
    def __init__(self, image_file, x, y):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.x, self.rect.y = x, y


class Ball(Breakout_Sprite):
    # ball class
    def __init__(self, image_file, speed_x, speed_y, WINDOW_HEIGHT, WINDOW_WIDTH, PLAYER_HEIGHT):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.bottom = WINDOW_HEIGHT - PLAYER_HEIGHT
        self.width = WINDOW_WIDTH
        self.rect.left = WINDOW_WIDTH / 2
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if self.rect.x > self.width - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
