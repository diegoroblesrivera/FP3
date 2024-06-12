def validar_lista_numeros(mensaje):
    while True:
        try:
            lista_numeros = [int(num) for num in input(mensaje).split()]
            return lista_numeros
        except ValueError:
            print("Error: Ingrese una lista de números enteros válidos separados por espacios.")

# Ingreso de lista de números con validación
numeros_ingresados = validar_lista_numeros("Ingrese una lista de números enteros separados por espacios: ")

# Verificación de paridad en la lista
numeros_pares = [num for num in numeros_ingresados if num % 2 == 0]
numeros_impares = [num for num in numeros_ingresados if num % 2 != 0]

# Mostrar resultados
print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
