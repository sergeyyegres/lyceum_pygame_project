import pygame
from pygame.locals import *
import sys
from breakout_sprites import *
import random
import time
import pygame.midi

# STANDART SETTINGS
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
BALL_WIDTH, BALL_HEIGHT = 16, 16
BRICK_WIDTH, BRICK_HEIGHT = 64, 16
PLAYER_WIDTH, PLAYER_HEIGHT = 64, 16
PLAYER_SPEED = 10
BALL_SPEED = 6
COLOR_KEY = (255, 255, 255)
MOTION = 1
STACK = 3
START_DELAY = 40
CLICK_DELAY = 30


# game fuction
def game(WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_SPEED, MOTION, STACK, START_DELAY, CLICK_DELAY, name):
    # initialization
    pygame.init()
    pygame.display.set_caption('Breakout')
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.key.set_repeat(START_DELAY, CLICK_DELAY)
    clock = pygame.time.Clock()
    score = 0
    update = True

    # sound play
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play()

    # groups
    all_sprites_group = pygame.sprite.Group()
    player_bricks_group = pygame.sprite.Group()
    bricks_group = pygame.sprite.Group()

    # add sprites to their group
    ball = Ball('ball.png', BALL_SPEED, -BALL_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH, PLAYER_HEIGHT)
    all_sprites_group.add(ball)

    player = Player('player.png', WINDOW_HEIGHT, WINDOW_WIDTH, PLAYER_SPEED)
    all_sprites_group.add(player)
    player_bricks_group.add(player)

    # create block field
    for i in range((WINDOW_WIDTH // (BRICK_WIDTH + 5)) - 1):
        for j in range((WINDOW_HEIGHT // (BRICK_HEIGHT + 5)) // STACK):
            brick = Brick('brick.png', (i + 1) * BRICK_WIDTH + 5, (j + 3) * BRICK_HEIGHT + 5)
            all_sprites_group.add(brick)
            bricks_group.add(brick)
            player_bricks_group.add(brick)

    # game loop
    while True:
        # game over
        if ball.rect.y > WINDOW_HEIGHT:
            # game over text
            window.fill((0, 0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("Game over!", 1, (100, 255, 100))
            text_x = WINDOW_WIDTH // 2 - text.get_width() // 2
            text_y = WINDOW_HEIGHT // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            window.blit(text, (text_x, text_y))
            pygame.draw.rect(window, (0, 255, 0), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
            # score text
            font = pygame.font.Font(None, 50)
            text = font.render(f"Score : {score}", 1, (100, 255, 100))
            text_x = WINDOW_WIDTH // 2 - text.get_width() // 2
            text_y = WINDOW_HEIGHT // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            window.blit(text, (text_x, text_y + 90))
            pygame.draw.rect(window, (0, 255, 0), (text_x - 10, text_y + 80,
                                                   text_w + 20, text_h + 20), 1)
            pygame.display.flip()
            update = False
            pygame.mixer.music.stop()
            # restart or exit
            while True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        with open('history.txt', 'a') as f:
                            f.write(str(
                                f'Name: {name} Score:{score} Settings:{WINDOW_WIDTH},{WINDOW_HEIGHT},{STACK},{BALL_SPEED},{MOTION}' + '\n'))
                        game(WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_SPEED, MOTION, STACK, START_DELAY, CLICK_DELAY, name)
                    if event.type == QUIT:
                        pygame.quit()
                        with open('history.txt', 'a') as f:
                            f.write(str(
                                f'Name: {name} Score:{score} Settings:{WINDOW_WIDTH},{WINDOW_HEIGHT},{STACK},{BALL_SPEED},{MOTION}' + '\n'))
                        sys.exit()

        # move player horizontally
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                with open('history.txt', 'a') as f:
                    f.write(str(
                        f'Name: {name} Score:{score} Settings:{WINDOW_WIDTH},{WINDOW_HEIGHT},{STACK},{BALL_SPEED},{MOTION}' + '\n'))
                sys.exit()
            elif event.type == MOUSEMOTION and MOTION == 1:
                player.move_mouse(event.pos[0])
            elif event.type == KEYDOWN and MOTION == 0:
                if event.key == K_LEFT:
                    player.move_left()
                elif event.key == K_RIGHT:
                    player.move_right()

        # collision detection (ball bounce against brick & player)
        hits = pygame.sprite.spritecollide(ball, player_bricks_group, False)
        if hits:
            hit_rect = hits[0].rect
            # bounce the ball (according to side collided)
            if hit_rect.left > ball.rect.left or ball.rect.right < hit_rect.right:
                ball.speed_y *= -1
                print(ball.speed_y)
            else:
                ball.speed_x *= -1
                print(ball.speed_x)

            # collision with blocks
            if pygame.sprite.spritecollide(ball, bricks_group, True):
                score += len(hits)
                print(f"Score: {score}")

        # render groups
        window.fill((0, 0, 0))
        all_sprites_group.draw(window)

        # refresh screen
        all_sprites_group.update()
        clock.tick(60)
        if update:
            pygame.display.flip()
