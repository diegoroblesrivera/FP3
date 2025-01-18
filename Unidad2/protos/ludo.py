import random
import time
def dado():
    return random.randint(1,6)
cam1=0
cam2=0
jug=None
print("Binevenido al ludo")
print ("Cuantos jugadores son?")
cJug=int(input())

while True:
    for i in range(cJug):
        print ("Turno del jugdor", i+1)
        print("va a tirar el dado? (s/n)")
        des=input()
        if des=="s":
            lado=dado()
            print("Ha sacado el numero ", lado)
            cam1=cam1+lado
            print(" ha avanzado a la casilla ", cam1)
    time.sleep(2) 
    if cam1>=24:
        break
    

    