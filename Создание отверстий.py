from mecode import G
import operations

# Параметры детали 
PLATE_WIDTH = 221   # длина детали
PLATE_HEIGHT = 131  # ширина детали
DEPTH = -26         # толщина детали

#Координаты всех отверстий в пересчете от центра

HOLES_2 = [(-18,-40),(-18,40)] #под глухие резьбовые отверстия
HOLES_4 = [(67.5,47.5),(67.5,-47.5),(-67.5,-47.5),(-67.5,47.5)] #под отверстия 10,5 окончательно
HOLES_6_1 = [(1.5,13),(1.5,-13),(-38.5,-13),(-38.5,13)] #под классные отверстия и расфрезерование
HOLES_6_2 = [(42.5,-47.5),(-42.5,47.5)] #под классные отверстия

holes_6 = HOLES_6_1+HOLES_6_2
all_holes = HOLES_2 + HOLES_4 + holes_6

# Создаём G-код файл
with G(outfile='Установ А.ngc', print_lines=False) as g:
    g.absolute()
    g.write('G21\n')   # миллиметры

    g.write('(Программа обработки плиты)\n')
    g.move(z=10)  # безопасная высота

    print("переход 1: центрование")
    g.write('(Центровка 12 отверстий)\n')
    g.write('T1 M6\n')      # центровочное сверло
    g.write('S1430 M3\n')   # обороты
    for x, y in all_holes:
        operations.center_drill(g, x, y, depth=-2, feed = 60)   # вызываем центровку с подачей

    print("переход 2: сверление 10")
    g.write('(Сверление 4 отверстий 10 мм насквозь)\n')
    g.write('T2 M6\n')      # сверло 10
    g.write('S2800 M3\n')   
    for x, y in HOLES_4:
        operations.drill(g, x, y, depth=DEPTH, feed = 504)

    print("переход 3: сверление 9,8")
    g.write('(Сверление 6 отверстий 9,8 мм насквозь)\n')
    g.write('T3 M6\n')      # сверло 9,8
    g.write('S2800 M3\n')   
    for x, y in holes_6:
        operations.drill(g, x, y, depth=DEPTH, feed = 504)

    print("переход 4: зенкерование 10,5")
    g.write('(Сверление 4 отверстий 10,5 мм насквозь)\n')
    g.write('T4 M6\n')      # зенкер 10,5
    g.write('S1343 M3\n')   
    for x, y in HOLES_4:
        operations.countersink(g, x, y, depth=DEPTH, feed = 1343)

    print("переход 5: расфрезеровать на глубину 12 до 18 четыре отверстия 10,5")
    g.write('(Фрезерование 4 отверстий до 18, глуб.12)\n')
    g.write('T5 M6\n')
    g.write('S6000 M3\n')
    for x, y in HOLES_4:
        operations.mill_counterbore(g, x, y,
                             depth=-12,         #Глубина фрезерования
                             final_diameter=18, #Финальный диаметр отверстия
                             tool_diameter=8,   #Диаметр инструмента
                             start_diameter=10, #Диаметр стартового отверстия (лучше указать 10 для удобства расчета припуска)
                             step_radial=1.0,   #Снимаемый припуск на сторону
                             feed = 1300)       #Подача

    print("переход 6: расфрезеровать на глубину 6 до 18 четыре отверстия 9,8")
    g.write('(Фрезерование 4 отверстий до 18, глуб.12)\n')
    g.write('T5 M6\n')
    g.write('S6000 M3\n')
    for x, y in HOLES_6_1:
        operations.mill_counterbore(g, x, y,
                             depth=-12,         #Глубина фрезерования
                             final_diameter=18, #Финальный диаметр отверстия
                             tool_diameter=8,   #Диаметр инструмента
                             start_diameter=10, #Диаметр стартового отверстия (лучше указать 10 для удобства расчета припуска)
                             step_radial=1.0,   #Снимаемый припуск на сторону
                             feed = 1300)       #Подача

    print("переход 7: сверление 14")
    g.write('(Сверление 2 отверстий 14 мм под резьбу на глубину 20 мм\n')
    g.write('T6 M6\n')      # сверло 14
    g.write('S3000 M3\n')   
    for x, y in HOLES_2:
        operations.drill(g, x, y, depth=-16, feed = 1150)

    print("переход 8: нарезание резьбы")
    g.write('(Нарезание резьбы М16 в 2 отверстиях)\n')
    g.write('T6 M6\nS200 M3\n')
    for x, y in HOLES_2:
        operations.tap(g, x, y,
                       depth=-16, #depth   — глубина нарезания (отрицательное число, мм)
                       pitch=2,   #шаг резьбы (мм)
                       rpm=443,   #обороты шпинделя (об/мин)
                       safe_z=5,  #безопасная высота
                       dwell=0.5)   #задержка в нижней точке для реверса (сек)
    g.move(z=20)
    g.write('M30\n')
print("Установ А завершен")