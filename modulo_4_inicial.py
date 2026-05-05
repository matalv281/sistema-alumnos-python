#### Módulo 4 - Python Nivel Inicial: Funciones, tuplas, diccionarios, excepciones y procesamiento de datos. ####

#### FUNCIONES
#Una función es un bloque de código que realiza una tarea específica y se puede reutilizar.

####¿Por qué necesitamos funciones?####
#Sin funciones:
    #print("Hola")
    #print("Hola")
    #print("Hola")
#Con funciones:
    #def saludar():
        #print("Hola")

    #saludar()
    #saludar()
    #saludar()
#Ventajas:
    #evitar repetir código
    #hacer programas más claros
    #reutilizar lógica

####Descomposición
#Descomposición = dividir un problema grande en partes pequeñas.
#Ejemplo:
    #Problema: programa de un cajero automático
        #Se divide en funciones:
            #def verificar_usuario():
                #pass

            #def retirar_dinero():
                #pass

            #def mostrar_saldo():
                #pass
#Cada función hace una tarea específica.

####¿De dónde provienen las funciones?
#Las funciones pueden venir de:
    #(1) Funciones incorporadas (built-in)
        #print()
        #input()
        #len()
    #(2) Funciones propias (definidas por el usuario)
        #def saludar():
            #print("Hola")
    #(3) Librerías
        #import math
        #math.sqrt(9)

####Tu primera función
#Estructura básica:
    #def nombre_funcion():
        #instrucciones
#Ejemplo:
def mensaje():
    print("Estoy aprendiendo funciones")

mensaje()
#Importante:
    #def define la función
    #() → parámetros (vacíos en este caso)
    #se ejecuta al llamarla

####Cómo funcionan las funciones
#Flujo de ejecución:
def saludar():
    print("Hola")

print("Inicio") #Inicio
saludar() #Hola
print("Fin") #Fin
#El programa:
    #Ejecuta línea por línea
    #Cuando encuentra la función → la ejecuta
    #Luego vuelve al flujo principal

#Importante: orden -> La función debe definirse antes de usarla.
#saludar()   #ERROR

#def saludar():
    #print("Hola")

####¿Cómo se comunican las funciones con su entorno?####
#Las funciones se comunican con el exterior mediante:
    #parámetros (entrada)
    #argumentos (valores que se pasan)

####Funciones parametrizadas
#Una función puede recibir datos:
def saludar(nombre):
    print("Hola", nombre) #nombre es un parámetro
#Uso:
saludar("Matías") #"Matías" es el argumento
#Ejemplo con varios parámetros
def sumar(a, b):
    print(a + b)

sumar(3, 5)

####Paso de parámetros posicionales
#Los argumentos se asignan según su posición.
def mostrar(a, b):
    print(a, b)

mostrar(1, 2) #a = 1, b = 2
mostrar(2, 1) #a = 2, b = 1

####Paso de argumentos de palabra clave
#Podemos indicar el nombre del parámetro:
def mostrar(a, b):
    print(a, b)

mostrar(a=1, b=2) #Más claro y flexible
#Ventaja
mostrar(b=2, a=1) #Funciona igual (no importa el orden)

####Combinación de argumentos posicionales y de palabras clave
#Podemos mezclar ambos:
def mostrar(a, b, c):
    print(a, b, c)

mostrar(1, b=2, c=3)
#Regla importante: Los posicionales primero, luego los keyword
#Incorrecto -> mostrar(a=1, 2, 3)  # ERROR

####Funciones parametrizadas: más detalles
#Valores por defecto
def saludar(nombre="Invitado"):
    print("Hola", nombre)

saludar() #Hola Invitado
saludar("Matías") #Hola Matías -> cambia el nombre
#Parámetros opcionales
def potencia(base, exponente=2):
    print(base ** exponente)

potencia(3)      # 9
potencia(3, 3)   # 27 -> cambia el exponente
#Importante: orden de parámetros
#def ejemplo(a, b=2): # CORRECTO
    #pass
#def ejemplo(a=2, b): # ERROR
    #pass

####Devolver un resultado de una función####
#Hasta ahora, las funciones hacían cosas (print).
#Ahora van a devolver resultados.

####Efectos y resultados: la instrucción return
#Diferencia clave:
    #Efecto → lo que la función hace (ej: print)
    #Resultado → lo que la función devuelve (return)
#Ejemplo sin return
    #def sumar(a, b):
        #print(a + b)
#Ejemplo con return
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado) #Ahora sí podés usar el resultado.
#Importante:
    #return termina la función
    #devuelve un valor

####Unas palabras sobre None
#Si una función no tiene return, devuelve: None
#Ejemplo:
def saludar():
    print("Hola")

x = saludar()
print(x) # Hola None
#None significa: “sin valor”

####Efectos y resultados: listas y funciones
#Las funciones pueden trabajar con listas.
#Ejemplo: sumar elementos
def suma_lista(lista):
    total = 0
    for n in lista:
        total += n
    return total

