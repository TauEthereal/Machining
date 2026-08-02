# operations/drill.py

def drill(g, x, y, depth,feed):
    """
    Сверление отверстия.
    g       — объект mecode
    x, y    — координаты центра
    depth   — глубина сверления (отрицательное число, мм)
    """
    g.move(z=5)        # подъём на безопасную высоту
    g.move(x=x, y=y)   # позиционирование
    g.write(f'F{feed}\n')
    g.move(z=depth)    # сверление
    g.move(z=5)        # подъём