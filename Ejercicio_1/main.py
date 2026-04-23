from triangle import classifyTriangle


def test():
    # Equilateral
    classifyTriangle(3, 3, 3)

    # Isoceles
    classifyTriangle(3, 3, 2)

    # Right triangle
    classifyTriangle(3, 4, 5)

    # Scalene
    classifyTriangle(2, 3, 4)

    # Caso raro (para cubrir todo)
    classifyTriangle(0, 0, 0)


test()