print(suma_lista([1, 2, 3])) # 6
#Importante: listas son mutables
def modificar(lista):
    lista[0] = 99

nums = [1, 2, 3]
modificar(nums)

print(nums) # [99, 2, 3]
#La función puede modificar la lista original.

####LAB: Un año bisiesto
#Determinar si un año es bisiesto.
def es_bisiesto(anio):
    if anio % 4 != 0:
        return False #Es divisible por 4 → posible bisiesto
    elif anio % 100 != 0:
        return True #Pero si es divisible por 100 → deja de ser bisiesto
    elif anio % 400 != 0:
        return False #A menos que también sea divisible por 400 → vuelve a ser bisiesto
    else:
        return True

print(es_bisiesto(2024)) # True

####LAB: ¿Cuántos días?
#Cantidad de días en un mes.
def dias_en_mes(anio, mes):
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    elif mes in [4, 6, 9, 11]:
        return 30
    elif 1 <= mes <= 12:
        return 31
    else:
        return None

print(dias_en_mes(2026, 7))

####LAB: Día del año
#Día del año (ej: 15 de marzo → día 74)
def dia_del_anio(anio, mes, dia):
    total = 0

    for m in range(1, mes):
        total += dias_en_mes(anio, m)

    return total + dia

print(dia_del_anio(2026, 3, 15))

####LAB: Números primos
#Determinar si un número es primo.
def es_primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(es_primo(951))

####LAB: Conversión del consumo de combustible
#Convertir consumo: litros/100km → millas por galón
def l100km_a_mpg(litros):
    return 235.214583 / litros

def mpg_a_l100km(mpg):
    return 235.214583 / mpg

print(l100km_a_mpg(728))
print(mpg_a_l100km(657.90))

####Scopes in Python (Ámbitos de variables)####
#El scope (alcance) define dónde existe una variable y dónde se puede usar.

####Funciones y ámbitos
#Hay dos tipos principales:
#Variable local: Existe solo dentro de la función.
def ejemplo():
    x = 10
    print(x)

ejemplo() # x solo existe dentro de la función
#Variable global: Existe fuera de la función.
x = 10

def ejemplo():
    print(x)

ejemplo() #La función puede leer variables globales
#Error típico
def ejemplo():
    x = 5

ejemplo()
print(x)  # ERROR -> x no existe fuera

####Funciones y ámbitos: la palabra clave global
#Por defecto: una función no puede modificar variables globales
#Ejemplo incorrecto
    #x = 10

    #def cambiar():
        #x = x + 5  # ERROR

    #cambiar()
#Solución global
x = 10

def cambiar():
    global x
    x = x + 5

cambiar()
print(x) # 15
#global permite acceder y modificar una variable global
#Advertencia: Usar global no es buena práctica en exceso -> mejor usar parámetros y return

####¿Cómo interactúa la función con sus argumentos?
#Cuando pasás argumentos a una función -> se comportan diferente según el tipo
#Tipos inmutables (no cambian) -> Ej: int, float, str
def modificar(x):
    x = 100

a = 10
modificar(a)

print(a) # 10 -> No cambia el original
#Tipos mutables (sí cambian) -> Ej: listas
def modificar(lista):
    lista[0] = 99

nums = [1, 2, 3]
modificar(nums)

print(nums) # [99, 2, 3]
#Importante:
    #int y str -> no se modifican afuera
    #list -> sí se modifica afuera

####Creación de funciones con múltiples parámetros####
#Funciones con varios parámetros para resolver problemas reales.

####Funciones de ejemplo: Evaluación del BMI
#El BMI (Índice de Masa Corporal) se calcula: peso / altura²
#Función:
def bmi(peso, altura):
    return peso / (altura ** 2)

resultado = bmi(70, 1.75) # Uso
print(resultado) # ≈ 22.86
#Versión mejorada
def bmi(peso, altura):
    if altura <= 0:
        return None
    return peso / (altura ** 2)

resultado = bmi(70, 1.75) # Uso
print(resultado) # ≈ 22.86

####Funciones de ejemplo: Triángulos
#Verificar si tres lados forman un triángulo.
#Regla: cada lado < suma de los otros dos
#Función
def es_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(es_triangulo(3, 4, 5))  # True
#Tipo de triángulo (extra)
def es_rectangulo(a, b, c):
    return a**2 + b**2 == c**2

print(es_triangulo(3, 4, 5))  # True

####Funciones de ejemplo: Factoriales
#El factorial de n: n! = n × (n-1) × ... × 1
#Función:
def factorial(n):
    if n < 0:
        return None

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado

print(factorial(5))  # 120

####Números de Fibonacci
#Secuencia: 0, 1, 1, 2, 3, 5, 8... -> cada número = suma de los dos anteriores
#Función iterativa:
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

print(fibonacci(6))  # 8

####Recursión -> Una función que se llama a sí misma
#Ejemplo: factorial recursivo
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#Ejemplo: Fibonacci recursivo
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(factorial(5))
#Importante:
#Toda recursión necesita:
    #Caso base (para detenerse)
    #Llamada recursiva
