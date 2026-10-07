"""
EJERCICIO 02: Sumatoria

1. Pide números enteros al usuario constantemente usando un bucle while. 
2. Suma los valores ingresados.
3. Detén el bucle únicamente cuando el usuario ingrese el número 0. 
4. Al final, muestra la suma total.
"""
suma = 0
while True:
    try:
        numero = int(input("Ingrese un número entero 0 para detener: "))
        if numero == 0:
            break
        suma += numero
    except ValueError:
        print("Entrada no válida")
print(f"La suma total es: {suma}")