import pygame
from pygame import *
import random
import time

pygame.init()


#sebelum mulai ganti width buat resolusi,
# apple buat makanan,
# player_width untuk besar player,
# speed untuk kecepatan
width = 800
apple_width = 10  # for player too
player_width = 20
speed = 5
window = pygame.display.set_mode((width, width))
clock = pygame.time.Clock()
running = True


snake_head = pygame.Rect(((width - player_width) / 2),
                         ((width - player_width) / 2),
                         player_width,
                         player_width)

apple = pygame.Rect(
    ((width - player_width) + (random.randint(10, width - 10) * time.time())) % width,
    ((width - player_width) + (random.randint(10, width - 10) * time.time())) % width,
    apple_width,
    apple_width)

v = [0, 0]
point = [0, 0]
tails = []
change_to = ''
direction = ''
while running:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            # key movement is from google
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'

            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

            if event.key == K_ESCAPE:
                running = False

        # If two keys pressed simultaneously

        # we don't want snake to move into two

        # directions simultaneously

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'

        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'

        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'

        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        # If two keys pressed simultaneously

        # we don't want snake to move into two

        # directions simultaneously

        # Moving the snake
    if direction == 'UP':
        snake_head[1] -= 10

    if direction == 'DOWN':
        snake_head[1] += 10

    if direction == 'LEFT':
        snake_head[0] -= 10

    if direction == 'RIGHT':
        snake_head[0] += 10

    if snake_head.x > width:
        snake_head.x = 0
    elif snake_head.x < 0:
        snake_head.x = width

    if snake_head.y > width:
        snake_head.y = 0
    elif snake_head.y < 0:
        snake_head.y = width


    if tails:
        for tail in tails:
            if tail[0] == snake_head[0] and tail[1] == snake_head[1]:
                print("You lose!!")
                running = False
    # spawning food again
    apple_spawn_padding = int(width/3)
    apple_center = [

        ((width - apple.w) + (random.randint(apple_spawn_padding, width-apple_spawn_padding) )) % width,
        ((width - apple.h) + (random.randint(apple_spawn_padding, width-apple_spawn_padding) )) % width,
    ]
    collide = snake_head.colliderect(apple)
    # renew the tail with the snake pos
    tails.insert(0, list(snake_head))

    if collide:
        apple.x = apple_center[0]
        apple.y = apple_center[1]
    else:
        tails.pop()

    for tail in tails:
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(tail[0], tail[1], player_width, player_width))

    pygame.draw.rect(window, (255, 255, 255), snake_head)
    pygame.draw.rect(window, (0, 255, 0), apple)
    # move and fps settings

    snake_head.move_ip(v[0] + point[0], v[1] + point[1])

    clock.tick(30)
    pygame.display.update()
