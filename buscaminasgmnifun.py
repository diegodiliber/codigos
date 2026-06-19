import numpy as np

# 1. FUNCIÓN PARA GENERAR EL TABLERO ALEATORIO
def generar_tablero():
    # Creamos la matriz vacía de 4x4
    tablero = [[0 for _ in range(4)] for _ in range(4)]
    rng = np.random.default_rng()
    
    for i in range(4):
        for j in range(4):
            numero = int(rng.random() * 10)
            while numero != 0 and numero != 1:
                numero = int(rng.random() * 10)
            tablero[i][j] = numero
            
    return tablero


# 2. FUNCIÓN PARA CONFIGURAR LA DIFICULTAD
def configurar_dificultad():
    nivel = int(input("Ingrese el nivel de dificultad (1 facil, 2 medio, 3 dificil): "))
    
    if nivel == 1:
        print("Nivel fácil seleccionado.")
        return 3
    elif nivel == 2:
        print("Nivel medio seleccionado.")
        return 6
    elif nivel == 3:
        print("Nivel difícil seleccionado.")
        return 9
    else:
        print("Nivel inválido, se asignará nivel fácil.")
        return 3


# 3. FUNCIÓN PARA EL TURNO DE JUEGO
def verificar_jugada(tablero, x, y):
    # Validamos que no se salga de la matriz 4x4 (índices 0 a 3)
    if x < 0 or x > 3 or y < 0 or y > 3:
        return "Posición inválida (fuera del tablero)"
        
    if tablero[x][y] == 0:
        return "No hay mina"
    elif tablero[x][y] == 1:
        return "¡BOOM! Hay mina"


# --- FLUJO PRINCIPAL DEL JUEGO ---

# Bienvenida
jugador = input("Ingrese su nombre: ")
print(f"\nHola {jugador}, bienvenido a Buscaminas\n")

# Configuraciones iniciales llamando a las funciones
minas_tablero = generar_tablero()
total_jugadas = configurar_dificultad()

print("\n---------------- ¡A JUGAR! ----------------\n")

# Ciclo del juego usando el número de jugadas obtenido
for k in range(total_jugadas):
    print(f"--- Intento {k + 1} de {total_jugadas} ---")
    posx = int(input("Ingrese la posición x (0-3): "))
    posy = int(input("Ingrese la posición y (0-3): "))
    
    # Llamamos a la función para verificar el resultado
    resultado = verificar_jugada(minas_tablero, posx, posy)
    print(resultado)
    print("")

# Fin del juego: mostramos dónde estaban las minas
print("--- Juego Terminado ---")
print("El tablero era:")
print(np.matrix(minas_tablero))