def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

def validar_num(numero_entrada):
    while True:
        try:
            numero = float(input(numero_entrada))
            return numero
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

# Ingreso de dos números con validaciones
num1 = validar_num("Ingrese el primer número: ")
num2 = validar_num("Ingrese el segundo número: ")

resultado_suma = sumar(num1, num2)
resultado_resta = restar(num1, num2)
resultado_multiplicacion = multiplicar(num1, num2)
resultado_division = dividir(num1, num2)

print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División: {resultado_division}")
