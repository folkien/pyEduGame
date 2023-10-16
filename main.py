import pygame
import random
from enum import Enum

from helpers.equations import Equation, generate_equation_add, generate_equation_divide_int, generate_equation_multiply, generate_equation_sub_positive

class GameOptions(str, Enum):
    ''' Game options enum'''
    GameAddSub = "Dodawanie i Odejmowanie"
    GameMultiply = "Mnożenie"
    GameDivide = "Dzielenie"



pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH, HEIGHT = 1280, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Game for Kids")

# Game : Fonts
font_small = pygame.font.Font(None, 32)
font_large = pygame.font.Font(None, 64)
font_huge = pygame.font.Font(None, 168)

# Game : Images
star_img = pygame.image.load("star.png")
boy_img = pygame.image.load("schoolboy.png")
boy_img_sad = pygame.image.load("schoolboy_sad.png")

def draw_stars(stars : int):
    ''' Draw stars in the top left corner '''
    # Draw stars count.
    txt_surface = font_large.render(f"{stars}", True, BLACK)
    screen.blit(txt_surface, (10, 10))

    # Draw stars images.
    for i in range(stars):
        screen.blit(star_img, (10 + i*50, 10))

def draw_equation(equation : Equation, user_input : str, color=BLACK):
    ''' Draw equation in the middle of the screen'''
    eq_surface = font_huge.render(f"{equation.equation}{user_input}", 
                                  True, 
                                  color)
    screen.blit(eq_surface, (WIDTH//3, HEIGHT//2))

def draw_menu(options : list, selected_idx : int):
    ''' Draw menu in the middle of the screen'''
    for i, option in enumerate(options):
        color = BLACK if i == selected_idx else (150, 150, 150)
        txt_surface = font_large.render(option, True, color)
        screen.blit(txt_surface, (WIDTH//2 - txt_surface.get_width()//2, HEIGHT//2 + i*40 - txt_surface.get_height()//2))

def draw_boy_study():
    ''' Draw boy in the bottom left corner'''
    screen.blit(boy_img, (0, 80))

def draw_boy_happy():
    ''' Draw boy in the bottom left corner'''
    screen.blit(boy_img, (0, 80))

def draw_boy_sad():
    ''' Draw boy sad in the bottom left corner'''
    screen.blit(boy_img_sad, (0, 80))

def on_success():
    ''' Success animation'''
    draw_equation(equation, user_input, GREEN)
    draw_boy_happy()
    pygame.display.flip()
    pygame.time.delay(500)

def on_failure():
    ''' Failure animation'''
    draw_equation(equation, user_input, RED)
    draw_boy_sad()
    pygame.display.flip()
    pygame.time.delay(500)


def GameOptionProcess(option :GameOptions):
    ''' Process game option'''
    if (option == GameOptions.GameAddSub):
        if (random.randint(0, 1) == 0):
            return generate_equation_sub_positive()
        else:
            return generate_equation_add()

    elif (option == GameOptions.GameMultiply):
        return generate_equation_multiply()

    elif (option == GameOptions.GameDivide):
        return generate_equation_divide_int()

running = True
in_menu = True
selected_idx = 0
stars = 0
equation = None
user_input = ""
# List of possible game options
options = [ option for option in GameOptions]

while running:
    screen.fill(WHITE)


    # Menu : Keyboard navigation
    if in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_idx = (selected_idx + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected_idx = (selected_idx - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    in_menu = False
        draw_menu(options, selected_idx)

    # Game : Keyboard input
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.K_ESCAPE:
                in_menu = True
                continue
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isnumeric():
                    user_input += event.unicode
                elif event.key == pygame.K_RETURN:
                    # Check : if equation is None
                    if (equation is None):
                        continue

                    # Check : if user input is empty
                    if (user_input == ""):
                        continue

                    # Check : if equation is correct
                    if (equation.answer == int(user_input)):
                        stars += 1
                        on_success()
                    # Check : Failure
                    else:
                        stars = max(0, stars-1)
                        on_failure()

                    # Reset
                    equation = None
                    user_input = ""
                # Backspace : Correction
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

        # Game Option processing
        if (equation is None):
            equation = GameOptionProcess(options[selected_idx])

        # Drawing
        draw_stars(stars)
        draw_equation(equation, user_input)
        draw_boy_happy()
    
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()

