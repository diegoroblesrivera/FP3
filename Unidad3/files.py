"""CREAR UN PROGRAMA QUE HAGA UNA TABLA DE 
MULTIPLICAR Y LA GUARDE EN UN ARCHIVO
EL ARCHIVO DEBE LLEVAR EL NUMERO DE LATABLA
QUE SE INTRODUJO POR EL USUARIO
EJ: TABLA5.TXT"""

num=int(input())

for i in range(1,11):
    with open(f'tablaDel{num}.txt', 'a') as archivo:
        archivo.write(str(num) +" x "+ str(i) + " = "+ str(num*i)+"\n" )
    