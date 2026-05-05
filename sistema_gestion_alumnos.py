####Proyecto Python Nivel Inicial - Sistema de Gestión de Alumnos####

####Paso 1 - base del programa
lista_alumnos = {}

def menu_ppal():
    print("\n---Menu---")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Mostrar promedio")
    print("5. Mostrar mejor promedio")
    print("6. Eliminar alumno")
    print("7. Salir")

####Paso 2 - funciones clave
#Agregar un alumno
def agregar_alumno(alumnos):
    nombre = input("Ingrese el nombre: ")
    try:
        nota = float(input("Ingrese la nota: "))
        alumnos[nombre] = nota
    except ValueError:
        print("Nota no válida")
#Mostrar alumnos
def mostrar_alumnos(alumnos):
    for nombre, nota in alumnos.items(): # .items() devuelve una vista de pares clave-valor (tuplas) del diccionario
        print(f"{nombre}: {nota}")
#Buscar alumno
def buscar_alumno(alumnos):
    nombre = input("Ingresar el nombre a buscar: ")
    print(alumnos.get(nombre, "No encontrado"))
#Mostrar promedio
def mostrar_promedio(alumnos):
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
def eliminar_alumno(alumnos):
    nombre = input("Ingresar el nombre a eliminar: ")
    alumnos.pop(nombre, None) # .pop() elimina y devuelve (retorna) un elemento específico de una lista o diccionario

####Paso 3 - loop ppal
while True:
    menu_ppal()
    opcion = input("Elija una opción: ")

    if opcion == "1":
        agregar_alumno(lista_alumnos)
    
    elif opcion == "2":
        mostrar_alumnos(lista_alumnos)
    
    elif opcion == "3":
        buscar_alumno(lista_alumnos)

    elif opcion == "4":
        promedio = mostrar_promedio(lista_alumnos)
        print(f"El promedio total es {promedio}")
    
    elif opcion == "5":
        nombre, nota = mejor_promedio(lista_alumnos)
        if nombre is not None:
            print(f"El mejor alumno es {nombre} con nota {nota}")
        else:
            print("No hay alumnos cargados")

    elif opcion == "6":
        eliminar_alumno(lista_alumnos)

    elif opcion == "7":
        break

    else:
        print("Opción inválida")