#Problema:
#La recursión puede ser:
    #lenta
    #consumir mucha memoria
#Por eso muchas veces se usa versión iterativa

####Tuplas y diccionarios####

####Tipos de secuencia y mutabilidad
#Tipos de secuencia en Python:
    #listas (list)
    #tuplas (tuple)
    #strings (str)
#Mutabilidad
#¿Se puede modificar?:
    #Lista -> sí
    #Tupla -> no
    #Cadena (str) -> no
#Ejemplo:
    #lista = [1, 2, 3]
    #lista[0] = 99 -> permitido

    #tupla = (1, 2, 3)
    # tupla[0] = 99 -> ERROR
#Mutable = se puede cambiar
#Inmutable = no se puede cambiar

####Tuplas
#Una tupla es como una lista, pero no se puede modificar.
#Crear una tupla -> tupla = (1, 2, 3)
#Acceder -> print(tupla[0])  # 1
#Tupla de un solo elemento -> t = (5,)  # la coma es obligatoria
#Usos típicos
    #datos que no deben cambiar
    #devolver múltiples valores
#def datos():
    #return (10, 20)

#x, y = datos()

####Diccionarios
#Un diccionario almacena datos en forma: clave → valor
#Crear un diccioario
persona = {
    "nombre": "Matías",
    "edad": 25
}

print(persona["nombre"]) # Acceder a valores
#Modificar
    #persona["edad"] = 26
# Agregar
    #persona["ciudad"] = "Buenos Aires"

####Métodos y funciones del diccionario
#keys() -> print(persona.keys())
#values() -> print(persona.values())
#items() -> for clave, valor in persona.items():
                #print(clave, valor)
#get() -> print(persona.get("nombre")) -> evita errores si no existe la clave.
#in -> print("edad" in persona)

####Las tuplas y los diccionarios pueden trabajar juntos -> Podés combinarlos.
#Diccionario con tuplas
#datos = {
    #"punto": (10, 20)
#}
#Lista de tuplas
#pares = [(1, 2), (3, 4)]
#Uso típico: recorrer
#persona = {"nombre": "Ana", "edad": 30}

#for clave, valor in persona.items():
    #print(clave, valor)

####Excepciones####
#Las excepciones permiten que tu programa:
    #no se rompa cuando ocurre un error
    #maneje situaciones inesperadas

####Errores: el pan de cada día del desarrollador.
#Los errores son normales en programación.
#Tipos comunes:
    #errores de sintaxis
    #errores en tiempo de ejecución
    #errores lógicos
#Ejemplo:
#print(10 / 0) -> ERROR: División por cero → programa se detiene

####Cuando los datos no son lo que deberían ser
#Errores por datos incorrectos:
#edad = int(input("Edad: ")) -> si escriben "hola" → error -> ValueError

####La rama try-except
#Permite capturar errores:
try:
    x = int(input("Número: "))
    print(10 / x)
except:
    print("Ocurrió un error")
#Flujo:
    #try → intenta ejecutar
    #except → maneja el error

####La excepción confirma la regla
#El programa sigue funcionando aunque haya error.
try:
    print(10 / 0)
except:
    print("Error controlado")

print("El programa sigue")

####Cómo lidiar con más de una excepción
#Podés manejar distintos errores:
try:
    x = int(input("Número: "))
    print(10 / x)
except ValueError:
    print("Entrada inválida")
except ZeroDivisionError:
    print("No se puede dividir por cero")

####La excepción default y cómo usarla
#Capturar cualquier error:
#try:
    #...
#except Exception: -> Exception es el padre de todos los errores
    #print("Error general")

####Algunas excepciones útiles
#Algunas importantes:
    #ValueError → dato inválido
    #TypeError → tipo incorrecto
    #ZeroDivisionError → dividir por cero
    #IndexError → índice fuera de rango
    #KeyError → clave inexistente
#Ejemplo:
#lista = [1, 2]
#print(lista[5]) -> IndexError

####Por qué no puedes evitar probar tu código
#Siempre hay errores posibles. Por eso:
    #hay que probar el código
    #cubrir casos extremos

####Cuando Python cierra los ojos
#A veces ocultar errores es peligroso:
#try:
    #...
#except:
    #pass
#Ignora el error completamente

####Pruebas, pruebas y probadores
#Tipos de pruebas:
    #manuales
    #automáticas
    #usuarios reales
#Objetivo:
    #detectar errores antes de producción

####Print debugging
#Técnica básica:
#print("Valor de x:", x) -> ayuda a entender qué pasa

####Algunos consejos útiles
    #Manejar errores específicos
    #No abusar de except general
    #Validar datos antes
    #Usar mensajes claros

####Pruebas unitarias: un nivel superior de codificación
#Pruebas automáticas:
#def sumar(a, b):
    #return a + b

#assert sumar(2, 3) == 5 -> Verifica que el código funcione