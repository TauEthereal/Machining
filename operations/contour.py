# operations/contour.py

def contour(g, width, height, radius, direction, feed):
    """
    Рисует внешний контур прямоугольника со скруглёнными углами.
    Начинает с середины нижней стороны (0, -height/2).
    direction — 'CCW' (против часовой) или 'CW' (по часовой).
    """
    start_x = 0
    start_y = -height / 2

    # Перемещение в начальную точку
    g.move(x=start_x, y=start_y)
    g.write('f{feed}\n')

    if direction == 'CCW':
        # Обход против часовой стрелки (влево → вверх → вправо → вниз)
        g.move(x=-(width / 2 - radius), y=start_y)
        g.arc(x=-width / 2, y=-height / 2 + radius, radius=radius, direction='CW')
        g.move(x=-width / 2, y=height / 2 - radius)
        g.arc(x=-width / 2 + radius, y=height / 2, radius=radius, direction='CW')
        g.move(x=width / 2 - radius, y=height / 2)
        g.arc(x=width / 2, y=height / 2 - radius, radius=radius, direction='CW')
        g.move(x=width / 2, y=-height / 2 + radius)
        g.arc(x=width / 2 - radius, y=-height / 2, radius=radius, direction='CW')
        g.move(x=start_x, y=start_y)

    else:  # 'CW' — по часовой стрелке (вправо → вниз → влево → вверх)
        g.move(x=width / 2 - radius, y=start_y)
        g.arc(x=width / 2, y=-height / 2 + radius, radius=radius, direction='CCW')
        g.move(x=width / 2, y=height / 2 - radius)
        g.arc(x=width / 2 - radius, y=height / 2, radius=radius, direction='CCW')
        g.move(x=-(width / 2 - radius), y=height / 2)
        g.arc(x=-width / 2, y=height / 2 - radius, radius=radius, direction='CCW')
        g.move(x=-width / 2, y=-height / 2 + radius)
        g.arc(x=-width / 2 + radius, y=-height / 2, radius=radius, direction='CCW')
        g.move(x=start_x, y=start_y)