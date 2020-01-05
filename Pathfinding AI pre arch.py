import os, random, pygame
#from pygame import *
pygame.init()

display_width = 1250
display_height = 650

os.environ['SDL_VIDEO_CENTERED'] = '1'
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(("Pathfinding AI"))    # Setup Window


run = True
gamestate = 'mainm'    # mainm == Main menu, ing == In game

image_title = pygame.image.load('Title.png')
image_play_button_unpressed = pygame.image.load('Play Button Unpressed.png')    # Preload Image Assets
image_play_button_pressed = pygame.image.load('Play Button Pressed.png')
image_play_button = image_play_button_unpressed

frame = pygame.time.Clock()    # Setup Tick Function


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
    
    global gamestate    
    gamestate = 'playing'    # Set Gamestate

    grid = []

    rows = 30
    columns = 20

    for row in range(rows):    # Initialise Grid

        grid.append([])

        for column in range(columns):

            grid[row].append(0)




        
button_play = button((display_width / 2 - 100), (display_height / 2 - 125), 200, 100)    # Setup Buttons

while run:    # Main Loop

    frame.tick(30)    # Lock To Max 30 FPS/Ticks
    #pygame.time.delay(10)

    pygame.display.update()
    display.fill((60,60,60))

    for event_l in pygame.event.get():
        #print(event.type)
        pos = pygame.mouse.get_pos()
        if event_l.type == pygame.QUIT:
            pygame.quit()
            quit()


    if gamestate == 'mainm':    # Main Menu


        display.blit(image_title, (display_width / 2 - 325, display_height / 2 - 275))    # Display Title

        button_play.draw(image_play_button)



        for event in pygame.event.get():    # Pygame Events indent
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                
                if button_play.is_over(pos):
                    
                    print("clicked")
                    play()
                    print(gamestate)


                    
        
            if event.type == pygame.MOUSEMOTION:
                if button_play.is_over(pos) == True:
                    image_play_button = image_play_button_pressed
                else:
                    image_play_button = image_play_button_unpressed



    if gamestate == 'playing':
        print("c")

                        



