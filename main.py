
from random import randint
intentos = 8
respuesta=0
numero_oculto=randint(1,100)

print("================================")
print("Bienvenido a Adivina el Numero")
print("================================\n\n")

name_player=input("Dime tu nombre porfavor: ")

print(f"Bienvenido {name_player} estoy pensando en un numero entre 1 y 100 y solo tienes 8 intentos para adivinar el numero correcto")
print("\n\n\tEstas listo empezamos...")

while intentos>0:

    print(f"\n***************\t{name_player} Tienes {intentos} intentos ************")
    respuesta = int(input("\nDijita tu respuesta numerica: "))

    if numero_oculto == respuesta: 
        print(f"\nGanaste el numero oculto era: {numero_oculto} y tu respuesta fue: {respuesta} Ganaste en tu intento: {9-intentos}\n\n")
        break
    elif respuesta <0 or respuesta > 100:
        print("\nEste numero no esta dentro del rango de 1 - 100")
    elif respuesta < numero_oculto:
        print("\nRespuesta Incorrecta seleccionaste un numero menor")
        
    elif respuesta > numero_oculto:
        print("\nRespuesta Incorrecta seleccionaste un numero mayor")
    
    else: print(f"\n************ Lo siento perdiste Excediste el Numero de Intentos la respuesta correcta era {numero_oculto} ************")
    intentos-=1
 
