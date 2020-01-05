import os
import random
import pygame
#from pygame import *
pygame.init()

display_width = 1255
display_height = 655

os.environ['SDL_VIDEO_CENTERED'] = '1'
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(("Pathfinding AI"))    # Setup Window


run = True
gamestate = 'mainm'    # mainm == Main menu, ing == In game

image_title = pygame.image.load('Title.png')
image_play_button_unpressed = pygame.image.load(
    'Play Button Unpressed.png')    # Preload Image Assets
image_play_button_pressed = pygame.image.load('Play Button Pressed.png')
image_play_button = image_play_button_unpressed

frame = pygame.time.Clock()    # Setup Tick Function

global colour
colour = random.randint(0, 255)


class button():
    def __init__(self, x, y, width, height):    # Create Button Class

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, image):

        display.blit(image, (self.x, self.y))

    def is_over(self, pos):

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:

                return True

        return False


def play():

    global gamestate, grid, rows, columns
    gamestate = 'playing'    # Set Gamestate

    grid = []

    rows = 13
    columns = 26

    for row in range(rows):    # Initialise Grid

        grid.append([])

        for column in range(columns):

            grid[row].append(0)

    grid[0][1] = 1


def draw_grid():

        # 45 x 45 Is Square Size
        # 5  x 5  Is Line Size

                                                                                        # Border
    pygame.draw.rect(display, (0, 0, 0), (0, 0, display_width, 5))
    pygame.draw.rect(display, (0, 0, 0), (0, display_height - 5, display_width, 5))
    pygame.draw.rect(display, (0, 0, 0), (0, 0, 5, display_height))
    pygame.draw.rect(display, (0, 0, 0), (display_width - 5, 0, 5, display_height))

    for num in range(columns):

        pygame.draw.rect(display, (0, 0, 0), (num * 50, 0, 5, display_height))    # Columns

    for num in range(rows):

        pygame.draw.rect(display, (0, 0, 0), (0, num * 50, display_width, 5))    # Rows

    for row_gen in range(rows):
        for column_gen in range(columns):

            if grid[row_gen][column_gen] == 0:

                pygame.draw.rect(display, (255, 255, 255), (((column_gen * 50) + 5), 5, 45, 45))

                pygame.draw.rect(display, (colour, 255, 255), (5, ((row_gen * 50) + 5), 45, 45))

            if grid[row_gen][column_gen] == 1:

                pygame.draw.rect(display, (0, 0, 0), (5, ((row_gen * 50) + 5), 45, 45))


button_play = button((display_width / 2 - 100), (display_height / 2 - 125),
                     200, 100)    # Setup Buttons

while run:    # Main Loop

    frame.tick(30)    # Lock To Max 30 FPS/Ticks

    pygame.display.update()
    display.fill((60, 60, 60))

    for event in pygame.event.get():    # Event Handler

        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if gamestate == 'mainm':    # Main Menu Events

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if button_play.is_over(pos):

                    play()
                    print(gamestate)
                    print(grid)

            if event.type == pygame.MOUSEMOTION:
                if button_play.is_over(pos) == True:
                    image_play_button = image_play_button_pressed
                else:
                    image_play_button = image_play_button_unpressed

    if gamestate == 'mainm':    # Main Menu

        display.blit(image_title, (display_width / 2 - 325,
                                   display_height / 2 - 275))    # Display Title

        button_play.draw(image_play_button)

    if gamestate == 'playing':

        draw_grid()
        colour = random.randint(0, 255)
