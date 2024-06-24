import math
import random
import pygame
from utils import draw_arc_line

W, H = 800, 700
DELTA = 100
POINTS = 10

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption(f'DELTA = {DELTA} POINTS = {POINTS}')

execution, points, color_surface, debug = True, [], None, False
while execution:
    screen.fill((200, 200, 200))

    if color_surface:
        screen.blit(color_surface, (0, 0))

    for i in range(len(points)):
        draw_arc_line(screen, *points[i], *points[(i + 1) % len(points)], *points[(i + 2) % len(points)])

    if debug:
        for i in range(len(points)):
            i2 = (i + 1) % len(points)
            pygame.draw.line(screen, (150, 0, 0), points[i], points[i2], 1)

            pygame.draw.circle(screen, (250, 0, 0), points[i], 3)
            pygame.draw.circle(screen, (250, 0, 0), points[i2], 3)

    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            execution = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT and DELTA > 0:
                DELTA -= 10
            if e.key == pygame.K_RIGHT and DELTA < 150:
                DELTA += 10
            if e.key == pygame.K_DOWN and POINTS > 3:
                POINTS -= 1
            if e.key == pygame.K_UP and POINTS < 30:
                POINTS += 1
            if e.key == pygame.K_d:
                debug = not debug

            pygame.display.set_caption(f'DELTA = {DELTA} POINTS = {POINTS}')

            if e.key == pygame.K_RETURN:
                points.clear()
                color_surface = None
                for ang in range(random.randint(0, 360 // POINTS), 360, 360 // POINTS):
                    r = random.randint(H // 3 - DELTA, min(H // 3 + DELTA, H // 2))
                    x = W // 2 + math.cos(math.radians(ang)) * r
                    y = H // 2 + math.sin(math.radians(ang)) * r
                    points.append((int(x), int(y)))

                screen.fill((200, 200, 200))
                for i in range(len(points)):
                    draw_arc_line(screen, *points[i], *points[(i + 1) % len(points)], *points[(i + 2) % len(points)])

                clr = random.choice([(0, 100, 150), (200, 0, 150), (0, 150, 100), (150, 100, 0)])
                color_surface = pygame.Surface((W, H))
                color_surface.fill((200, 200, 200))
                for ang in range(720):
                    mx, my = W // 2, H // 2
                    for r in range(W):
                        mx = int(W // 2 + math.cos(math.radians(ang / 2)) * r)
                        my = int(H // 2 + math.sin(math.radians(ang / 2)) * r)
                        if not (0 <= mx < W and 0 <= my < H and screen.get_at((mx, my)) == (200, 200, 200, 255)):
                            if 0 <= mx < W and 0 <= my < H:
                                pygame.draw.line(color_surface, clr, (W // 2, H // 2), (mx, my), 6)
                            break
