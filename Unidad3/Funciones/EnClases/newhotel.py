hotel = [
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
]
while True:
    print("Bienvenido al hotel duocuc")
    print("""
 // ¿Qué desea hacer? //
1. Reservar una habitación.
2. Check out de una habitación.
3. Ver todas las habitaciones.
4. Guardar en un archivo
5. Salir.
    """)
    op = int(input("Seleccione una opción: "))
    match op:
        case 1:
            print("En que piso se va  alaojar?")
            piso=int(input())
            while piso<1 or piso>10:
                print("Opcion invalida")
                print("En que piso se va  alaojar?")
                piso=int(input())


            print("En que habitacion se va  alaojar?")
            hab=int(input())
            while hab<0 or hab>5:
                print("Opcion invalida")
                print("En que habitacion se va  alaojar?")
                hab=int(input())
            if hotel[piso-1][hab-1]:
                print("La habitacion está usada")
            else:
                nom=input("Ingrese un nombre\n")
                hotel[piso-1][hab-1]={"nombre":nom}
        case 2:
            print("Que piso va a actualizar?")
            piso=int(input())
            print("Que habitacion va a actualizar?")
            hab=int(input())
            hotel[piso-1][hab-1]=[]

        case 3:
                for i in hotel:
                    print(i)
        case 4:
            f = open("outfile.txt","w")
            for piso in hotel:
                for hab in piso:
                    f.write(str(hab))
                f.write('\n')
            f.close()
        case 5:
              break
        case _:
              print("Opcion invalida")
        


