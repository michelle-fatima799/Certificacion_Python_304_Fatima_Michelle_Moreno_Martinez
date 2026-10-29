#Ciclo externo para el numero de la base de la tabla de la base
for i in range(1,5):
    print(f"---Tabla ddel {i}---")
    #Ciclo interno nos multiplica la base(i) por el numero(j)
    for j in range(1,11):
        print(f"{i} X {j} =  {i*j}")
    print(f"AQUI TERMINA LA TABLA DEL {i}")
