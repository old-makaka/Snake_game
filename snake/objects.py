import pygame
import random

import Globals


class Lake:

    def __init__(self, x, y, type_):
        self.lake_pixels = []

        if type_ == 'round':
            for i in [-40, -20, 0, 20, 40]:
                for j in [-40, -20, 0, 20, 40]:
                    if -60 < i + j < 60:
                        self.lake_pixels.append([i + x, j + y])

        if type_ == 'big':
            for i in [-60, -40, -20, 0, 20, 40, 60]:
                for j in [-60, -40, -20, 0, 20, 40, 60]:
                    if -120 < i + j < 120:
                        self.lake_pixels.append([i + x, j + y])

        if type_ == 'long':
            for i in [-60, -40, -20, 0, 20, 40, 60]:
                for j in [-60, -40, -20, 0, 20, 40, 60]:
                    if -40 < i - j < 40:
                        self.lake_pixels.append([i + x, j + y])

    def visualize(self):
        for pixel in self.lake_pixels:
            pygame.draw.rect(Globals.sc, Globals.water, [pixel[0], pixel[1], 20, 20])


class Rock:

    def __init__(self, ban):
        ok = False
        x_ = 0
        y_ = 0
        while not ok:
            ok = True
            x_ = random.randint(0, 37) * 20 + 20
            y_ = random.randint(0, 23) * 20 + 100
            for a in ban:
                if a[0] == x_ and a[1] == y_:
                    ok = False
        self.x = x_
        self.y = y_

    def visualize(self):
        pygame.draw.rect(Globals.sc, Globals.snake2_gray, [self.x, self.y, 20, 20])


class Bonus:

    def __init__(self, ban):

        ok = False
        x = 0
        y = 0
        while not ok:
            ok = True
            x = random.randint(0, 37) * 20 + 20
            y = random.randint(0, 23) * 20 + 100
            for a in ban:
                if a[0] == x and a[1] == y:
                    ok = False
        self.bonus_pixels = [x, y]


class Apple(Bonus):

    def visualize(self):
        x_ = self.bonus_pixels[0]
        y_ = self.bonus_pixels[1]
        pygame.draw.circle(Globals.sc, Globals.red, [x_ + 10, y_ + 10], 9)
        pygame.draw.polygon(Globals.sc, Globals.brown, [[x_ + 4, y_], [x_ + 12, y_ + 2], [x_ + 10, y_ + 8]])


class Star(Bonus):

    def visualize(self):
        x_ = self.bonus_pixels[0]
        y_ = self.bonus_pixels[1]
        pygame.draw.polygon(Globals.sc, Globals.black, [[x_ + 10, y_], [x_ + 12, y_ + 6], [x_ + 20, y_ + 6],
                                                        [x_ + 14, y_ + 12], [x_ + 16, y_ + 20], [x_ + 10, y_ + 14],
                                                        [x_ + 5, y_ + 20], [x_ + 8, y_ + 12], [x_, y_ + 6],
                                                        [x_ + 8, y_ + 6]])


