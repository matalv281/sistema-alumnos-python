####Sistema de Gestión de Alumnos####

####Datos globales
alumnos = {}

####Funciones
#Agregar un alumno
def agregar(alumnos):
    nombre = input("Ingrese el nombre: ")
    try:
        nota = float(input("Ingrese la nota: "))
        alumnos[nombre] = nota
    except ValueError:
        print("Nota no válida")
#Mostrar alumnos
def mostrar(alumnos):
    for nombre, nota in alumnos.items(): #.items() devuelve una vista de pares clave-valor (tuplas) del diccionario
        print(f"{nombre}: {nota}")
#Buscar alumno
def buscar(alumnos):
    nombre = input("Ingresar el nombre a buscar: ")
    print(alumnos.get(nombre, "No encontrado"))
#Mostrar promedio
def promedio(alumnos):
    if len(alumnos) == 0:
        return 0
    return sum(alumnos.values()) / len(alumnos)
#Mostrar mejor promedio
def mejor_promedio(alumnos):
    if not alumnos:
        return None, None
    
    mejor_nombre = None
    mejor_nota = -1

    for nombre, nota in alumnos.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_nombre = nombre

    return mejor_nombre, mejor_nota
#Eliminar alumno
def eliminar(alumnos):
    nombre = input("Ingresar el nombre a eliminar: ")
    alumnos.pop(nombre, None) #.pop() elimina y devuelve (retorna) un elemento específico de una lista o diccionario

####Menú principal
def menu():
    print("\n---Menu---")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Mostrar promedio")
    print("5. Mostrar mejor promedio")
    print("6. Eliminar alumno")
    print("7. Salir")

####Programa principal
while True:
    menu()
    opcion = input("Elija una opción: ")

    if opcion == "1":
        agregar(alumnos)
    
    elif opcion == "2":
        mostrar(alumnos)
    
    elif opcion == "3":
        buscar(alumnos)

    elif opcion == "4":
        promedio = promedio(alumnos)
        print(f"El promedio total es {promedio}")
    
    elif opcion == "5":
        nombre, nota = mejor_promedio(alumnos)
        if nombre is not None:
            print(f"El mejor alumno es {nombre} con nota {nota}")
        else:
            print("No hay alumnos cargados")

    elif opcion == "6":
        eliminar(alumnos)

    elif opcion == "7":
        break

    else:
        print("Opción inválida")