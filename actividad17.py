contador = 0

palabra = input("Introduce una palabra, si quieres salir escribe fin: ")

while palabra != "fin":
    contador = contador + 1
    palabra = input("Introduce otra palabra, si quieres salir escribe fin: ")

print(f"Has introducido una cantidad de {contador} palabras")