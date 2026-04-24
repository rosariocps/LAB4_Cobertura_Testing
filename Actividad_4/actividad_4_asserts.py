#-----------------------------------------
# FUNCION STATS (CON BUGS INTENCIONALES)
#-----------------------------------------

def stats(lst):
    min = None  
    max = None 
    freq = {} 

    for i in lst:
        i = abs(i)  # BUG 1

        if min is None or i < min:
            min = i

        if max is None or i > max:   
            max = i

        if i in freq:
            freq[i] = 1   # BUG 2
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)

    # MEDIANA
    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        middle = len(lst_sorted) // 2
        median = lst_sorted[middle]

    # MODA
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    return min, max, median, mode


#-----------------------------------------
# FUNCION DE TEST (ASSERTS + MENSAJE)
#-----------------------------------------

def run_test(test_name, lst, expected):
    result = stats(lst)

    print(f"\n--- {test_name} ---")

    labels = ["min", "max", "median", "mode"]

    for i in range(4):
        try:
            assert result[i] == expected[i]
            print(f"[✓ OK] {labels[i]} correcto")
        except AssertionError:
            print(f"[✗ ERROR] {labels[i]} incorrecto → esperado {expected[i]}, obtenido {result[i]}")


#-----------------------------------------
# TESTS
#-----------------------------------------

def test_original():
    print("TEST 1: Casos originales")

    run_test(
        "Caso impar",
        [18,19,20,20,21],
        (18,21,20,[20])
    )

    run_test(
        "Caso par",
        [20,18,19,17],
        (17,20,18.5,[20,18,19,17])
    )


def test_bug_abs():
    print("\nTEST 2: Detectando bug de valores negativos")

    run_test(
        "Caso negativos",
        [-3,-4],
        (-4,-3,-3.5,[-3,-4])
    )


def test_bug_freq():
    print("\nTEST 3: Detectando bug de frecuencia")

    run_test(
        "Caso frecuencia",
        [1,1,2],
        (1,2,1,[1])
    )


#-----------------------------------------
# EJECUCION
#-----------------------------------------

test_original()
test_bug_abs()
test_bug_freq()