import turtle
import time
import random

# Configuracion de la ventana del juego
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Variables principales del juego
delay = 0.1
score = 0
high_score = 0
game_state = "menu"  # Puede ser: menu, instructions, playing, pause, game_over

# CREACION DE OBJETOS (TURTLES)
#  
# Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Comida para la serpiente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Lista para guardar los pedazos del cuerpo (segmentos)
segments = []

# Lapiz para escribir en la pantalla (puntajes y menus)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()


# FUNCIONES PARA CAMBIAR DE PANTALLA 

def show_menu():
    global game_state
    game_state = "menu"
    
    # Escondemos la serpiente y la comida fuera de la pantalla
    head.goto(1000, 1000)
    head.direction = "stop"
    food.goto(1000, 1000)
    
    # Borramos el cuerpo de la serpiente si veniamos de perder
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    
    # Dibujamos el menu principal
    pen.clear()
    pen.goto(0, 50)
    pen.write("BIENVENIDO A SNAKE", align="center", font=("Courier", 26, "bold"))
    pen.goto(0, -10)
    pen.write("Presiona [ 1 ] para Jugar", align="center", font=("Courier", 18, "normal"))
    pen.goto(0, -60)
    pen.write("Presiona [ 2 ] para Como se juega", align="center", font=("Courier", 18, "normal"))

def show_instructions():
    global game_state
    game_state = "instructions"
    
    pen.clear()
    pen.goto(0, 120)
    pen.write("COMO SE JUEGA", align="center", font=("Courier", 22, "bold"))
    pen.goto(0, 40)
    pen.write("- Usa W, A, S, D para moverte.", align="center", font=("Courier", 14, "normal"))
    pen.goto(0, 0)
    pen.write("- Presiona [ P ] para Pausar el juego.", align="center", font=("Courier", 14, "normal"))
    pen.goto(0, -40)
    pen.write("- No choques con las paredes ni contigo.", align="center", font=("Courier", 14, "normal"))
    pen.goto(0, -120)
    pen.write("Presiona [ ESC ] para volver", align="center", font=("Courier", 16, "bold"))

def start_game():
    global score, delay, game_state
    game_state = "playing"
    score = 0
    delay = 0.1
    
    # Limpiamos los segmentos viejos
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    
    # Reiniciamos posicion de la cabeza y comida
    head.goto(0, 0)
    head.direction = "stop"
    food.goto(random.randint(-270, 270), random.randint(-270, 270))
    
    pen.clear()
    update_score_board()

def pause_game():
    global game_state
    if game_state == "playing":
        game_state = "pause"
        pen.goto(0, 0)
        pen.write("JUEGO PAUSADO", align="center", font=("Courier", 28, "bold"))
        pen.goto(0, -40)
        pen.write("Presiona [ ESC ] para seguir", align="center", font=("Courier", 16, "normal"))

def resume_game():
    global game_state
    if game_state == "pause":
        game_state = "playing"
        pen.clear()
        update_score_board()

def show_game_over():
    global game_state
    game_state = "game_over"
    
    head.goto(1000, 1000)
    food.goto(1000, 1000)
    for segment in segments:
        segment.goto(1000, 1000)
    
    pen.clear()
    pen.goto(0, 40)
    pen.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
    pen.goto(0, -20)
    pen.write("Presiona [ R ] para Repetir", align="center", font=("Courier", 18, "normal"))
    pen.goto(0, -70)
    pen.write("Presiona [ ESC ] para el Menu", align="center", font=("Courier", 18, "normal"))

def update_score_board():
    if game_state == "playing":
        pen.clear()
        pen.goto(0, 260)
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))


# CONTROL DE TECLADO

def go_up():
    if game_state == "playing" and head.direction != "down":
        head.direction = "up"

def go_down():
    if game_state == "playing" and head.direction != "up":
        head.direction = "down"

def go_left():
    if game_state == "playing" and head.direction != "right":
        head.direction = "left"
    
def go_right():
    if game_state == "playing" and head.direction != "left":
        head.direction = "right"

def key_one():
    if game_state == "menu":
        start_game()

def key_two():
    if game_state == "menu":
        show_instructions()

def key_p():
    if game_state == "playing":
        pause_game()

def key_r():
    if game_state == "game_over":
        start_game()

def key_esc():
    if game_state == "pause":
        resume_game()
    elif game_state in ["instructions", "game_over"]:
        show_menu()


# Escuchador de eventos del teclado
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

wn.onkeypress(key_one, "1")
wn.onkeypress(key_two, "2")
wn.onkeypress(key_p, "p")
wn.onkeypress(key_p, "P")
wn.onkeypress(key_r, "r")
wn.onkeypress(key_r, "R")
wn.onkeypress(key_esc, "Escape")

# Mostramos el menu al arrancar el programa
show_menu()

#  FUNCION PARA MOVER LA SERPIENTE 

def move_snake():
    # Recorremos los segmentos de atras hacia adelante para que sigan a la cabeza
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # El primer segmento toma la posicion de la cabeza
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Movimiento de la cabeza segun la direccion guardada
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)


# LOOP PRINCIPAL (WHILE TRUE) 
while True:
    wn.update()
    
    # Solo corremos la logica si el estado es playing
    if game_state == "playing":
        
        # 1. Revisar si choca contra las paredes de la ventana
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(0.3)
            show_game_over()

        # 2. Revisar si la serpiente se come la comida
        if head.distance(food) < 20:
            # Mover la comida a un lugar aleatorio
            food.goto(random.randint(-270, 270), random.randint(-270, 270))

            # Crear un nuevo pedazo de cuerpo y agregarlo a la lista
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("blue")
            new_segment.penup()
            segments.append(new_segment)

            # Aumentar dificultad (bajar el delay) y sumar puntos
            delay = max(0.03, delay - 0.002)
            score += 10
            
            if score > high_score:
                high_score = score
                
            update_score_board()

        # Mover la serpiente en el tablero
        move_snake()

        # 3. Revisar colision con su propio cuerpo
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(0.3)
                show_game_over()

    # Pausa pequeña para controlar la velocidad del juego
    time.sleep(delay)

wn.mainloop()