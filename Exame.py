
import numpy as np

rng = np.random.default_rng()

numero = int(rng.random()*10)
while(numero <0 and numero >10):
   numero = int(rng.random()*10)

print("")

Nombre=input("Ingrese su nombre: ")
print(f"\n---Bienvenido a Adivina {Nombre}---\n\n El juego consisite en adivinar\n un numero en un rango del 0-10\n")

nivel=int(input("Ingrese su nivel de dificultad Facil=1 Normal=2 Dificil=3 "))

if nivel==1: 
    print("\nSelecionaste el nivel facil tienes 9 intentos\n")
    jugadas=9

elif nivel==2:
    print("\nSelecionaste el nivel Normal tienes 6 intentos\n ")
    jugadas=6

elif nivel ==3: 
    print("\nSelecionaste el nivel Dificil tienes 3 intentos\n")
    jugadas=3
else: 
    print("\nNumero de nivel no valido se te asignara el nivel Facil\n")
    jugadas=9

a=numero*1

for k in range(0,jugadas):
    intento=int(input("¿Que numero crees que es?\n\n"))

    if intento == a:
        print("\n------ADIVINASTE!!!!-----\n")
        break

    else:
        print("\n------Numero erroneo-----\n")

print(f"Tu numero de intentos fue {k+1}")



