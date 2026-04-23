def classifyTriangle(a, b, c):
    """
    Clasifica un triángulo según sus lados.

    return:
        'Equilateral' → todos los lados iguales
        'Isoceles' → dos lados iguales
        'Right' → triángulo rectángulo
        'Scalene' → todos diferentes
        'NotATriangle' → no forma triángulo válido
    """

    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isoceles'
    elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
        return 'Right'
    elif a != b and a != c and b != c:
        return 'Scalene'
    else:
        return 'NotATriangle'