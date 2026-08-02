from mecode import G
import operations

# Параметры детали 
WIDTH = 221
HEIGHT = 131
RADIUS = 5.5
DEPTH = -26

TOOL_DIA = 14
TOOL_RADIUS = TOOL_DIA / 2
SAFE_Z = 5

# Выбор направления обхода
DIRECTION = 'CCW'   # или 'CW' – менять здесь

with G(outfile='Установ Б.ngc', print_lines=False) as g:
    g.absolute()
    g.write('G21\n')   # миллиметры

    g.write('(Программа обработки плиты)\n')
    g.move(z=10)  # безопасная высота

    g.write('(Фрезеровка внешнего контура)\n')
    g.write('T7 M6\n') #фреза 14 мм
    g.write('S3000 M3\n') #подача
    g.move(z=SAFE_Z)

    entry_approach_x = 0
    entry_approach_y = -HEIGHT / 2 - TOOL_RADIUS
    entry_x = 0
    entry_y = -HEIGHT / 2

    g.move(x=entry_approach_x, y=entry_approach_y)
    g.move(z=DEPTH, feed=1150)

    # Компенсация: для CCW – G41 (слева), для CW – G42 (справа)
    if DIRECTION == 'CCW':
        g.compensation = 'left'
    else:
        g.compensation = 'right'

    g.move(x=entry_x, y=entry_y)
    operations.contour(g, WIDTH, HEIGHT, RADIUS, direction=DIRECTION,feed = 1150)
    g.write('G40\n')
    g.move(z=SAFE_Z)
    g.move(z=20)
    g.write('M30\n')
print("Установ Б завершен")