#### Repaso Módulo 2 - Python Nivel Inicial ####

#Ejercicio 1
#Pedí el precio de un producto y mostrale: precio con IVA (21%)
precio = float(input("Ingrese el precio de un producto: "))
iva = precio * 0.21
total = precio + iva

print("El precio con IVA incluido:", total)

#Ejercicio 2
#Pedí un número y calculá: 3x³ - 2x² + 3x - 1
x = float(input("Ingrese un número: "))
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1

print(y)

#Ejercicio 3
#Pedí:
    #nombre
    #edad
#Mostrá: "Hola [nombre], tienes [edad] años"
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))

print("Hola", nombre + ", tienes", edad, "años") #Se usa + para unir el nombre con la coma

#Ejercicio 4
#Pedí la cantidad de horas trabajadas y el pago por hora.
    #Mostrá el sueldo total.
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))

sueldo = horas_trabajadas * pago_por_hora

print("El sueldo total es", sueldo, end="$\n")

#Ejercicio 5
#Pedí:
    #nombre
    #cantidad de productos
    #precio por producto
#Mostrá:
    #total a pagar
    #mensaje final personalizado
name = str(input("Ingrese su nombre: "))
cantidad_productos = int(input("Ingrese la cantidad de productos: "))
precio_por_producto = float(input("Ingrese el precio por producto: "))

total_a_pagar = cantidad_productos * precio_por_producto

print("Total a pagar a", name + ":", total_a_pagar, end="$")