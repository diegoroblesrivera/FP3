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
t=0
def resv(piso, num_habi, nombre):
    if not hotel[piso][num_habi]:  # Verificar si la habitación está vacía
        hotel[piso][num_habi] = nombre
        print(f"Reserva realizada para {nombre} en el piso {piso}, habitación {num_habi}.")
    else:
        print(f"Estimado/a {nombre}, la habitación {num_habi} del piso {piso} se encuentra ocupada, redireccionando a menú principal.")

def guardar_reserva(piso, num_habi, nombre):
    with open("hotel.txt", "w") as archivo:
        archivo.write(f"Su habitacion esta en el piso {piso+1},
        numero {num_habi+1}. Gracias por su compra :D, {nombre}.")

def saber(hotel):
    for i, piso in enumerate(hotel):
        for j, habitacion in enumerate(piso):
            if not habitacion:
                print(f"Habitación {j+1} del piso {i+1} está disponible.")
            else:
                print(f"Habitación {j+1} del piso {i+1} está lamentablemente ocupada.")
                
def monetizar(t):
    for i, piso in enumerate(hotel):
        for j, habitacion in enumerate(piso):
            if habitacion:
                if i>=0 and i<=2:
                    t=t+78500
                elif i>=3 and i<=6:
                    t=t+90000
                elif  i>=7 and i<=9:
                    t=t+110000      
    return t

while True:
    print("Bienvenido al hotel duocuc")
    print("""
 // ¿Qué desea hacer? //
1. Reservar una habitación.
2. Ver todas las habitaciones.
3. Verificar disponibilidad de habitaciones.
4. Monetizar
5. Salir.
    """)
    op = int(input("Seleccione una opción: "))
    match op:
        case(1):
            piso = int(input("Ingrese el piso: "))-1
            num_habi = int(input("Ingrese el número de su habitación: "))-1
            nombre = input("Ingrese su nombre para la reserva: ")
            resv(piso, num_habi, nombre)
            guardar_reserva(piso, num_habi, nombre)
        case (2):
            for piso in hotel:
                print(piso)
        case (3):
            saber(hotel)    
        case (4):
            print("El total monetizado es ", (monetizar(t))*1.19)
        case (5):
            print("usted ha salido")
            break
        case (_):
            print("opcion invalida ._.")
