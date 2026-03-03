import random

numero_secreto = random.randint(1,100)

contador = 0

print("¡Bienvenido. He pensado un numero entre 1 y 100. Adivinalo")

while True:
    intento = int(input("Apuesta colega:"))
    contador += 1
    
    if intento < numero_secreto:
        print("Es mayor")

    elif intento > numero_secreto:
        print("Es menor")

    else:
        print(f"¡Oleeeeeee! Adivinaste el numero secreto en {contador} intentos.")
        break