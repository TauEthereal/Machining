# operations/contour.py

def contour(g, width, height, radius, offset, feed):
    """
    Рисует внешний контур прямоугольника со скруглёнными углами.
    offset — смещение наружу (обычно радиус фрезы).
    Начинает с середины нижней стороны (0, -height/2 - offset).
    Все координаты автоматически смещаются на offset.
    """
    # Начальная точка — середина нижней стороны + смещение наружу
    start_x = 0
    start_y = -height / 2 - offset

    g.move(x=start_x, y=start_y)
    g.move(z=5)  # безопасная высота (можно не писать, если уже подняты)
    
    # Обход против часовой стрелки (влево → вверх → вправо → вниз)
    # Все координаты сдвинуты на offset
    g.move(x=-(width / 2 - radius) - offset, y=start_y)
    g.arc(x=-width / 2 - offset, y=-height / 2 + radius + offset,
          radius=radius + offset, direction='CCW')
    g.move(x=-width / 2 - offset, y=height / 2 - radius + offset)
    g.arc(x=-width / 2 + radius + offset, y=height / 2 + offset,
          radius=radius + offset, direction='CCW')
    g.move(x=width / 2 - radius + offset, y=height / 2 + offset)
    g.arc(x=width / 2 + offset, y=height / 2 - radius + offset,
          radius=radius + offset, direction='CCW')
    g.move(x=width / 2 + offset, y=-height / 2 + radius + offset)
    g.arc(x=width / 2 - radius + offset, y=-height / 2 - offset,
          radius=radius + offset, direction='CCW')
    g.move(x=start_x, y=start_y)