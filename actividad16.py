suma = 0

numero = int(input("Introduce un número, para salir pon 0: "))

while numero != 0:
    suma = suma + numero
    numero = int(input("Introduce otro número, para salir pon 0: "))

print(f"La suma de todo es: {suma}")