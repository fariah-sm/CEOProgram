"""
title: smiley
author: Fariah Mahmood
date: 7/20/18 9:42 AM
"""

# -*- coding: utf-8 -*-


import pygame


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (246, 226, 51)
PLANT = (0, 153, 0)


PI = 3.141592653
x_coord, x_speed, y_coord, y_speed = 0, 0, 0, 0
ball_pos_x, ball_pos_y = 380, 380
ball_speed_x, ball_speed_y = 0, 3


size = (700, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Move Stick Figure")


done = False
clock = pygame.time.Clock()


def draw_stick_figure(screen, x, y):
    pygame.draw.circle(screen, YELLOW, [200 + x, 200 + y], 150)
    pygame.draw.line(screen, BLACK, [250 + x, 125 + y], [250 + x, 175 + y], 5)
    pygame.draw.line(screen, BLACK, [150 + x, 125 + y], [150 + x, 175 + y], 5)
    pygame.draw.arc(screen, BLACK, [95 + x, 155 + y, 215, 100], PI, 0, 2)
    pygame.draw.line(screen, YELLOW, [200 + x, 350 + y], [200 + x, 400 + y], 5)
    pygame.draw.line(screen, YELLOW, [200 + x, 375 + y], [50 + x, 300 + y], 5)  # R ARM
    pygame.draw.line(screen, YELLOW, [200 + x, 375 + y], [350 + x, 400 + y], 5)  # L ARM
    pygame.draw.line(screen, YELLOW, [375 + x, 500 + y], [200 + x, 400 + y], 5)  # L LEG
    pygame.draw.line(screen, YELLOW, [25 + x, 500 + y], [200 + x, 400 + y], 5)  # R LEG


def draw_basketball(screen, x, y):
    pygame.draw.circle(screen, BLUE, [x, y], 30)
    pygame.draw.circle(screen, YELLOW, [x, y], 20)


while not done:
    if ball_pos_y > (500 + y_coord):
        ball_speed_y = -50
    if ball_pos_y < (300 + y_coord):
        ball_speed_y = 50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -50
            elif event.key == pygame.K_RIGHT:
                x_speed = 50
            elif event.key == pygame.K_UP:
                y_speed = -50
            elif event.key == pygame.K_DOWN:
                y_speed = 50
        elif event.type == pygame.KEYUP:
            x_speed = 0
            y_speed = 0

    screen.fill(WHITE)
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    ball_pos_y = ball_pos_y + ball_speed_y
    ball_pos_x = x_coord + 30

    draw_stick_figure(screen, x_coord, y_coord)
    draw_basketball(screen, ball_pos_x, ball_pos_y)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
