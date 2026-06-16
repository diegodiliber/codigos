def filtrar_pared(lista):
    return [n for n in lista if n % 2 == 0]
numeros = [1,2,3,4,5,6]
pares = filtrar_pared(numeros)
print(pares)
