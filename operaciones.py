def operaciones(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return suma, resta, multiplicacion, division
resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = operaciones(10,5)
print(resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)