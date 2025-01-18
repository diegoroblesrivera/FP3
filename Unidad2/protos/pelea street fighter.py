from os import system
system("cls")
import random
def ataque():
    return random.randint(2,10)
def critico():
    return random.randint(1,5)
def miss(): #fallar el ataque
    return random.randint(1,20)
def bloq(): #al blouqear hay año reducido
    return random.randint(1,10)
hp1=60
hp2=60

while True:
    for i in range(2):
        print(f"turno del jugador {i+1}")
        t = input("ataque = (t) o (enter): ")
        system("cls")
        if t =="t" or t=="":
            if i+1==1:
                attack = ataque()
                critic = critico()
                mis = miss()
                bloqued = bloq()
                if bloqued==bloq():
                    attack=attack*0.01
                    print("bloqueo!, daño reducido")
                if mis == miss():
                    attack=attack*0
                    print("fallo el attack")
                if critic == critico():
                    attack=attack*1.6
                    print("salio critico!")
                hp2= hp2-attack
                print(f"jugador 1 le infligio {attack} de daño a jugador 2")
                print(f"la salud del jugador 2 tiene {hp2} HP")
                if hp2 <=0:
                    print("jugador 1 se quedo sin HP")
                    break
            if i+1==2:
                attack = ataque()
                critic = critico()
                mis = miss()
                if bloqued==bloq():
                    attack=attack*0.01
                    print("bloqueo!, daño reducido")
                if mis == miss():
                    attack=attack*0
                    print("fallo el attack")
                if critic == critico():
                    attack=attack*1.6
                    print("salio critico!")
                hp1= hp1-attack
                print(f"jugador 2 le infligio {attack} de daño a jugador 1")
                print(f"la salud del jugador 1 tiene {hp1} HP")
                if hp1 <=0 :
                    print("jugador 1 se quedo sin HP")
                    break
    if hp1 <=0 :
        break
    if hp2 <=0 :
        break
