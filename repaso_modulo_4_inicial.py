#### Repaso Módulo 4 - Python Nivel Inicial ####

####Funciones básicas
#Ejercicio 1:
#Crear una función que reciba un número y devuelva "par" o "impar".
def tipo_numero(n):
    if n % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."

n = int(input("Ingrese un número: "))
resultado = tipo_numero(n)
print(resultado)

#Ejercicio 2:
#Función que reciba dos números y devuelva el mayor.
def numero_mayor(m, n):
    if m > n:
        return f"El número {m} es mayor al número {n}."
    elif m < n:
        return f"El número {n} es mayor al número {m}."
    else:
        return "Los números ingresados son iguales."

m = int(input("Ingrese el primer número: "))
n = int(input("Ingrese el segundo número: "))
resultado = numero_mayor(m, n)
print(resultado)

####Funciones + listas
#Ejercicio 3:
#Crear una función que reciba una lista y devuelva la suma de sus elementos.
def suma_elementos(lista):
    total = 0
    for n in lista:
        total += n
    return total

lista = []

for i in range(3):
    n = int(input(f"Ingrese el número {i+1}: "))
    lista.append(n)

resultado = suma_elementos(lista)
print(resultado)

#Ejercicio 4:
#Función que reciba una lista y devuelva el número mayor.
def mayor_elemento(lista):
    return max(lista)

lista = []

for i in range(3):
    n = int(input(f"Ingrese el número {i+1}: "))
    lista.append(n)

resultado = mayor_elemento(lista)
print(f"El mayor número de la lista es {resultado}.")

