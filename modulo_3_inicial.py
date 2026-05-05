#### Módulo 3 - Python Nivel Inicial: Valores booleanos, ejecución condicional, bucles, listas y procesamiento de listas, operaciones lógicas y a nivel de bits. ####
####
#Un programa puede hacer preguntas y obtener respuestas.
edad = int(input("Edad: "))
print(edad > 18)
#Esto devuelve:
    #True (verdadero)
    #False (falso)

#El operador de igualdad es: ==
#Ejemplos:
print(5 == 5)  # True
print(5 == 3)  # False
#No confundir:
    #   = → asignación
    #   == → comparación

#Operadores de comparación:
    #   == igual
    #   != distinto
    #   > mayor
    #   < menor
    #   >= mayor o igual
    #   <= menor o igual
#Ejemplos simples:
print(10 == 10) #True
print(10 != 5) #True
print(5 > 3) #True
print(2 < 1) #False
# Otro ejemplo:
x = 10
print(x >= 5)

#Podemos usar esos resultados para tomar decisiones:
edad = int(input("Edad: "))

if edad >= 18:
    print("Sos mayor de edad") #Si la condición es verdadera → se ejecuta el bloque

#Ejemplo típico: analizar el número ingresado
numero = int(input("Número: "))

print(numero > 0)
print(numero == 0)
print(numero < 0)

#Condición
#Estructura básica:
#if condicion:
    #instruccion
#Ejemplo:
x = 5

if x > 0:
    print("Es positivo") #Es positivo
#Importante: Usar indentación (tab o espacios)

#Análisis de ejemplos de código
#Ejemplo:
x = 10

if x > 5:
    print("Mayor que 5") #Mayor que 5

print("Fin") #Fin
#El if solo afecta su bloque

#El pseudocódigo es una forma de escribir lógica sin sintaxis estricta.
#Por ejemplo:
    #SI edad >= 18 ENTONCES
        #mostrar "Mayor de edad"
    #FIN
#Sirve para pensar antes de programar.

#LAB Operadores de comparación y ejecución condicional
#Ejemplo:
numero = int(input("Número: "))

if numero % 2 == 0:
    print("Es par")

#LAB Fundamentos de la declaración if-else
#Estructura:
    #if condicion:
        #instruccion1
    #else:
        #instruccion2
#Ejemplo:
edad = int(input("Edad: "))

if edad >= 18:
    print("Mayor")
else:
    print("Menor")

#LAB Fundamentos de la declaración if-elif-else
#Estructura para múltiples casos:
    #if condicion1:
        #...
    #elif condicion2:
        #...
    #else:
        #...
#Ejemplo:
numero = int(input("Número: "))

if numero > 0:
    print("Positivo")
elif numero == 0:
    print("Cero")
else:
    print("Negativo")

####
#Los loops permiten ejecutar instrucciones repetidamente.
#Tipos principales:
    #while → depende de una condición
    #for → recorre una secuencia

#Estructura básica de while
    #while condicion:
        #instruccion
#Ejemplo
contador = 1

while contador <= 5:
    print(contador)
    contador += 1 #1, 2, 3, 4, 5. Repite mientras la condición sea verdadera.

#Un bucle infinito nunca termina.
#while True:
    #print("Hola")
#Para frenarlo: Ctrl + C (en consola)

#Otro ejemplo con while
numero = 0

while numero != 5:
    numero = int(input("Ingresá 5: ")) #Se repite hasta que el usuario acierta.

#Adivina el número secreto
secreto = 7
numero = 0

while numero != secreto:
    numero = int(input("Adiviná el número: "))
    print("Intentá de nuevo...")

print("¡Correcto!")

#for se usa para repetir una cantidad fija de veces.
for i in range(5):
    print(i) #0, 1, 2, 3, 4

#for + range() con tres argumentos -> range(inicio, fin, paso)
#Ejemplo
for i in range(2, 10, 2):
    print(i) #2, 4, 6, 8

#LAB: counting mississippily
for i in range(1, 6):
    print(i, "Mississippi") #1 Mississippi, 2 Mississippi ... 5 Mississippi

print("Ready or not, here I come!")

#break rompe el bucle.
#Ejemplo
for i in range(10):
    if i == 5:
        break
    print(i) #0, 1, 2, 3, 4

#continua salta una iteración.
#Ejemplo
for i in range(5):
    if i == 2:
        continue
    print(i) #0, 1, 3, 4

#LAB: break – Atascado en un bucle
while True:
    palabra = input("Escribí 'salir': ")
    if palabra == "salir":
        break

#LAB: continuar – El feo devorador de vocales (eliminar vocales)
palabra = input("Palabra: ")

for letra in palabra:
    if letra in "aeiou":
        continue
    print(letra)

#LAB: Devorador de vocales bonito (mejora de lo anterior)
palabra = input("Palabra: ")
resultado = ""

for letra in palabra:
    if letra not in "aeiou":
        resultado += letra

