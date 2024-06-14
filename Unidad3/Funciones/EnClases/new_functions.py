import math
# Crear una funcion para el area de un circulo y 
# luego crear otra para el volumen de un cilidndro
# usando el resultado de la funcion anterior.
# Area= 3.14 * r*r
# Volumen de un circulo= area * altura


# def area_circulo (radio):
#     return 3.14 * radio*radio

# def volumen_cilindro(radio,alt):
#     return area_circulo(radio)*alt


# print(volumen_cilindro(5, 9))

# def area_cuadrado (lado):
#     return lado*lado

# def volumen_cubo(lado,alt):
#     return area_cuadrado(lado)*alt


# print(volumen_cubo(5, 9))

# Crear una funcion para insertar un a lista y muestra los cuadrados de 
# cada elemento

def cuadrados(lista):
    hook=[]
    cont=0
    for i in lista:
        hook.append(i**2)
    with open(f'cuadrados.txt', 'w') as file:
                for num in hook:
                    cont=cont+1
                    file.write(f"Cuadrado {cont} {num} \n")
    return hook
oo=[2,6,-4,5.8, 8, 7 , 14 ,8]
print(cuadrados(oo))
    
# print(math.sqrt(64))
    
    

