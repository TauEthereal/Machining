# operations/countersink.py

def countersink(g, x, y, depth, feed):
    """
    Зенкерование отверстия.
    g       — объект mecode
    x, y    — координаты центра
    depth   — глубина зенкерования (отрицательное число, мм)
    """
    g.move(z=5)                 # подъём
    g.move(x=x, y=y)            # позиционирование
    g.write(f'F{feed}\n')       # подача
    g.move(z=depth)             # зенкерование
    g.move(z=5)                 # подъём