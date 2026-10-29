#Solicitar el numero por el teclado
numero = int(input("Ingresa un numero entre el 1 y el 10: "))

#Validar que el numero esta en el rango
if 1<=numero <= 10:
    print(f"\n--- Tabla de multiplicar del{numero} (6 iteraciones)---")
    # Bucle con 10 iteraciones (del 1 al 10)
    for i in range(1, 10):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Error: El numero ingresado esta fuera del rango permitido (1 al 10).")
