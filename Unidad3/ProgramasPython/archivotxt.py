# #Las comillas al inicio y 3 al final del texto representan un texto
# #con saltos de línea
# datos = """Este es un archivo de texto simple que no tiene 
# ningún formato en particular, lo podemos utilizar
# para guardar todo tipo de texto. 
# """
# with open('archivo.txt', 'w') as archivo:
#     archivo.write(datos)


# # Opción 1
# # Sintaxis: open('nombre_del_archivo', 'modo')
# # Modos comunes: 'r' (lectura), 'w' (escritura), 'a' (anexar), 'r+' (lectura/escritura)
# archivo = open('datos.txt', 'r')
# contenido = archivo.read()
# print(contenido)
# archivo.close()

# # Opción 2
# # Usando el contexto 'with', el archivo se cierra automáticamente al salir del bloque 'with'
# with open('datos.txt', 'r') as archivo:
#     contenido = archivo.read()
#     print(contenido)


# Abrir archivo, r es permiso de lectura
# with open('datos.txt', 'r') as archivo:
#     contenido = archivo.read()
# print(contenido)



# n = int(input('Introduce un número entero entre 1 y 10: '))
# nombre_fichero = 'tabla-' + str(n) + '.txt'
# with open(nombre_fichero, 'w') as f:
#     for i in range(1, 11):
#         f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')




