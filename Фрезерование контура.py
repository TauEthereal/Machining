from mecode import G
from operations.contour import contour

WIDTH = 221
HEIGHT = 131
RADIUS = 5.5
DEPTH = -26
TOOL_DIA = 14
TOOL_RADIUS = TOOL_DIA / 2
SAFE_Z = 5
FEED = 1150   # подача для контура

with G(outfile='Установ Б.ngc', print_lines=False) as g:
    g.absolute()
    g.write('(Фрезеровка внешнего контура)\n')
    g.move(z=SAFE_Z)
    g.write('T7 M6\n')          # фреза ⌀14
    g.write('S3000 M3\n')

    # Подвод к точке входа (снаружи, ниже детали)
    entry_x = 0
    entry_y = -HEIGHT / 2 - TOOL_RADIUS
    g.move(x=entry_x, y=entry_y)
    g.write(f'F{FEED}\n')
    g.move(z=DEPTH)

    # Рисуем контур с ручным смещением на радиус фрезы
    contour(g, WIDTH, HEIGHT, RADIUS, TOOL_RADIUS, FEED)

    g.move(z=SAFE_Z)
    g.move(z=20)
    g.write('M30\n')

print("Установ Б создан")