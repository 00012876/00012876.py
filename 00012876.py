#source https://www.edureka.co/blog/snake-game-with-pygame/
#Task:
# Demonstrate your knowledge of Python by modifying a small simple game, “Hungry Snake”, where you need to demonstrate your knowledge of
# python syntax, use of 3 different data types, conditionals, loop, functions. Well commented and organised code will receive higher marks.
# Procedural or object-oriented approach to programming is appreciated. Modifications can include input from the  user, adding different levels
# with increasing difficulty, more snakes on screen, snakes with changing colours. Use your creativity!
#
# The code examples should be pushed to a private git repository.


from pygame import *
#creating the menu
init()

size = (1000, 800)
screen = display.set_mode(size)
#font of menu
ARIAL_50 = font.SysFont('arial', 50)


class Menu:
    def __init__(self):
        self._options = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._options.append(ARIAL_50.render(option, True, (255, 255, 0)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._options) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._options):
            option_rect: Rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)


running = True


def quit_game():
    global running
    running = False

#menu's functions
menu = Menu()
menu.append_option('press SPACE to start', quit_game)
menu.append_option('QUIT', quit_game)
#menu control
while running:
    for e in event.get():
        if e.type == QUIT:
            quit_game()
        if e.type == KEYDOWN:
            if e.key == K_w:
                menu.switch(-1)
            elif e.key == K_s:
                menu.switch(1)
            elif e.key == K_SPACE:
                menu.select()

    screen.fill((0, 191, 255))

    menu.draw(screen, 100, 100, 75)

    display.flip()

import pygame
import time
import random

pygame.init()
#change colors
white = (255, 255, 255)
yellow = (255, 255, 10)
black = (0, 100, 0)
red = (213, 255, 80)
green = (30, 255, 30)
blue = (50, 153, 213)
#change space
dis_width = 1000
dis_height = 800
#change name of the game
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('00012876 snake')

clock = pygame.time.Clock()
#snake's speed
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 45)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
#message after lose
        while game_close == True:
            dis.fill(blue)
            message("You fail! Press R-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
#control after lose
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
#game control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
#eating apples
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 2

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()