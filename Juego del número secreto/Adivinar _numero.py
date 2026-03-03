#importar libreria
import random
#Generar numero secreto
numero_secreto = random.randint(0,100)
contador = 0
#imprime la bienvenida
print("Bienvenido al juego de adivinar el numero")
#bucle para adivinar el numero
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

