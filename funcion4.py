lista=(10, 5, 7, 8, 9, 1, 3, 4, 6, 2)
def numero_mayor(lista):
    mayor =max(lista)
    
    return mayor



a=numero_mayor(lista)
print(a)



def numero_min_manual(lista):
    # Empezamos asumiendo que el primer número es el menor
    minimo = lista[0] 
    
    # Comparamos con el resto de los elementos
    for numero in lista:
        if numero < minimo:
            minimo = numero
            
    return minimo

b=numero_min_manual(lista)
print(b)