

fut=" Algo mas de texto por aca"

lista=["Mario", "Luigui", "Peach", "TOAD"]

with open('mi_archivo.txt', 'a') as archivo:
    for i in lista:
        archivo.write(f"{i}\n")
    
    
# archivo = open('mi_archivo.txt', 'r')
# contenido = archivo.read()
# print(contenido)
# archivo.close()

# with open('mi_archivo.txt', 'a') as archivo:
#     for elemento in mi_lista:
#         archivo.write(elemento + '\n')


# import json
# # Datos JSON
# datos = {
# "nombre": "Esteban",
# "edad": 25,
# "comuna": "Santiago",
# "estudios": ["colegio Arturo Prat", "liceo el bosque",
# "Duoc UC", "Diplomado Duoc UC"]
# }
# # Abre el archivo, w es escritura
# with open('archivo.json', 'w') as archivo:
#     json.dump(datos, archivo)
    
    



    
# personas = {}



# while True:

#   nomb = input("Ingrese su nombre: ")

#   eda = int(input("Ingrese su edad: "))

#   personas[nomb] = eda

  

#   salir = input("Para salir presione 'x', para continuar presione enter ")

#   if salir == "x":

#     break

#   else:

#     print("Siga ingresando nombres y edades.")

    

# print("Lista de personas ingresadas:")

# for nombre, edad in personas.items():

#   print(f"Nombre: {nombre}, Edad: {edad} años")
  
# print(personas)