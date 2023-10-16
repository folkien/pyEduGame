import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH, HEIGHT = 1280, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Game for Kids")
font_small = pygame.font.Font(None, 32)
font_large = pygame.font.Font(None, 64)
font_huge = pygame.font.Font(None, 128)

star_img = pygame.image.load("star.png")
boy_img = pygame.image.load("schoolboy.png")

def draw_stars(stars):
    for i in range(stars):
        screen.blit(star_img, (10 + i*50, 10))

def draw_equation(equation, color=BLACK):
    eq_surface = font_huge.render(equation, True, color)
    screen.blit(eq_surface, (WIDTH//3, HEIGHT//2))

def draw_menu(options, selected_idx):
    for i, option in enumerate(options):
        color = BLACK if i == selected_idx else (150, 150, 150)
        txt_surface = font_large.render(option, True, color)
        screen.blit(txt_surface, (WIDTH//2 - txt_surface.get_width()//2, HEIGHT//2 + i*40 - txt_surface.get_height()//2))

def draw_boy():
    screen.blit(boy_img, (0, 80))

def on_success():
    draw_equation(equation + user_input, GREEN)
    pygame.display.flip()
    pygame.time.delay(1000)

def on_failure():
    draw_equation(equation + user_input, RED)
    pygame.display.flip()
    pygame.time.delay(1000)

running = True
in_menu = True
selected_idx = 0
stars = 0
equation = "2 + 2 = "
user_input = ""
options = ["Dodawanie i Odejmowanie", "Mnożenie", "Dzielenie"]

while running:
    screen.fill(WHITE)

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
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isnumeric():
                    user_input += event.unicode
                elif event.key == pygame.K_RETURN:
                    if eval(equation[:-2]) == int(user_input):
                        stars += 1
                        on_success()
                    else:
                        stars = max(0, stars-1)
                        on_failure()

                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    if options[selected_idx] == "Dodawanie i Odejmowanie":
                        op = random.choice(["+", "-"])
                    elif options[selected_idx] == "Mnożenie":
                        op = "*"
                    elif options[selected_idx] == "Dzielenie":
                        op = "//"
                        while b == 0 or a % b != 0: 
                            a = random.randint(1, 10)
                            b = random.randint(1, 10)
                    equation = f"{a} {op} {b} = "
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

        draw_stars(stars)
        draw_equation(equation + user_input)
        draw_boy()
    
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()

