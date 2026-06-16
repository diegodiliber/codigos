def es_palindromo(palabra):
    return palabra == palabra[::-1]
palabra = input("ingrese una palabra: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palindromo")
else: print(f"{palabra} no es un palindromo")