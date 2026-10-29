numero = int(input("Ingresa un numero del 1 al 10: "))
if 1<=numero <= 0:
    print("Tu numero no se acepta")                         
elif numero >=1 and numero<=10:
    i = 1
    while i <= 10:
        resultado = numero * i
        print (numero, "x", i, "=", resultado)
        i = i + 1
else:
    print("Ese numero no existe")