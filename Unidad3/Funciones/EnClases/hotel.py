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

def resv(piso, num_habi, nombre):
    if not hotel[piso][num_habi]:  # Verificar si la habitación está vacía
        hotel[piso][num_habi] = nombre
        print(f"Reserva realizada para {nombre} en el piso {piso}, habitación {num_habi}.")
    else:
        print(f"Estimado/a {nombre}, la habitación {num_habi} del piso {piso} se encuentra ocupada, redireccionando a menú principal.")

def guardar_reserva(piso, num_habi, nombre):
    with open("hotel.txt", "w") as archivo:
        archivo.write(f"Su habitacion esta en el piso {piso}, numero {num_habi}. Gracias por su compra :D, {nombre}.")

def saber(hotel):
    for i, piso in enumerate(hotel):
        for j, habitacion in enumerate(piso):
            if not habitacion:
                print(f"Habitación {j} del piso {i} está disponible.")
            else:
                print(f"Habitación {j} del piso {i} está ocupada.")

while True:
    print("Bienvenido al hotel duocuc")
    print("""
 // ¿Qué desea hacer? //
1. Reservar una habitación.
2. Ver todas las habitaciones.
3. Verificar disponibilidad de habitaciones.
4. Salir.
    """)
    op = int(input("Seleccione una opción: "))
    match op:
        case(1):
            piso = int(input("Ingrese el piso: "))
            num_habi = int(input("Ingrese el número de su habitación: "))
            nombre = input("Ingrese su nombre para la reserva: ")
            resv(piso, num_habi, nombre)
            guardar_reserva(piso, num_habi, nombre)
        case (2):
            for piso in hotel:
                print(piso)
        case (3):
            saber(hotel)
        case (4):
            print("usted ha salido")
            break
        case (_):
            print("opcion invalida ._.")
