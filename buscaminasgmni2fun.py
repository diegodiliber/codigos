import numpy as np

# 1. FUNCIÓN PARA GENERAR EL TABLERO ALEATORIO
def generar_tablero():
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


# --- FLUJO PRINCIPAL DEL JUEGO ---

# Bienvenida
jugador = input("Ingrese su nombre: ")
print(f"\nHola {jugador}, bienvenido a Buscaminas\n")

# Inicializamos el tablero con minas
minas_tablero = generar_tablero()
total_jugadas = configurar_dificultad()

# Creamos una lista vacía para registrar las coordenadas ya usadas
historial_jugadas = []

print("\n---------------- ¡A JUGAR! ----------------\n")

# Ciclo del juego
for k in range(total_jugadas):
    print(f"--- Intento {k + 1} de {total_jugadas} ---")
    
    # Este bucle se repetirá hasta que el usuario dé una coordenada válida y nueva
    while True:
        posx = int(input("Ingrese la posición x (0-3): "))
        posy = int(input("Ingrese la posición y (0-3): "))
        
        # Validar que no se salga de los límites de la matriz
        if posx < 0 or posx > 3 or posy < 0 or posy > 3:
            print("Coordenada inválida (fuera del rango 0-3). Ingrésala nuevamente.\n")
            continue  # Vuelve a pedir las coordenadas
            
        # Validar si la coordenada ya fue usada antes
        if (posx, posy) in historial_jugadas:
            print("Coordenada ya jugada anteriormente. Ingrésala nuevamente.\n")
            continue  # Vuelve a pedir las coordenadas
            
        # Si pasó las validaciones, salimos del bucle 'while' para procesar el disparo
        break

    # Guardamos la jugada actual en el historial
    historial_jugadas.append((posx, posy))
    
    # Evaluamos qué había en esa posición
    if minas_tablero[posx][posy] == 1:
        print("\n💥 ¡BOOM! Has pisado una mina. ¡PERDISTE EL JUEGO! 💥\n")
        break  # Rompe el ciclo 'for' por completo y termina el juego
    else:
        print("💧 A salvo. No hay mina aquí.\n")

# Fin del juego
print("--- Juego Terminado ---")
print("El tablero final era:")
print(np.matrix(minas_tablero))