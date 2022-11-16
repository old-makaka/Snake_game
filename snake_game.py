import pygame
import random
import math

pygame.init()

black = (0, 0, 0)
sand = (245, 195, 125)
snake1 = (112, 186, 60)
snake2 = (46, 133, 46)
white = (255, 255, 255)
text = (60, 60, 60)
red = (189, 26, 26)
brown = (51, 16, 17)
water = (0, 128, 192)
light_gray = (220, 220, 220)

sc = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

field = (20, 100, 780, 580)

font1 = pygame.font.SysFont('freesanbold.ttf', 30)
font2 = pygame.font.SysFont('freesanbold.ttf', 50)
font3 = pygame.font.SysFont('freesanbold.ttf', 70)

score_level = [5, 10, 20, 40, 60]


def score_draw(score, score_level, level):
    out = font1.render('Your score: ' + str(score) + ' / ' + str(score_level[level - 1]), True, text)
    sc.blit(out, [20, 10])


def time_draw(t):
    out = font1.render('Time: ' + str(t), True, text)
    sc.blit(out, [20, 50])


def level_draw(level):
    out = font1.render('Level: ' + str(level), True, text)
    sc.blit(out, [700, 10])


def snake_draw(snake):
    for i in range(len(snake)):
        x = snake[i][0]
        y = snake[i][1]
        pygame.draw.polygon(sc, snake1, [[x + 4, y], [x + 16, y], [x + 20, y + 4], [x + 20, y + 16],
                                         [x + 16, y + 20], [x + 4, y + 20], [x, y + 16], [x, y + 4]])
        if i != 0:
            pygame.draw.circle(sc, snake2, [x + 10, y + 10], 8)


def apple_draw(apple):
    x = apple[0]
    y = apple[1]
    pygame.draw.circle(sc, red, [x + 10, y + 10], 9)
    pygame.draw.polygon(sc, brown, [[x + 4, y], [x + 12, y + 2], [x + 10, y + 8]])


def gen_apple(ap, s):
    ok = False
    while not ok:
        ok = True
        ap[0] = random.randint(0, 37) * 20 + 20
        ap[1] = random.randint(0, 23) * 20 + 100
        for a in s:
            if a[0] == ap[0] and a[1] == ap[1]:
                ok = False


def start_screen_draw():
    out = font2.render('WELCOME TO THE SNAKE GAME!', True, text)
    sc.blit(out, [130, 200])
    out = font1.render('You need to pass 5 levels to win', True, text)
    sc.blit(out, [250, 280])
    out = font1.render('Press "SPACE" button to continue', True, snake2)
    sc.blit(out, [240, 340])


def start_level_screen_draw(level, total_score):
    out = font3.render('LEVEL ' + str(level), True, text)
    sc.blit(out, [305, 200])
    out = font1.render('Current score: ' + str(total_score), True, text)
    sc.blit(out, [320, 300])
    out = font1.render('Press "SPACE" button to start the game', True, snake2)
    sc.blit(out, [230, 350])


def end_win_screen_draw(total_score, total_time):
    out = font2.render('CONGRATULATIONS! YOU WIN!', True, text)
    sc.blit(out, [130, 160])
    out = font1.render('Total score: ' + str(total_score), True, text)
    sc.blit(out, [320, 240])
    out = font1.render('Total time: ' + str(total_time), True, text)
    sc.blit(out, [320, 300])
    out = font1.render('Press "q" key to quit or "r" key to restart', True, snake2)
    sc.blit(out, [210, 360])


def end_loose_screen_draw(total_score, total_time):
    out = font2.render('YOU LOST!', True, text)
    sc.blit(out, [290, 160])
    out = font1.render('Total score: ' + str(total_score), True, text)
    sc.blit(out, [320, 220])
    out = font1.render('Total time: ' + str(total_time), True, text)
    sc.blit(out, [320, 280])
    out = font1.render('Press "q" key to quit or "r" key to restart', True, snake2)
    sc.blit(out, [210, 340])


def loop():
    total_score = 0
    total_time = 0
    alive = True
    for level in range(1, 6):

        if not alive:
            break

        level_started = False
        while not level_started:
            sc.fill(light_gray)
            start_level_screen_draw(level, total_score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        level_started = True

        head = [0, 0]
        head[0] = random.randint(0, 37) * 20 + 20
        head[1] = random.randint(0, 23) * 20 + 100

        apple = [0, 0]
        snake = list()
        snake.append([head[0], head[1]])
        gen_apple(apple, snake)

        t1 = pygame.time.get_ticks()
        score = 0
        x_change = 0
        y_change = 0

        while alive and score < score_level[level - 1]:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        x_change = -20
                        y_change = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        x_change = 20
                        y_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        y_change = -20
                        x_change = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        y_change = 20
                        x_change = 0

            head[0] += x_change
            head[1] += y_change
            if head[0] < 0 or head[0] > 760 or head[1] < 100 or head[1] > 560:
                alive = False
                break

            fed = False
            if head[0] == apple[0] and head[1] == apple[1]:
                score += 1
                gen_apple(apple, snake)
                fed = True

            snake.insert(0, [head[0], head[1]])
            if not fed:
                snake.pop()

            for a in snake[1:]:
                if a == head:
                    alive = False
                    break

            t2 = pygame.time.get_ticks()
            time = (t2 - t1) // 1000

            sc.fill(white)
            pygame.draw.rect(sc, sand, (20, 100, 760, 480))
            snake_draw(snake)
            score_draw(score, score_level, level)
            level_draw(level)
            time_draw(time)
            apple_draw(apple)
            pygame.display.update()
            clock.tick(int(5 + math.sqrt(level) * math.sqrt(score)))

        total_score += score
        total_time += time

    if alive:
        while True:
            sc.fill(light_gray)
            end_win_screen_draw(total_score, total_time)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return
                    if event.key == pygame.K_r:
                        loop()
                        return

    else:
        while True:
            sc.fill(light_gray)
            end_loose_screen_draw(total_score, total_time)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return
                    if event.key == pygame.K_r:
                        loop()
                        return


started = False
while not started:
    sc.fill(light_gray)
    start_screen_draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True

loop()

pygame.quit()
quit()
