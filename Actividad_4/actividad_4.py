def stats(lst):
    min = None  
    max = None 
    freq = {} 

    for i in lst:
        i = abs(i)  # BUG INSERTADO 1
        if min is None or i < min:
            min = i
        if max is None or i > max:   
            max = i
        if i in freq: # nro. repetido
            freq[i] = 1 # BUG INTENCIONAL 2: debió ser +=1
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

#---------------------------
# CASOS DE TEST
#---------------------------

def test():
    # Casos originales (logran coverage al 100% pero NO detectan errores)
    stats([18,19,20,20,21])  # impar + repetido
    stats([20,18,19,17])     # par
    
def test_bug_abs():
    print("\n Segundo test:") 
    # Caso que revela error con valores negativos
    stats([-3, -4])

def test_bug_freq():
    print("\n Tercer test:") 
    # Caso que revela error en la moda
    stats([1,1,2])

test()
# test_bug_abs()
test_bug_freq()