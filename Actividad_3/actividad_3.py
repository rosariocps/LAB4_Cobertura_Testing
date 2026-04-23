# SPECIFICATION:
#
#
# TASK:
#
# The stats function computes some basic statistics functions
# (minimo, maximo, mediana y moda)
# when given a list of numbers as input.
# Achieve full statement coverage on the stats function.
# All you should have to do is modify the test function
# to call stats with different lists of values.

def stats(lst):
    min = None #minimo 
    max = None #maximo
    freq = {} #frecuencia: cuantas veces aparece/se repite cada numero
    # ej: lst = [1, 2, 2, 3] -> {1: 1, 2: 2, 3: 1}

    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq: # nro. repetido
            freq[i] += 1 
        else: # nro. nuevo
            freq[i] = 1

    lst_sorted = sorted(lst) # ordena la lista

# calculo mediana y moda
# mediana
    if len(lst_sorted) % 2 == 0: # en caso sera par
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else: # en caso impar
        middle = len(lst_sorted) // 2
        median = lst_sorted[middle]

# moda
    mode_times = None

# encontrar frecuencia maxima
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
# encontrar numeros con esa frecuencia
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    print("list = " + str(lst))
    print("min = " + str(min))
    print("max = " + str(max))
    print("median = " + str(median))
    print("mode(s) = " + str(mode))


def test():
    
    ###Your code here.
    # Change l to something that manages full coverage. You may
    # need to call stats twice with different input in order
    # to achieve full coverage.
    # SOLUCION:
    stats([18,19,20,20,21]) # impar
    stats([20,18,19,17]) # par

test()