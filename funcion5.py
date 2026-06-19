lista =[4, 18, 22, 16, 1, 22]
def nummayor(lista,num):
    cuantos = 0
    for elememto in lista:
        if elememto ==num :
            cuantos = cuantos+1
    return cuantos

print(f"el mayor es: {nummayor(lista,input("ingrese numero: "))}")