print(resultado)

#while + else
i = 0

while i < 3:
    print(i) #0, 1, 2
    i += 1
else:
    print("Fin del while") #else se ejecuta cuando el bucle termina normalmente.

#for + else
for i in range(3):
    print(i) #0, 1, 2
else:
    print("Fin del for") #Igual lógica que en while

#LAB: Fundamentos del bucle while
contador = 1

while contador <= 10:
    print(contador) #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    contador += 1

#LAB: La hipótesis de Collatz
n = int(input("Número: "))

pasos = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    pasos += 1

print("Pasos:", pasos)

####
#Las computadoras trabajan con lógica booleana:
    #True → verdadero (1)
    #False → falso (0)
#Toda decisión en programación se basa en esto.
#Ejemplo:
print(5 > 3)   # True
print(2 > 10)  # False

#Las expresiones lógicas devuelven True o False.
#Operadores lógicos
#AND -> Solo es verdadero si TODO es verdadero.
print(True and True)   # True
print(True and False)  # False
#OR -> Basta con que uno sea verdadero.
print(True or False)   # True
#NOT -> Invierte el valor.
print(not True)   # False
print(not False)  # True
#Ejemplo real
edad = 20
tiene_dni = True

if edad >= 18 and tiene_dni:
    print("Puede votar")

#Valores lógicos frente a bits individuales
#Relación:
    #True ≈ 1
    #False ≈ 0
#Pero:
    #Booleano → lógica
    #Bit → representación en memoria

#Operadores bit a bit
#Operan bit a bit (nivel binario).
#AND (&)
print(5 & 3) # 5 = 101 y 3 = 011 -> resultado = 001 → 1
#OR (|)
print(5 | 3)  # 7
#XOR (^) -> Da 1 solo si los bits son distintos.
print(5 ^ 3)  # 6
#NOT (~) -> Invierte bits (resultado negativo por complemento a dos)
print(~5) # -6

#Trabajar con bits implica usar representación binaria.
#Ejemplo:
x = 10
print(bin(x)) # 0b1010 -> Cada número es una secuencia de bits.

#Ejemplo práctico: encender/apagar bits
x = 4  # 100
y = 1  # 001

print(x | y)  # 101 → 5

#Desplazamiento binario a la izquierda y desplazamiento binario a la derecha.
#Desplazamiento a la izquierda (<<)
print(5 << 1) #Multiplica por 2
    # 5 = 101
    # → 1010 = 10
#Desplazamiento a la derecha (>>)
print(5 >> 1) #Divide por 2 (entero)
    # 5 = 101
    # → 10 = 2
#Ejemplos:
print(3 << 2)  # 12
print(8 >> 2)  # 2

####
#Una lista es una estructura que permite guardar muchos valores en una sola variable.
#¿Por qué necesitamos listas?
    #Sin listas:
        #a = 10
        #b = 20
        #c = 30
    #Con listas:
        #numeros = [10, 20, 30]
#Ventaja:
    #agrupar datos
    #recorrerlos con loops
    #manipularlos fácilmente

#Listas de indexación
#Cada elemento tiene una posición (índice).
    #numeros = [10, 20, 30]
#Siempre empiezan en 0

#Acceder a elementos:
numeros = [10, 20, 30]

print(numeros[0])  # 10
print(numeros[2])  # 30
#También podes modificar:
numeros[1] = 99 # [10, 99, 30]

#Eliminar elementos -> del
numeros = [10, 20, 30]
del numeros[1]

print(numeros)  # [10, 30]

#Podés acceder desde el final:
numeros = [10, 20, 30]

print(numeros[-1])  # 30
print(numeros[-2])  # 20
#Muy útil para trabajar con el último elemento.

#LAB: Conceptos básicos sobre listas
numeros = [1, 2, 3, 4, 5]

for n in numeros:
    print(n) #Recorre toda la lista.

#Funciones vs. métodos
#Diferencia clave:
    #Función → independiente
    #Método → pertenece a un objeto
#Ejemplo:
    #len([1, 2, 3]) -> función
    #lista.append(4) -> método

#Agregar elementos: append() e insert()
#append() agrega al final.
    #numeros = [1, 2]
    #numeros.append(3)
#insert() agrega en posición específica.
    #numeros.insert(1, 99)

#Utilizar listas
#Ejemplo práctico -> Lista dinámica con input
numeros = []

for i in range(5):
    n = int(input("Número: "))
    numeros.append(n)

print(numeros)

#Listas en acción
numeros = [5, 3, 8, 1]

maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print("Mayor:", maximo)

#LAB: The Beatles
beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

beatles.append("Stu Sutcliffe")
beatles.append("Pete Best")

del beatles[-1]  # eliminar Pete Best
del beatles[-1]  # eliminar Stu Sutcliffe

beatles.insert(0, "Ringo Starr")

print(beatles)

