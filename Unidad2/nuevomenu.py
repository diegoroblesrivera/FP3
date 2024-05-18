usuario1= None
usuario2=None 
usuario3=None
contrasena1= None 
contrasena2=None 
contrasena3= None

while True:
    print("Seleccione una opcion")
    print("1.- Iniciar sesion")
    print("2.- Registrar")
    print("3.- Salir")
    op=int(input())
    match op:
        case 1:
            if usuario1==None and usuario2==None and usuario3==None:
                print("No existen usuarios aun")
            else:
                print("Ingrese su usuario")
                uservol=input()
                if uservol==usuario1 :
                    passvol=input(("Ingrese su contraseña"))
                    if contrasena1==passvol:
                        print("Bienvenido al sistema")
                    else:
                        print("Su contraseña es invalida")    
                elif uservol==usuario2:
                    passvol=input(("Ingrese su contraseña"))
                    if contrasena2==passvol:
                        print("Bienvenido al sistema")
                    else:
                        print("Su contraseña es invalida") 
                
                elif uservol==usuario3:
                    passvol=input(("Ingrese su contraseña"))
                    if contrasena3==passvol:
                        print("Bienvenido al sistema")
                    else:
                        print("Su contraseña es invalida") 


        case 2:
            print("Resistre un usuario dweseado: 1, 2 , o 3")
            opc=int(input())
            match opc:
                case 1:
                    print("Ingrese el usuario ", opc)
                    usuario1=input()
                    print("Usuario ingresado conrrectamente, ingrese su contraseña")
                    contrasena1=input()
                    print("Contraseña ingresada con exito, ahora puede acceder al sistema")
                case 2:
                    print("Ingrese el usuario ", opc)
                    usuario2=input()
                    print("Usuario ingresado conrrectamente, ingrese su contraseña")
                    contrasena2=input()
                    print("Contraseña ingresada con exito, ahora puede acceder al sistema")
                case 3:
                    print("Ingrese el usuario ", opc)
                    usuario3=input()
                    print("Usuario ingresado conrrectamente, ingrese su contraseña")
                    contrasena3=input()
                    print("Contraseña ingresada con exito, ahora puede acceder al sistema")
                case _:
                    print("Seleccione una opcion valida")

        case 3:
            print("Opcion 3")
            break
        case _:
            print("Seleccione una opcion valida")