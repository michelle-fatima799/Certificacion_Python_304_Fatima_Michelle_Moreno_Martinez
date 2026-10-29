persona={
    "nombre":"Michelle",
    "edad":16,
    "profesion":"Programador",
    "estudiante":False
}
print(persona)
print(persona["nombre"])
print(persona.get("Profesion"))
persona["edad"]=13
print(persona["edad"])
persona["ciudad"]="san pepe Rach"
print(persona)
