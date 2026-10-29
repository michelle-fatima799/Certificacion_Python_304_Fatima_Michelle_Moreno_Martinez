tablas =[
    ["Nombre","Edad","Calificacion"],
    ["Michelle",16,9.0],
    ["Aaron",17,7.0],
    ["Angela",16,6.0],
    ["Keilany",16,8.0],
    ["Santiago",17,7.5],
    ["Alma",16,9.0],
    ["Jorge",16,9.0],
    ["Danna",16,6.0],
    ["Joshua",16,6.0],
    ["Angel",16,7.0]
]
filas = len(tablas)
columnas = len(tablas[0])
buscar_nombre = input("Ingresa el nombre:")
for i in range(filas):
    for j in range(columnas):
        if j == 0 and tablas[i][j] == buscar_nombre:
            print(f"Nombre encontrado en la posicion [{i}] [{j}]")



persona={
    "nombre":"isabel",
    "edad":16,
    "profesion":"ingenieria",
    "estudiante":"False"
}
print(persona)
print(persona["estudiante"])
print(persona["nombre"])
print(persona.get("edad"))

persona["edad"]=67
print(persona.get("edad"))
#Agregar un par(clave:valor)
persona["ciudad"]="san pepe racho"
print(persona)
#RECORRER DICIONARIO CON UN BLUCLE
for clave,valor in persona.items():
    print(f"{clave}:{valor}")