def screen_visualize(type_, level, total_score, total_time):

    if type_ == 'start':
        out = Globals.font2.render('WELCOME TO THE SNAKE GAME!', True, Globals.text)
        Globals.sc.blit(out, [130, 200])
        out = Globals.font1.render('You need to pass 5 levels to win', True, Globals.text)
        Globals.sc.blit(out, [250, 280])
        out = Globals.font1.render('Press "SPACE" button to continue', True, Globals.snake2)
        Globals.sc.blit(out, [240, 340])
        out = Globals.font1.render('Press "L" key to show leaderboard', True, Globals.snake2)
        Globals.sc.blit(out, [239, 380])

    if type_ == 'colour_choice':
        out = Globals.font2.render('CHOOSE SNAKE COLOUR', True, Globals.text)
        Globals.sc.blit(out, [160, 100])
        x = 350
        y = 250
        pygame.draw.polygon(Globals.sc, Globals.snake1, [[x + 16, y], [x + 64, y],
                                                         [x + 80, y + 16], [x + 80, y + 64],
                                                         [x + 64, y + 80], [x + 16, y + 80],
                                                         [x, y + 64], [x, y + 16]])
        pygame.draw.circle(Globals.sc, Globals.snake2, [x + 40, y + 40], 32)
        pygame.draw.polygon(Globals.sc, Globals.text, [[x - 30, y + 10], [x - 30, y + 70], [x - 70, y + 40]])
        pygame.draw.polygon(Globals.sc, Globals.text, [[x + 110, y + 10], [x + 110, y + 70], [x + 150, y + 40]])
        out = Globals.font1.render('Press "SPACE" button to continue', True, Globals.snake2)
        Globals.sc.blit(out, [240, 400])
        out = Globals.font1.render('Press "L" key to show leaderboard', True, Globals.snake2)
        Globals.sc.blit(out, [239, 450])

    if type_ == 'level':
        out = Globals.font3.render('LEVEL ' + str(level), True, Globals.text)
        Globals.sc.blit(out, [305, 200])
        out = Globals.font1.render('Current score: ' + str(total_score), True, Globals.text)
        Globals.sc.blit(out, [320, 300])
        out = Globals.font1.render('Press "SPACE" button to start the game', True, Globals.snake2)
        Globals.sc.blit(out, [220, 350])

    if type_ == 'win':
        out = Globals.font2.render('CONGRATULATIONS! YOU WIN!', True, Globals.text)
        Globals.sc.blit(out, [130, 160])
        out = Globals.font1.render('Total score: ' + str(total_score), True, Globals.text)
        Globals.sc.blit(out, [320, 240])
        out = Globals.font1.render('Total time: ' + str(total_time), True, Globals.text)
        Globals.sc.blit(out, [320, 300])
        out = Globals.font1.render('Press "Q" key to quit or "R" key to restart', True, Globals.snake2)
        Globals.sc.blit(out, [210, 360])
        out = Globals.font1.render('Press "L" key to show leaderboard', True, Globals.snake2)
        Globals.sc.blit(out, [230, 400])

    if type_ == 'loose':
        out = Globals.font2.render('YOU LOST!', True, Globals.text)
        Globals.sc.blit(out, [290, 160])
        out = Globals.font1.render('Total score: ' + str(total_score), True, Globals.text)
        Globals.sc.blit(out, [320, 220])
        out = Globals.font1.render('Total time: ' + str(total_time), True, Globals.text)
        Globals.sc.blit(out, [320, 280])
        out = Globals.font1.render('Press "Q" key to quit or "R" key to restart', True, Globals.snake2)
        Globals.sc.blit(out, [210, 340])
        out = Globals.font1.render('Press "L" key to show leaderboard', True, Globals.snake2)
        Globals.sc.blit(out, [230, 380])

    if type_ == 'leaderboard':
        out = Globals.font2.render('LEADERBOARD', True, Globals.text)
        Globals.sc.blit(out, [280, 100])
        out = Globals.font1.render('position', True, Globals.text)
        Globals.sc.blit(out, [100, 150])
        out = Globals.font1.render('score', True, Globals.text)
        Globals.sc.blit(out, [300, 150])
        out = Globals.font1.render('time', True, Globals.text)
        Globals.sc.blit(out, [450, 150])
        with open('leaderboard.txt', 'r') as lb:
            for line in lb.readlines():
                line = line.split()
                out = Globals.font1.render(line[0], True, Globals.text)
                Globals.sc.blit(out, [100, 150 + int(line[0]) * 40])
                out = Globals.font1.render(line[1], True, Globals.text)
                Globals.sc.blit(out, [300, 150 + int(line[0]) * 40])
                out = Globals.font1.render(line[2], True, Globals.text)
                Globals.sc.blit(out, [450, 150 + int(line[0]) * 40])
        out = Globals.font1.render('Press "SPACE" button to continue', True, Globals.snake2)
        Globals.sc.blit(out, [240, 450])


def leaderboard_update(total_score, total_time):
    leader = False
    l_ = len(Globals.leaderboard)

    print(Globals.leaderboard)
    for i in range(l_):
        if total_score >= Globals.leaderboard[i + 1][0]:
            for j in range(min(5, l_), i, -1):
                Globals.leaderboard[j + 1] = [Globals.leaderboard[j][0], Globals.leaderboard[j][1]]
            Globals.leaderboard[i + 1] = [total_score, total_time]
            leader = True
            break

    print(Globals.leaderboard)
    if not leader and l_ < 5:
        Globals.leaderboard[l_ + 1] = [total_score, total_time]

    with open('leaderboard.txt', 'w') as lb:
        for i in range(len(Globals.leaderboard)):
            lb.write(str(i + 1) + ' ' + str(Globals.leaderboard[i + 1][0]) + ' '
                     + str(Globals.leaderboard[i + 1][1]) + '\n')


def screen_show(type_, level, total_score, total_time):
    wait = True
    while wait:

        Globals.sc.fill(Globals.light_gray)
        screen_visualize(type_, level, total_score, total_time)
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and type_ == 'colour_choice':
                mouse = pygame.mouse.get_pos()

                if (280 < mouse[0] < 330) and (260 < mouse[1] < 320):
                    if Globals.snake1 == Globals.snake1_green:
                        Globals.snake1 = Globals.snake1_red
                        Globals.snake2 = Globals.snake2_red
                    elif Globals.snake1 == Globals.snake1_red:
                        Globals.snake1 = Globals.snake1_gray
                        Globals.snake2 = Globals.snake2_gray
                    elif Globals.snake1 == Globals.snake1_gray:
                        Globals.snake1 = Globals.snake1_green
                        Globals.snake2 = Globals.snake2_green

                if (460 < mouse[0] < 500) and (260 < mouse[1] < 320):
                    if Globals.snake1 == Globals.snake1_green:
                        Globals.snake1 = Globals.snake1_gray
                        Globals.snake2 = Globals.snake2_gray
                    elif Globals.snake1 == Globals.snake1_red:
                        Globals.snake1 = Globals.snake1_green
                        Globals.snake2 = Globals.snake2_green
                    elif Globals.snake1 == Globals.snake1_gray:
                        Globals.snake1 = Globals.snake1_red
                        Globals.snake2 = Globals.snake2_red

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_SPACE and (type_ == 'start' or type_ == 'level' or type_ == 'colour_choice'):
                    wait = False

                if event.key == pygame.K_SPACE and type_ == 'leaderboard':
                    wait = False

                if event.key == pygame.K_l and type_ != 'level':
                    screen_show('leaderboard', level, total_score, total_time)
                    screen_show(type_, level, total_score, total_time)
                    wait = False

                if event.key == pygame.K_r and (type_ == 'win' or type_ == 'loose'):
                    wait = False
