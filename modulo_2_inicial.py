#### Módulo 2 - Python Nivel Inicial: Tipos de datos, variables, operadores y operaciones básicas de entrada/salida en Python. ####
####
print("Hello, World!") #Muestra el texto entre comillas en la consola.

#print() es una función incorporada de Python que sirve para mostrar información.
print("Hola") #Hola
print(5) #5
print(2 + 3) #5

#Los argumentos son los valores que le pasamos a una función.
print("Hola mundo") #"Hola mundo" es el argumento
print("Hola", "Matías") #También puede haber varios argumentos

#Invocar una función significa ejecutarla.
print("Hola") #print es el nombre de la función y () es la invocación

#Cada print() imprime en una nueva línea.
print("Mi nombre es Matías")
print("Estoy aprendiendo Python")
print("¡Es genial!")

#Efecto: muestra texto en pantalla
#Argumentos: lo que queremos imprimir
#Valor de retorno: None (no devuelve nada útil)
x = print("Hola") #Hola
print(x) #None

#Las instrucciones son las líneas de código que Python ejecuta.
print("Uno")
print("Dos")
#Se ejecutan de arriba hacia abajo.

#Caracteres especiales
#Salto de línea
print("Hola\nMundo")
#Comillas dentro de texto
print("Él dijo \"Hola\"") #Él dijo "Hola"

#Usar múltiples argumentos
#Podemos pasar varios valores separados por coma:
print("Hola", "Matías", 2026) #Hola Matías 2026
#Por defecto se separan con espacios.

#Argumentos posicionales
#Los argumentos se interpretan según su posición.
print("Hola", "Mundo") #Primero imprime "Hola", luego "Mundo".

#Argumentos de palabras clave
#Son argumentos con nombre.
#Ejemplo importante: sep y end
print("Hola", "Mundo", sep="-") #Hola-Mundo

print("Hola", end=" ")
print("Mundo") #Hola Mundo

#Ejemplo combinando lo visto
print("Python", "es", "genial", sep=" - ", end="!!!\n") #Python - es - genial!!!

#Formatear salida significa controlar cómo se ve.
print("Nombre:", "Matías")
print("Edad:", 25)

print("Nombre: %s \nEdad: %d" % ("Matías", 25)) #Otra forma

nombre = "Matías"
edad = 25
print(f"Nombre: {nombre} \nEdad: {edad}") #Otra forma (más moderno)

#Un literal es un valor que aparece directamente en el código.
#Es “el dato en sí mismo”, no una variable.
print(10)
print("Hola")
print(3.14)
print(True)
#Todos estos son literales porque están escritos directamente.

#Los integers (enteros) son números sin parte decimal.
print(10)
print(-5)
print(0)
#Características:
    #Pueden ser positivos o negativos
    #No tienen coma ni punto decimal
#También pueden escribirse en otros sistemas:
print(0b1010)  # binario → 10
print(0o12)    # octal → 10
print(0xA)     # hexadecimal → 10

#Los floats son números con decimales.
print(3.14)
print(-0.5)
print(2.0)
#Características:
    #Usan punto, no coma
    #Representan números reales
#También pueden usar notación científica:
print(3e2)   # 300.0
print(3e-2)  # 0.03

#Los strings son textos.
print("Hola")
print('Python')
#Características:
    #Van entre comillas simples ' ' o dobles " "
    #Representan texto
#Ejemplos:
print("Mi nombre es Matías")
print("123")  # esto es texto, no número

#Los booleanos representan valores lógicos.
print(True)
print(False)
#Solo existen dos valores:
    #True → verdadero
    #False → falso
#Se usan en condiciones:
print(5 > 3)  # True
print(2 > 10) # False

#Ejercicios típicos con strings:
print("Me gusta \"Python\"") #Me gusta "Python" (uso de comillas)
print("Hola " + "Mundo") #Hola Mundo (concatenación)
print("Ja" * 3) #JaJaJa (repetición de strings)
print("""Línea 1
Línea 2
Línea 3""") #Strings multilínea

#Los operadores permiten realizar operaciones con datos (números, textos, etc.).
#Python puede usarse como una calculadora.
#Ejemplos simples:
print(2 + 3)   # suma   #5
print(10 - 5)  # resta  #5
print(4 * 2)   # multiplicación #8
print(8 / 2)   # división   #4.0
#Notas importantes:
    #La división (/) siempre da float
    #No hace falta guardar en variables para calcular

#Estos son los operadores básicos en Python:
print(5 + 3)  # 8 (suma)
print(5 - 3)  # 2 (resta)
print(5 * 3)  # 15 (multiplicación)
print(5 / 2)  # 2.5 (división)
print(5 // 2)  # 2 (división entera) -> descarta los decimales
print(5 % 2)  # 1 (módulo) -> devuelve el resto
print(2 ** 3)  # 8 (potencia)

#Los operadores tienen un orden de prioridad (como en matemática).
#Orden (de mayor a menor):
    #   ** → potencia
    #   *, /, //, %
    #   +, -
print(2 + 3 * 4) #14 -> Primero se hace 3 * 4, luego se suma 2.
print((2 + 3) * 4) #20 -> Los paréntesis cambian la prioridad.
print(2 ** 3 ** 2) #512 -> La potencia se evalúa de derecha a izquierda.

#La función input() sirve para leer datos que escribe el usuario.
nombre = input()
print(nombre)
#El programa se detiene hasta que el usuario escribe algo.

#Podemos mostrar un mensaje antes de que el usuario escriba:
nombre = input("Ingrese su nombre: ")
print("Hola", nombre)
#Ese texto es una guía para el usuario.

#IMPORTANTE: input() siempre devuelve un string.
edad = input("Edad: ")
print(type(edad)) #<class 'str'>
#Aunque el usuario escriba un número, sigue siendo texto.

#No podés hacer operaciones matemáticas directamente con input():
    #edad = input("Edad: ")
    #print(edad + 5)  #ERROR
#Porque estás intentando sumar: string + entero → incompatible
#Para solucionar eso usamos conversión de tipos:
edad = int(input("Edad: "))
print(edad + 5)
#Funciones comunes:
    #int() → entero
    #float() → decimal
    #str() → texto

#En el siguiente ejemplo, convertimos antes de operar:
numero = float(input("Ingrese un número: "))
resultado = numero * 2
print("Resultado:", resultado)

#Los strings también tienen operadores:
print("Hola " + "Mundo") #Hola Mundo -> CONCATENACIÓN (+)
print("Ja" * 3) #JaJaJa -> REPETICIÓN (*)

#Podemos combinar tipos:
numero = 5
texto = "Edad: " + str(numero)
print(texto)
#Siempre que mezcles tipos → convertir.

#Ejercicios con input()
#Ejercicio 1
nombre = input("Nombre: ")
edad = input("Edad: ")

print("Hola", nombre)
print("Tenés", edad, "años")
#Ejercicio 2
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
#Ejercicio 3
x = float(input("x: "))

resultado = 3 * x**3 - 2 * x**2 + 3 * x - 1

print("Resultado:", resultado)