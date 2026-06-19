matriz=[
    [0,0,0,0,0],
    [1,0,1,0,1],
    [0,1,0,1,0],
    [1,1,1,0,1],
    [0,1,0,1,1]
]
print("Matriz Original")
for fila in matriz:
    print(fila)
print("\n matriz modificada")

for i in range(0,5):
    for j in range(0,5):
        if matriz[i][j] == 1:
            matriz[i][j] = 5

for fila in matriz:
    print(fila)