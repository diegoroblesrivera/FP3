Total = int(0)
f=0
p=0
jc=0
j=0
listado_productos={}
nom=input("Para comenzar, ingrese su nombre")
while True:
    print('''Elija la comida a comer
          1. Fideos $1490
          2. Pollo asado $4920
          3. Jugos en cajas $2190
          4. Jamon $2310
          5. Terminar la cuenta y calcular gasto final''')
    Eleccion = int(input())
    match Eleccion:
            case 1:
                Total += 1490
                f=f+1
                listado_productos["Fideos"+str(f)] = 1490
            case 2:
                Total+=4920
                p=p+1
                listado_productos["Pollo asado"+str(p)] = 4920
            case 3:
                Total+=2190
                jc=jc+1
                listado_productos["Jugos en cajas"+str(jc)] = 1490
            case 4:
                Total+=2310
                j=j+1
                listado_productos["Jamon"+str(j)] = 1490
            case 5: 
                break
            case _:
                print("Eleccion invalida")
TotalFinal = Total+(Total*0.19)

print (f"su cuenta total es: {TotalFinal}")
with open(f'boleta{nom}.txt', 'w') as file:
    file.write(f"Bienvenido a supermacado Alegre\n")
    file.write(f"------------------------------\n")
    file.write(f"Producto .........Precio\n")
    for item, price in listado_productos.items():
        file.write(f"{item}.....${price}\n")
    file.write(f"------------------------------\n")
    file.write(f"Su subtotal es ${Total}\n")
    file.write(f"Su total a pagar es ${TotalFinal}\n")
