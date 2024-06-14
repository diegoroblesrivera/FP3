from israel_solu import buscar_valor

def creaDiccionario():
    dic_vacio={}
    while True:
        key=input("Ingrese una key")
        if key.lower()=="shazam":
            print(dic_vacio)
            break
        else:
            value=input("Ingrese el valor de key anterior")
            dic_vacio[key] = value
    preg=input("ingrese la key a buscar")
    print(buscar_valor(dic_vacio, preg ))
            

creaDiccionario()
"""Crear un programa cre cree un diccionario soliciando la key
y el value de la misma. Seguira solicitando pares de datos
hasta ingresar la palabra secreta SHAZAM. 
Una vez creado el diccionario, debe llamar a la fucnion
buscar_valor que se encuentra en el archivo israel_solu.py
y mastrar el valor de la key que el usuario ingrese"""

