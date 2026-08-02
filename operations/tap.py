# operations/tap.py

def tap(g, x, y, depth, pitch, rpm, safe_z, dwell):
    """
    Нарезание резьбы метчиком в глухом отверстии.
    g       — объект mecode
    x, y    — координаты центра
    depth   — глубина нарезания (отрицательное число, мм)
    pitch   — шаг резьбы (мм)
    rpm     — обороты шпинделя (об/мин)
    safe_z  — безопасная высота
    dwell   — задержка в нижней точке для реверса (сек)
    """
    feedrate = rpm * pitch   # подача = обороты * шаг

    g.move(z=safe_z)                 # подъём
    g.move(x=x, y=y)                 # позиционирование
    g.write(f'G84 X{x} Y{y} Z{depth} R{safe_z} F{feedrate:.2f} P{dwell}\n')
    g.write('G80\n')                 # отмена цикла
    g.move(z=safe_z)                 # подъём