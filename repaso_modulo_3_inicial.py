#### Repaso Módulo 3 - Python Nivel Inicial ####

##Lógica + condiciones

#Ejercicio 1
#Pedí un número e indicá si:
    #es par
    #es múltiplo de 3
    #cumple ambas
numero = int(input("Ingrese un número: "))

es_par = numero % 2 == 0
es_multiplo_3 = numero % 3 == 0

if es_par and es_multiplo_3:
    print("El número ingresado es par y múltiplo de 3.")
elif es_par:
    print("El número ingresado es par.")
elif es_multiplo_3:
    print("El número ingresado es múltiplo de 3.")
else:
    print("El número ingresado no es par ni múltiplo de 3.")

#Ejercicio 2
#Pedí edad y si tiene documento (s/n):
    #Mostrar si puede votar (≥18 y tiene documento)
edad = int(input("Ingrese su edad: "))
dni = input("¿Posee DNI? (s/n): ").lower() #lower() evita problemas con mayúsculas

if edad < 18:
    print("No puede votar porque es menor de edad.")
elif dni != "s":
    print("No puede votar porque no tiene documento.")
else:
    print("Usted puede votar.")

##Loops + acumuladores

#Ejercicio 3
#Pedí números hasta que el usuario ingrese 0.
#Mostrar:
    #suma total
    #cantidad de números ingresados
suma = 0
contador = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

print("Suma total:", suma)
print("Cantidad de números ingresados:", contador)

#Ejercicio 4
#Pedí un número n y calculá:
    #suma de números de 1 a n
numero = int(input("Ingrese un número: "))
suma = 0

for i in range(1, numero + 1):
    suma += i

print("La suma de 1 a", numero, "es:", suma)

##Listas básicas

#Ejercicio 5
#Cargar 5 números en una lista.
#Mostrar:
    #lista completa
    #número mayor
    #número menor
lista = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

print("Lista completa:", lista)
print("Número mayor:", max(lista))
print("Número menor:", min(lista))

#Ejercicio 6
#Dada una lista, contar cuántos números son pares.

lista = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

contador_pares = 0

for numero in lista:
    if numero % 2 == 0:
        contador_pares += 1

print("Cantidad de números pares:", contador_pares)

##Listas + lógica

#Ejercicio 7
#Eliminar los números repetidos de una lista.
lista = []
nueva = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

for n in lista:
    if n not in nueva:
        nueva.append(n)

print("Sin duplicados:", nueva)

#Ejercicio 8
#Buscar un número dentro de una lista.
#Mostrar si está o no.
lista = [3, 7, 1, 9, 5]

buscado = int(input("Ingrese el número a buscar: "))

encontrado = False

for numero in lista:
    if numero == buscado:
        encontrado = True
        break

if encontrado:
    print("El número está en la lista.")
else:
    print("El número no está en la lista.")

##Ordenamiento
#Ejercicio 9
#Ordenar una lista usando bubble sort.
lista = [5, 3, 8, 4, 2]

n = len(lista)

for i in range(n):
    intercambio = False
    
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            intercambio = True
    
    if not intercambio:
        break

print("Lista ordenada:", lista)

#Ejercicio 10
#Cargar números y mostrarlos ordenados (podés usar .sort()).
lista = [5, 3, 8, 4, 2]
lista.sort()

print(lista)

##Strings + loops

#Ejercicio 11
#Pedí una palabra y:
    #eliminar vocales
    #mostrar resultado
palabra = str(input("Ingrese una palabra: "))
resultado = ""

for letra in palabra:
    if letra not in "aeiou":
        resultado += letra

print(resultado)

#Ejercicio 12
#Contar cuántas veces aparece una letra en una palabra.
palabra = input("Ingrese una palabra: ").lower()
letra = input("Ingrese una letra: ").lower()

contador = 0

for caracter in palabra:
    if caracter == letra:
        contador += 1

print("La letra aparece", contador, "veces.")

##Matrices

#Ejercicio 13
#Crear una matriz 3x3 con números ingresados por el usuario.
#Mostrar la matriz.
matriz = [
    [int(input("Ingrese un número: ")) for j in range(3)]
    for i in range(3) # i: elemento de cada fila (de izquierda a derecha); j: número de fila (de abajo hacia arriba)
]

for fila in matriz:
    print(fila)

#Ejercicio 14
#Calcular la suma de todos los elementos de una matriz.
matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        numero = int(input(f"Ingrese [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

suma = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento

print("Suma total:", suma)

#Ejercicio 15
#Mostrar:
    #suma de cada fila
    #suma de cada columna
matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        numero = int(input(f"Ingrese [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

# Filas
for i, fila in enumerate(matriz): #enumerate() es una función de Python que te permite recorrer una colección (lista, string, etc.) obteniendo a la vez el índice y el valor.
    print(f"Suma fila {i}:", sum(fila))

# Columnas
for j in range(len(matriz[0])):
    suma_col = 0
    for i in range(len(matriz)):
        suma_col += matriz[i][j]
    print(f"Suma columna {j}:", suma_col)

#Ejercicio 16
#Determinar si un número es primo.
#Un número primo:
    #es mayor que 1
    #solo es divisible por 1 y por sí mismo
numero = int(input("Ingrese un número: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("Es primo")
else:
    print("No es primo")

#Ejercicio 17
#Juego:
    #adivinar número (usar while)

#El programa:
    # 1) genera un número secreto
    # 2) el usuario intenta adivinarlo
    # 3) el programa da pistas: mayor o menor
    # 4) termina cuando acierta
import random

numero_secreto = random.randint(1, 100) #random.randint(1, 100) → genera número secreto
intentos = 0
max_intentos = 5

while intentos < max_intentos:
    intento = int(input("Adiviná el número (1-100): "))
    intentos += 1
    
    if intento == numero_secreto:
        print("¡Correcto!")
        break
    elif intento < numero_secreto:
        print("Muy bajo")
    else:
        print("Muy alto")

if intento != numero_secreto:
    print("Perdiste. El número era:", numero_secreto)

#Ejercicio 18 (FINAL)
#Dada una lista:
    #separar en:
        #pares
        #impares
lista = [1, 2, 3, 4, 5, 6]

pares = []
impares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Pares:", pares)
print("Impares:", impares)