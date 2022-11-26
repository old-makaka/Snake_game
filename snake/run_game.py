import objects


def init():
    import pygame
    import random
    import math

    import Globals

    pygame.init()

    Globals.init_colours()
    Globals.init_fonts()
    Globals.init_screen()
    Globals.init_leaderboard()

    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    score_level = [5, 10, 20, 40, 60]

    def score_draw(score, score_level_, level):
        out = Globals.font1.render('Your score: ' + str(score) + ' / ' +
                                   str(score_level_[level - 1]), True, Globals.text)
        Globals.sc.blit(out, [20, 10])

    def time_draw(t):
        out = Globals.font1.render('Time: ' + str(t), True, Globals.text)
        Globals.sc.blit(out, [20, 50])

    def level_draw(level):
        out = Globals.font1.render('Level: ' + str(level), True, Globals.text)
        Globals.sc.blit(out, [700, 10])

    def snake_draw(snake):
        for i in range(len(snake)):
            x = snake[i][0]
            y = snake[i][1]
            pygame.draw.polygon(Globals.sc, Globals.snake1, [[x + 4, y], [x + 16, y],
                                                             [x + 20, y + 4], [x + 20, y + 16],
                                                             [x + 16, y + 20], [x + 4, y + 20],
                                                             [x, y + 16], [x, y + 4]])
            if i != 0:
                pygame.draw.circle(Globals.sc, Globals.snake2, [x + 10, y + 10], 8)

    def loop():
        total_score = 0
        total_time = 0
        alive = True
        for level in range(1, 6):

            if not alive:
                break

            objects.screen_show('level', level, total_score, total_time)

            head = [0, 0]
            head[0] = random.randint(0, 37) * 20 + 20
            head[1] = random.randint(0, 23) * 20 + 100

            snake = list()
            snake.append([head[0], head[1]])
            apple = objects.Apple(snake)
            star_exist = False
            star = None

            t1 = pygame.time.get_ticks()
            time = 0
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

                ban = snake + [apple.bonus_pixels]
                if star_exist:
                    ban += [star.bonus_pixels]

                head[0] += x_change
                head[1] += y_change
                if head[0] < 0 or head[0] > 760 or head[1] < 100 or head[1] > 560:
                    alive = False
                    break

                fed = False
                if head[0] == apple.bonus_pixels[0] and head[1] == apple.bonus_pixels[1]:
                    score += 1
                    apple = objects.Apple(ban)
                    if random.randint(1, 10) == 5:
                        star_exist = True
                        star = objects.Star(ban)
                    else:
                        star_exist = False
                    fed = True

                if star_exist and head[0] == star.bonus_pixels[0] and head[1] == star.bonus_pixels[1]:
                    score += 5
                    star_exist = False

                snake.insert(0, [head[0], head[1]])
                if not fed:
                    snake.pop()

                for a in snake[1:]:
                    if a == head:
                        alive = False
                        break

                t2 = pygame.time.get_ticks()
                time = (t2 - t1) // 1000

                Globals.sc.fill(Globals.white)
                pygame.draw.rect(Globals.sc, Globals.sand, (20, 100, 760, 480))
                snake_draw(snake)
                score_draw(score, score_level, level)
                level_draw(level)
                time_draw(time)
                apple.visualize()
                if star_exist:
                    star.visualize()
                pygame.display.update()
                clock.tick(int(5 + math.sqrt(level) * math.sqrt(score)))

            total_score += score
            total_time += time

        objects.leaderboard_update(total_score, total_time)

        if alive:
            objects.screen_show('win', 0, total_score, total_time)

        else:
            objects.screen_show('loose', 0, total_score, total_time)

        loop()

    objects.screen_show('start', 0, 0, 0)
    objects.screen_show('colour_choice', 0, 0, 0)

    loop()

    pygame.quit()
    quit()
