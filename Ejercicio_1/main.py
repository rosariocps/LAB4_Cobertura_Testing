from triangle import classify_triangle

def test():
    # Equilateral
    classify_triangle(3, 3, 3)

    # Isosceles
    classify_triangle(3, 3, 2)

    # Right triangle
    classify_triangle(3, 4, 5)

    # Scalene
    classify_triangle(2, 3, 4)

test()