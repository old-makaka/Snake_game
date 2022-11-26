import pygame

black = None
sand = None
yellow = None
snake1_green = None
snake2_green = None
snake1_red = None
snake2_red = None
snake1_gray = None
snake2_gray = None
white = None
text = None
red = None
brown = None
water = None
light_gray = None
snake1 = None
snake2 = None

sc = None

font1 = None
font2 = None
font3 = None
font4 = None

leaderboard = {}


def init_colours():
    global black, sand, white, text, red, brown, water, light_gray, snake1, snake2, yellow
    global snake1_green, snake2_green, snake1_red, snake2_red, snake1_gray, snake2_gray
    black = (0, 0, 0)
    sand = (245, 195, 125)
    snake1_green = (112, 186, 60)
    snake2_green = (46, 133, 46)
    snake1_red = (212, 49, 13)
    snake2_red = (179, 0, 0)
    snake1_gray = (112, 112, 112)
    snake2_gray = (80, 80, 80)
    white = (255, 255, 255)
    text = (60, 60, 60)
    red = (189, 26, 26)
    brown = (51, 16, 17)
    water = (0, 128, 192)
    light_gray = (220, 220, 220)
    yellow = (255, 255, 36)
    snake1 = snake1_green
    snake2 = snake2_green


def init_screen():
    global sc
    sc = pygame.display.set_mode((800, 600))


def init_fonts():
    global font1, font2, font3, font4
    font1 = pygame.font.SysFont('freesanbold.ttf', 30)
    font2 = pygame.font.SysFont('freesanbold.ttf', 50)
    font3 = pygame.font.SysFont('freesanbold.ttf', 70)
    font4 = pygame.font.SysFont('freesanbold.ttf', 20)


def init_leaderboard():
    global leaderboard
    with open("leaderboard.txt", "r") as lb:
        for line in lb.readlines():
            n, leader_score, leader_time = map(int, line.split())
            leaderboard[n] = [leader_score, leader_time]
