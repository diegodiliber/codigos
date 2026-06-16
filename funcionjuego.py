import numpy as np
def generartableroincial(tablero):
    rng = np.random.default_rng()
    for i in range(0,4):
        for j in range(0.4):
            numero = int(rng.random()*2)
            while(numero !=0 and numero !=1):
                numero = int(rng.random()*2)
                tablero[i][j]= numero
                return tablero
            def validarjugadas(tablero,memoria, posx, posy):
                if memoria[posx][posy] == 1:
                    return "repetido"
    
    
    if tablero[posx][posy] == 1: # type: ignore
        memoria[posx][posy] = 1  # type: ignore
        return "impacto"
    else:
        memoria[posx][posy] = 1  # type: ignore
        return "sin impacto"
tablero = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
memoria=[   
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
tablero = generartableroincial(tablero)
print("Tablero Generado (Minas):")
for fila in tablero:
    print(fila)

print("\nHaciendo una jugada de prueba en la posición (0,1)...")
resultado = validarjugadas(tablero, memoria, 0, 1) # type: ignore
print(f"Resultado del tiro: {resultado}")