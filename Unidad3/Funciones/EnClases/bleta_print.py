
carrito=[]
f=["uva", "pera", "platano"]
pf=[1200, 1000, 1300]
t=0
while True:
    
    print("""
          1.- Comprar
          2.- Pagar
          3.- Salir
          """)
    op=int(input("Seleccione una opcion"))
    match op:
        case 1:
            
            
            for i in range(len(f)):
                print(i+1,".-",f[i] , "=$",pf[i] )
            sel=int(input("Selecciones los productos a comprar"))
            carrito.append(sel-1)
            print(carrito)   
        case 2:
            print
            print()
            with open('boleta.txt', 'a') as archivo:
                archivo.write("Verdureria Guaton de la fruta\n")
                archivo.write("-----------------------------\n")
                for i in carrito:
                    archivo.write(f"{f[i]}***${pf[i]}\n")
                archivo.write("-----------------------------\n")
                for i in carrito:
                    t=t+pf[i]
                t_iva=t*0.19
                tt=t+t_iva
                archivo.write(f"TOTAL {t}\n")
                archivo.write(f"TOTAL IVA {t_iva}\n")
                archivo.write(f"TOTAL a PAGAR {tt}\n")
                archivo.write("Gracias por su compra\n")
            
                
            
        case 3:
            break
        case _:
            print("Eleccion no valida, seleccione de 1-3")
            
