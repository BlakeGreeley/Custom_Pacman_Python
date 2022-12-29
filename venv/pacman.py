from turtle import width
import pygame
from board import boards
import math

pygame.init()

WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
level = boards
color = 'orange'
PI = math.pi

def draw_board(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            
            # each design application on the board from 1-9 spaces v

            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                (j * num2 + num2, i * num1 + (0.5*num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.5)), (i * num1 + (0.5*num1)), num2, num1], 0, PI/2, 3)

            if level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.5)), (i * num1 + (0.5*num1)), num2, num1], 0, 2/PI, 3)
            
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                (j * num2 + num2, i * num1 + (0.5*num1)), 3)
            
            # each design application on the board from 1-9 spaces ^
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()