####
#El algoritmo Bubble Sort
#El Bubble Sort funciona así:
    #Compara elementos de a pares
    #Si están desordenados → los intercambia
    #Repite hasta que todo esté ordenado
#Ejemplo visual:
    #Lista inicial -> [5, 3, 8, 1]
    #Paso a paso:
        # 5 > 3 → intercambiar → [3, 5, 8, 1]
        # 5 < 8 → no cambia
        # 8 > 1 → intercambiar → [3, 5, 1, 8]
        # Se repite hasta ordenar.
#Código básico
numeros = [5, 3, 8, 1]

n = len(numeros)

for i in range(n - 1):
    for j in range(n - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(numeros) #[1, 3, 5, 8]
#Sin embargo, Python tiene una forma mucho más simple: utilizar sort()
numeros = [5, 3, 8, 1]
numeros.sort()

print(numeros) #[1, 3, 5, 8]
#Orden descendente
    #numeros.sort(reverse=True)
# sort() -> modifica la lista != sorted() -> crea una nueva lista
#Versión con input del usuario:
numeros = []

cantidad = int(input("¿Cuántos números?: "))

for i in range(cantidad):
    n = int(input("Número: "))
    numeros.append(n)

# Bubble sort
n = len(numeros)

for i in range(n - 1):
    for j in range(n - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:", numeros)

####
#Las listas no guardan valores directamente, sino referencias.
#Esto significa que pueden comportarse de forma inesperada.
#Ejemplo
lista1 = [1, 2, 3]
lista2 = lista1

lista1[0] = 99

print(lista2) #[99, 2, 3] -> ambas variables apuntan a la misma lista.
#Copia real
lista1 = [1, 2, 3]
lista2 = lista1[:]

lista1[0] = 99

print(lista2) #[1, 2, 3]

#El slicing permite tomar partes de una lista: lista[inicio:fin]
#Ejemplo
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4]) #[20, 30, 40] -> Incluye inicio, excluye fin

#También funcionan con índices negativos:
numeros = [10, 20, 30, 40, 50]

print(numeros[-4:-1]) #[20, 30, 40]
#Otros ejemplos útiles
print(numeros[:3])   # primeros 3
print(numeros[2:])   # desde el índice 2
print(numeros[:])    # copia completa

#Los operadores in y not in sirven para verificar si un elemento está en la lista.
#Ejemplo
numeros = [1, 2, 3, 4]

print(3 in numeros)     # True
print(10 in numeros)    # False
print(5 not in numeros) # True

#Listas: algunos programas sencillos
# (1) Buscar un elemento:
numeros = [4, 7, 1, 9]
buscar = 7

encontrado = False

for n in numeros:
    if n == buscar:
        encontrado = True
        break

print("Encontrado:", encontrado) #Encontrado: True
# (2) Contar ocurrencias:
numeros = [1, 2, 2, 3, 2]
contador = 0

for n in numeros:
    if n == 2:
        contador += 1

print("Cantidad:", contador) #Cantidad: 3
# (3) Eliminar duplicados (simple)
numeros = [1, 2, 2, 3, 1]
sin_repetidos = []

for n in numeros:
    if n not in sin_repetidos:
        sin_repetidos.append(n)

print(sin_repetidos) #[1, 2, 3]

#LAB: Trabajar con listas -> conceptos básicos
#Dada una lista, eliminar repetidos.
lista = [1, 2, 3, 2, 1, 4]
nueva = []

for elemento in lista:
    if elemento not in nueva:
        nueva.append(elemento)

print("Sin duplicados:", nueva) #Sin duplicados: [1, 2, 3, 4]

####
#Listas en aplicaciones avanzadas
#Una lista puede contener otras listas.
#Ejemplo
lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] #Esto es una lista de listas
#Acceso a elementos.
#Ejemplo
print(lista[0])      # [1, 2, 3]
print(lista[1][2])   # 6 -> lista[1] → segunda fila, [2] → tercer elemento
#Ejemplo práctico
estudiantes = [
    ["Juan", 20],
    ["Ana", 22],
    ["Luis", 19]
]

print(estudiantes[0][0])  # Juan
print(estudiantes[1][1])  # 22

#Matrices bidimensionales
#Son listas que representan filas y columnas (matrices).
#Se accede como: matriz[fila][columna]
#Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[2][1])  # 8
#Recorrer una matriz
    #for fila in matriz:
        #for elemento in fila:
            #print(elemento)
#Crear matriz con ceros
filas = 3
columnas = 4

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(0)
    matriz.append(fila)

print(matriz) #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#Naturaleza multidimensional de las listas: aplicaciones avanzadas
#Las listas pueden tener más dimensiones: 3D, 4D, etc.
#Ejemplo 3D
datos = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(datos[1][0][1])  # 6
#Ejemplo tipo examen (suma de matriz)
matriz = [
    [1, 2],
    [3, 4]
]

suma = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento

print("Suma:", suma) # Suma: 10