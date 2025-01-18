
import random
import time
jug1=0
jug2=0

def ruleta():
    return random.randint(1,6)

print("BIENVENIDO A LA RULETA RUSA")
bala=ruleta()

for p in range(6) :
    print("turno del jugador", p+1)
    print("Para disparar presione 'f'")
    mov=input()
    if mov=='f':
        time.sleep(1)
        print("*")
        time.sleep(1)
        print("*")
        time.sleep(1)
        print("*")
        if p+1==bala:
            print("BANG!!!")
            break
        else:
            print("ZAFASTE WEY")