#Ejercicio 5:
#Eliminar duplicados de una lista usando función.
def eliminar_duplicados(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista

lista = []

for i in range(4):
    n = int(input(f"Ingrese el número {i+1}: "))
    lista.append(n)

resultado = eliminar_duplicados(lista)
print(f"La lista es: {resultado}.")

####Funciones + lógica
#Ejercicio 6:
#Función que determine si un número es primo.
def es_primo(n):
    #Porque 0, 1 y negativos no son primos.
    if n <= 1:
        return False
    #Si un número tiene divisores, alguno está antes de √n.
    for i in range(2, int(n**0.5) + 1):
        #Significa que es divisible (encontramos un divisor), por lo que no es primo.
        if n % i == 0:
            return False
    
    return True

numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print("El número ingresado es primo.")
else:
    print("El número ingresado no es primo.")

#Ejercicio 7:
#Función que calcule el factorial de un número.
def factorial(n): ##El factorial de n: n! = n × (n-1) × ... × 1
    if n < 0:
        return None

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado

numero = int(input("Ingrese un número: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}.")

#Ejercicio 8:
#Función que calcule el término n de Fibonacci.
def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b

numero = int(input("Ingrese un número: "))
resultado = fibonacci(numero)
print(f"El término {numero} de Fibonacci es {resultado}.")

####Diccionarios
#Ejercicio 9:
#Crear una función que reciba un diccionario de alumnos y devolver el promedio.
def promedio_alumnos(diccionario):
    suma_alumnos = sum(diccionario.values())
    cantidad_alumnos = len(diccionario)
    return suma_alumnos / cantidad_alumnos

alumnos = {}

while True:
    nombre = input("Nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    
    nota = int(input("Nota: "))
    alumnos[nombre] = nota #El diccionario se arma así. Eso crea la relación clave → valor.

resultado = promedio_alumnos(alumnos)
print(f"El promedio general del alumnado es {resultado}.")

#Ejercicio 10:
#Función que busque una clave en un diccionario. Devolver:
    #valor si existe.
    #"No encontrado" si no existe.
def buscar_clave(diccionario, clave):
    return diccionario.get(clave, "No encontrado.")

alumnos = {}

while True:
    nombre = input("Nombre del alumno (o 'salir' para terminar): ")
    
    if nombre.lower() == "salir":
        break

    #Validar que no sea número.
    if nombre.isdigit():
        print("Error: debe ingresar un nombre válido.")
        continue
    #Validación de duplicados.
    if nombre in alumnos:
        print("Ese alumno ya existe, se actualizará la nota.")

    try:
        nota = int(input("Nota: "))
        alumnos[nombre] = nota
    #Validar que no sea texto.
    except ValueError:
        print("Error: debe ingresar un número válido.")

print(f"El diccionario es: {alumnos}")

#Pedir el nombre a buscar.
clave = input("Ingrese el nombre a buscar: ")

resultado = buscar_clave(alumnos, clave)
print(f"Resultado de la búsqueda: {resultado}")

####Excepciones
#Ejercicio 11:
#Crear función que:
    #pida un número.
    #maneje error si no es número.
def pedir_numero():
    while True:
        try:
            n = float(input("Ingrese un número: "))
            return n
        except ValueError:
            print("Error: debe ingresar un número válido.")

numero = pedir_numero()
print("Ingresaste el número:", numero)

#Ejercicio 12:
#Función que divida dos números y evite división por cero.
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división por cero."

m = int(input("Ingrese el primer número: "))
n = int(input("Ingrese el segundo número: "))
resultado = dividir(m, n)
print(f"El resultado de la división entre {m} y {n} es {resultado}.")

####Integradores
#Ejercicio 13:
#Crear un programa que:
    #Pida números al usuario.
    #Los guarde en una lista.
    #Use funciones para:
        #calcular suma.
        #calcular promedio.
        #encontrar el mayor.
def suma_lista(lista):
    total = 0
    for n in lista:
        total += n
    return total

def promedio_lista(lista):
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad

def mayor_lista(lista):
    return max(lista)

lista_elementos = []

for i in range(3):
    n = int(input(f"Ingrese el número {i+1}: "))
    lista_elementos.append(n)

calcular_suma = suma_lista(lista_elementos)
calcular_promedio = promedio_lista(lista_elementos)
encontrar_mayor = mayor_lista(lista_elementos)
print(f"La suma de los elementos de la lista es {calcular_suma}.") 
print(f"El promedio entre los elementos de la lista es {calcular_promedio}.")
print(f"El número mayor de la lista es {encontrar_mayor}.")

#Ejercicio 14:
#Crear un sistema de alumnos:
    #guardar nombres y notas en un diccionario.
    #mostrar:
        #promedio.
        #alumno con mejor nota.
def promedio(diccionario):
    suma_alumnos = sum(diccionario.values())
    cantidad_alumnos = len(diccionario)
    return suma_alumnos / cantidad_alumnos

def mejor_alumno(diccionario):
    if not diccionario:
        return None
    return max(diccionario, key=diccionario.get)

alumnos = {}

while True:
    nombre = input("Nombre del alumno (o 'salir' para terminar): ")
    
    if nombre.lower() == "salir":
        break

    #Validar que no sea número.
    if nombre.isdigit(): #Método de cadena (string) que devuelve True si todos los caracteres de la cadena son dígitos (del 0 al 9, incluyendo subíndices y superíndices), y False de lo contrario.
        print("Error: debe ingresar un nombre válido.")
        continue
    #Validación de duplicados.
    if nombre in alumnos:
        print("Ese alumno ya existe, se actualizará la nota.")

    try:
        nota = int(input("Nota: "))
        alumnos[nombre] = nota
    #Validar que no sea texto.
    except ValueError:
        print("Error: debe ingresar un número válido.")

print(f"El diccionario es: {alumnos}")

promedio_al = promedio(alumnos)
mejor_al = mejor_alumno(alumnos)
print(f"El promedio del curso es {promedio_al}.")
print(f"El alumno con la mejor calificación es {mejor_al}.")

#Ejercicio 15:
#Programa que:
    #Pida números hasta ingresar 0.
    #Guarde en lista.
    #Use funciones para:
        #eliminar duplicados.
        #separar pares e impares.
        #ordenar lista.
def eliminar_duplicados(lista):
    nueva = []
    for n in lista:
        if n not in nueva:
            nueva.append(n)
    return nueva

def separar_elementos(lista):
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

numeros = []

while True:
    numero = int(input("Ingrese un número (ingrese 0 para finalizar): "))
    if numero == 0:
        break
    numeros.append(numero)

numeros = eliminar_duplicados(numeros)
pares, impares = separar_elementos(numeros)
numeros.sort()

print(f"La lista ordenada es {numeros}")
print(f"Los números pares de la lista son {pares}")
print(f"Los números impares de la lista son {impares}")