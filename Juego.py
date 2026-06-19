import numpy as np

tablero = [
    [0, 0, 0 ,0], #0
    [0, 0, 0, 0], #1
    [0, 0, 0 ,0], #2
    [0, 0 ,0 ,0]  #3 
    #0/#1/#2/#3 
 ]

        
rng = np.random.default_rng()
numero = int(rng.random()*10)

for i in range(0,4):
    for j in range(0,4):
        numero = int(rng.random()*10)
        while (numero != 0 and numero != 1):
            numero = int(rng.random()*10)
        tablero[i][j] = numero

print("")
jugador = input("Ingrese su nombre: ")
print (f'hola {jugador} bienvenido a buscaminas')
print("")
nivel= int(input("Ingrese el nivel de dificultad (1 facil ,2 medio ,3 dificil): "))
if 1== nivel:
  print("nivel facil")
  jugadas = 3
elif 2 == nivel:
    print("nivel medio")
    jugadas = 6
elif 3 == nivel:
    print("nivel dificil")
    jugadas = 9
else:
    print("nivel invalido, se asignara nivel facil")
jugadas = 3
print("")
print ('----------------Muga----------------')
print("")
for k in range(0,jugadas):
    posx= int(input("Ingrese la posicion x: "))
    posy= int(input("Ingrese la posicion y: "))
    if tablero[posx][posy] == 0:
        print("No hay mina")

    elif tablero[posx][posy] == 1:
        print("Hay mina")
    else:
        print("Posicion invalida")

print(tablero)
