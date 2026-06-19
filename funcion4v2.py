lista =[4, 18, 22, 16, 1]
def nummayor(lista):
    mayor = 0
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

print(f"el mayor es: {nummayor(lista)}")