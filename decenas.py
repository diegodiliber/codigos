def operacion (x,y):
    def suma (a, b):
        return a + b
    return suma (x,y)
    resultado = operacion(5,3)
    print(f"el resultado de la operacion es: {resultado}")