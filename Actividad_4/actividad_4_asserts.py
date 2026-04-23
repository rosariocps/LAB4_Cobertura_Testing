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
# FUNCION AUXILIAR PARA VALIDAR
#-----------------------------------------

def check(test_name, result, expected):
    print(f"\n--- {test_name} ---")

    labels = ["min", "max", "median", "mode"]

    for i in range(4):
        if result[i] == expected[i]:
            print(f"✔ {labels[i]} correcto")
        else:
            print(f"❌ {labels[i]} incorrecto → esperado {expected[i]}, obtenido {result[i]}")


#-----------------------------------------
# TEST 1: CASOS ORIGINALES
#-----------------------------------------

def test_original():
    print("TEST 1: Casos originales (NO detectan errores claramente)")

    # Caso impar
    result = stats([18,19,20,20,21])
    expected = (18,21,20,[20])
    check("Caso impar", result, expected)

    # Caso par
    result = stats([20,18,19,17])
    expected = (17,20,18.5,[20,18,19,17])
    check("Caso par", result, expected)


#-----------------------------------------
# TEST 2: BUG DE VALORES NEGATIVOS
#-----------------------------------------

def test_bug_abs():
    print("\nTEST 2: Detectando bug de valores negativos")

    result = stats([-3,-4])
    expected = (-4,-3,-3.5,[-3,-4])

    check("Caso negativos", result, expected)


#-----------------------------------------
# TEST 3: BUG DE FRECUENCIA
#-----------------------------------------

def test_bug_freq():
    print("\nTEST 3: Detectando bug de frecuencia")

    result = stats([1,1,2])
    expected = (1,2,1,[1])

    check("Caso frecuencia", result, expected)


#-----------------------------------------
# EJECUCION
#-----------------------------------------

test_original()
test_bug_abs()
test_bug_freq()