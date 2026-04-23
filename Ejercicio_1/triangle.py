def classify_triangle(x, y, z):
    if x == y == z:
        print("Equilateral triangle")

    elif x == y or y == z or z == x:
        print("isosceles triangle")

    elif x**2 + y**2 == z**2:
        print("right angled triangle")

    else:
        print("scalene triangle")


if __name__ == "__main__":
    classify_triangle(1, 2, 3)