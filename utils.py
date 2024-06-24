import math
import pygame


def draw_arc(windows, x1, y1, x2, y2, x3, y3, _points: list = None):
    limit = 10**6

    # Первая прямая
    x1, x2 = (x1, x2) if x1 != x2 else (x1, x2 + 0.1)
    px1, py1 = (x1 + x2) // 2, (y1 + y2) // 2
    k1 = -1 / ((y2 - y1) / (x2 - x1)) if y1 != y2 else -limit
    b1 = py1 - k1 * px1

    # Вторая прямая
    x2, x3 = (x2, x3 + 1) if x3 - x2 == 0 else (x2, x3)
    px2, py2 = (x2 + x3) // 2, (y2 + y3) // 2
    k2 = -1 / ((y3 - y2) / (x3 - x2)) if ((y3 - y2) / (x3 - x2)) != 0 else -limit
    b2 = py2 - k2 * px2

    # Окружность
    x0 = (b2 - b1) / (k1 - k2) if k1 - k2 != 0 else limit
    y0 = k1 * x0 + b1
    r = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

    k = (y3 - y1) / (x3 - x1) if x3 - x1 != 0 else limit
    b = y1 - k * x1
    sign = k * x2 + b - y2 > 0

    if r > 1000:
        pygame.draw.line(windows, (0, 0, 0), (int(x1), int(y1)), (int(x3), int(y3)), 2)
    else:
        xa_ = ya_ = -1
        for a in range(3600):
            xa = x0 + math.cos(math.radians(a / 10)) * r
            ya = y0 + math.sin(math.radians(a / 10)) * r
            if xa_ == -1 and ya_ == -1:
                xa_, ya_ = xa, ya

            if (k * xa + b - ya > 0) == sign:
                pygame.draw.line(windows, (0, 0, 0), (int(xa_), int(ya_)), (int(xa), int(ya)), 2)
            xa_, ya_ = xa, ya

    if _points:
        kc = -1 / ((y3 - y0) / (x3 - x0)) if ((y3 - y0) / (x3 - x0)) != 0 else -limit
        bc = y3 - kc * x3

        l_ = 1 / limit
        d = -l_ if (k * (x3 - l_) + b - (kc * (x3 - l_) + bc) >= 0) != sign else l_
        return [(x3 - d, kc * (x3 - d) + bc), (x3, y3)]


def draw_arc_line(windows, x1, y1, x2, y2, x3, y3):
    len_1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    len_2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    ln = min(len_1, len_2) / 2

    x1_, y1_ = x1 - (x1 - x2) / 2,  y1 - (y1 - y2) / 2
    x3_, y3_ = x3 - (x3 - x2) / 2, y3 - (y3 - y2) / 2

    x1 = x2 - (x2 - x1) / (len_1 / ln)
    y1 = y2 - (y2 - y1) / (len_1 / ln)
    x3 = x2 + (x3 - x2) / (len_2 / ln)
    y3 = y2 + (y3 - y2) / (len_2 / ln)

    pygame.draw.line(windows, (0, 0, 0), (x1, y1), (x1_, y1_), 3)
    pygame.draw.line(windows, (0, 0, 0), (x3, y3), (x3_, y3_), 3)

    x2_, y2_ = x3 - (x3 - x2) / 100, y3 - (y3 - y2) / 100
    x2, y2 = x1 + (x2 - x1) / 100, y1 + (y2 - y1) / 100

    # pygame.draw.circle(windows, (250, 0, 0), (x1, y1), 1)
    # pygame.draw.circle(windows, (250, 0, 0), (x2, y2), 1)
    # pygame.draw.circle(windows, (250, 0, 0), (x2_, y2_), 1)
    # pygame.draw.circle(windows, (250, 0, 0), (x3, y3), 1)
    draw_arc(windows, x1, y1, x2, y2, x3, y3)
