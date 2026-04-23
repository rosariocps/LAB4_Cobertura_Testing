def foo(x, y):
    if x == 0:
        y += 1
    if y == 0:
        x += 1


# SOLO UNA LLAMADA
foo(0, -1)