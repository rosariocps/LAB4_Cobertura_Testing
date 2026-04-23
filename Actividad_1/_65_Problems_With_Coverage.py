import math

# ========================================================
# ACTIVIDAD: PROBLEMAS CON LA COBERTURA (PRIME NUMBERS)
# ========================================================

def isPrime_Buggy(number):
    """Esta función logra 100% de cobertura pero falla con el número 9"""
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    # El error está aquí: range es exclusivo al final
    for check in range(3, int(math.sqrt(number))):  
        if (number % check) == 0:  
            return False
    return True

def isPrime_Fixed(number):
    """Esta versión corrige el error de límite lógico"""
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    # Corrección: + 1
    for check in range(3, int(math.sqrt(number)) + 1):  
        if (number % check) == 0:  
            return False
    return True

def test():
    print("Iniciando pruebas...")
    
    # 1. Demostración del fallo de cobertura
    # isPrime_Buggy(9) devolverá True (ERROR) porque el loop no se ejecuta
    resultado_incorrecto = isPrime_Buggy(9)
    print(f"¿Es 9 primo para la función con bug?: {resultado_incorrecto}")
    
    # 2. Validación de la solución
    assert isPrime_Fixed(9) == False
    assert isPrime_Fixed(25) == False
    assert isPrime_Fixed(23) == True
    
    print(">>> Test de problemas de cobertura finalizado con éxito.")

if __name__ == "__main__":
    test()