lista =[4, 18, 22, 16, 1]
def mmayorlista(lista):
    mayor = lista[0]
    for i in range(1,len(lista)):
            if lista[i] > mayor:
             mayor = lista[i]
    return mayor
print(mmayorlista(lista))