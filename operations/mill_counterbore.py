# operations/mill_counterbore.py

def mill_counterbore(g, x, y, depth, final_diameter, tool_diameter,step_radial,
                     start_diameter, feed):
    """
    Фрезерование ступенчатого отверстия (цилиндрического углубления)
    с несколькими проходами для постепенного расширения.

    Параметры:
        g                — объект mecode
        x, y             — координаты центра
        depth            — глубина углубления (отрицательное число, мм)
        final_diameter   — конечный диаметр отверстия (мм)
        tool_diameter    — диаметр фрезы
        start_diameter   — начальный диаметр (если None, то равен tool_diameter)
        step_radial      — увеличение радиуса за один проход (мм)
    """
    
    # Радиусы
    start_radius = start_diameter / 2
    final_radius = final_diameter / 2
    tool_radius = tool_diameter / 2

    # Текущий радиус расширения (начинаем с начального)
    current_radius = start_radius

    # Подъём на безопасную высоту
    g.move(z=5)

    # Цикл по проходам (увеличиваем радиус)
    while current_radius < final_radius:
        # Следующий радиус (не превышаем final_radius)
        next_radius = min(current_radius + step_radial, final_radius)

        # Радиус траектории центра фрезы
        path_radius = next_radius - tool_radius

        # Опускаемся на глубину
        g.write(f'F{feed}\n')
        g.move(z=depth)

        # Перемещаемся на радиус (по X) и делаем полный круг
        g.move(x=x + path_radius, y=y)
        g.arc(x=x, y=y, radius=path_radius, direction='CW')

        # Поднимаем фрезу
        g.move(z=5)

        # Обновляем текущий радиус для следующего прохода
        current_radius = next_radius