def recorrer_lista(lista):
 for elemento in lista:
    print(elemento)
# Ejemplo de uso

mi_lista = [1, 2, 3, 4, 5]
# recorrer_lista(mi_lista)

def pares_e_impares(lista):

    pares = []
    impares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
        else:
            impares.append(elemento)
    print("Números pares:", pares)
    print("Números impares:", impares)
# Ejemplo de uso
lista_completa = [1, 2, 3, 4, 5, 6, 7, 8, 9,66,88,23]
# pares_e_impares(lista_completa)

def buscar_valor(diccionario, key):
    if key in diccionario:
        return diccionario[key]
    else:
        return f"La clave '{key}' no existe en el diccionario."

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

clave_buscada = str(input("ingrese numero indice: "))

resultado = buscar_valor(mi_diccionario, clave_buscada)

# print(resultado)