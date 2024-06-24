import math
import random
import pygame
from utils import draw_arc

pygame.init()
screen = pygame.display.set_mode((500, 350))

POINTS = 15
DELTA = 5

execution, points, arcs = True, [], []
while execution:
    screen.fill((200, 200, 200))

    for x, y in points:
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 3)

    if arcs:
        for arc in arcs:
            draw_arc(screen, *arc)

    if len(points) == 3:
        arcs.append((*points[0], *points[1], *points[2]))
        points = draw_arc(screen, *points[0], *points[1], *points[2], _points=points)

    if len(points) == 2:
        draw_arc(screen, *points[0], *points[1], *pygame.mouse.get_pos())

    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            execution = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                x, y = pygame.mouse.get_pos()
                points.append((x, y))
            if e.button == 3:
                points = []

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                POINTS -= 1
            if e.key == pygame.K_RIGHT:
                POINTS += 1
            if e.key == pygame.K_DOWN:
                DELTA -= 1
            if e.key == pygame.K_UP:
                DELTA += 1
            if e.key == pygame.K_r:
                rad, arcs, points, first = 100, [], [], []
                for i in range(1, 360, 360 // POINTS):
                    xr = 250 + math.cos(math.radians(i)) * rad
                    yr = 150 + math.sin(math.radians(i)) * rad
                    points.append((xr, yr))
                    rad += random.randint(-DELTA, DELTA)

                    if i == 1:
                        first = points[0]

                    if len(points) == 3:
                        arcs.append((*points[0], *points[1], *points[2]))
                        points = draw_arc(screen, *points[0], *points[1], *points[2], _points=points)

                points.append(first)
                arcs.append((*points[0], *points[1], *points[2]))
                points.clear()
