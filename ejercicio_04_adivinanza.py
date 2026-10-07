"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""
x = 40
while True:
    try:
        guess = int(input("Adivina el número: "))
        if guess < x:
            print("El número es mayor")
        elif guess > x:
            print("El número es menor")
        else:
            print("Adivinaste el número")
            break
    except ValueError:
        print("Entrada no válida")
