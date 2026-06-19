import numpy as np
import random

def generaraTableroInicial(tablero):
    rng = np.random.default_rng()
    for i in range(0, 4):
        for j in range(0, 4):
            numero=int(rng.ramdon()*10)
            while (numero!=0 and numero!=1):
                numero=int(rng.ramdon()*10)
            tablero[i][j]=numero
    return tablero

def validarJugada(tablero, posx,posy):
    if (tablero[posx][posy]==1):
      if memoria[posx][posy]==1:
        return "jugada ya realizada"
      else:
        return 'SIN IMPACTO'
    else:
        return 'SIN IMPACTO'
memoria = [
    [0, 0, 0 ,0], #0
    [0, 0, 0, 0], #1
    [0, 0, 0 ,0], #2
    [0, 0 ,0 ,0]  #3 
    #0/#1/#2/#3 
 ]
    

tablero = [
    [0, 0, 0 ,0], #0
    [0, 0, 0, 0], #1
    [0, 0, 0 ,0], #2
    [0, 0 ,0 ,0]  #3 
    #0/#1/#2/#3 
 ]
