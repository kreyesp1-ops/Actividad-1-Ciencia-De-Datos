# =============================================================
# TALLER PRÁCTICO - FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON
# Ciencia de Datos - Unidad 1
# Actividad completa: 20 ejercicios (Bloques 1-6)
# =============================================================


# -------------------------------------------------------------
# 🔹 BLOQUE 1: DATOS ESTRUCTURADOS VS. NO ESTRUCTURADOS
# -------------------------------------------------------------

# Ejercicio 1: Crear una lista que represente datos estructurados y mostrar su tipo
edades = [18, 20, 22, 19, 21]  # Lista de edades de estudiantes (datos estructurados)
print("=== Ejercicio 1 ===")
print("Edades de estudiantes:", edades)
print("Tipo de dato:", type(edades))  # type() muestra el tipo de dato, en este caso <class 'list'>


# Ejercicio 2: Crear una variable tipo texto (dato no estructurado) y contar sus palabras
comentario = "Este curso de programacion es muy interesante"  # Texto libre (dato no estructurado)
print("\n=== Ejercicio 2 ===")
palabras = comentario.split()  # split() divide el texto en palabras usando espacios como separador
print("Comentario:", comentario)
print("Cantidad de palabras:", len(palabras))  # len() cuenta la cantidad de elementos en la lista


# Ejercicio 3: Crear un diccionario con información estructurada de un estudiante
estudiante = {
    "nombre": "Kevin",
    "edad": 20,
    "carrera": "Ingenieria"
}  # Diccionario que almacena información del estudiante como pares clave:valor
print("\n=== Ejercicio 3 ===")
print("Nombre:", estudiante["nombre"])  # Acceso a valores del diccionario mediante sus claves
print("Edad:", estudiante["edad"])
print("Carrera:", estudiante["carrera"])


# -------------------------------------------------------------
# 🔹 BLOQUE 2: TIPOS DE VARIABLES Y SINTAXIS BÁSICA
# -------------------------------------------------------------

# Ejercicio 4: Declarar variables de diferentes tipos e imprimir su tipo
entero = 10  # Número entero (int)
flotante = 3.5  # Número decimal (float)
cadena = "Python"  # Cadena de texto (str)
booleano = True  # Valor booleano True/False (bool)
print("\n=== Ejercicio 4 ===")
print("Tipo de 'entero':", type(entero))  # <class 'int'>
print("Tipo de 'flotante':", type(flotante))  # <class 'float'>
print("Tipo de 'cadena':", type(cadena))  # <class 'str'>
print("Tipo de 'booleano':", type(booleano))  # <class 'bool'>


# Ejercicio 5: Concatenar nombre y apellido almacenados en variables
nombre = "Kevin"
apellido = "Reyes"
print("\n=== Ejercicio 5 ===")
completo = nombre + " " + apellido  # El operador + concatena (une) cadenas de texto
print("Nombre completo:", completo)


# Ejercicio 6: Convertir una variable tipo string con valor numérico a entero y sumarle 10
numero = "15"  # Variable tipo string que contiene un número
print("\n=== Ejercicio 6 ===")
numero_entero = int(numero)  # int() convierte el string a número entero
resultado = numero_entero + 10  # Ahora podemos realizar operaciones aritméticas
print(f"Número original (string): '{numero}'")
print(f"Convertido a entero y sumado 10: {resultado}")


# -------------------------------------------------------------
# 🔹 BLOQUE 3: OPERADORES
# -------------------------------------------------------------

# Ejercicio 7: Calcular el promedio de tres números usando operadores aritméticos
a = 4
b = 3
c = 5
print("\n=== Ejercicio 7 ===")
promedio = (a + b + c) / 3  # Operadores aritméticos: + (suma) y / (división)
print(f"Números: {a}, {b}, {c}")
print(f"Promedio: {promedio:.2f}")  # :.2f formatea el número con 2 decimales


# Ejercicio 8: Usar operadores de comparación para verificar si un número es mayor que 50
num = 60
print("\n=== Ejercicio 8 ===")
print(f"¿El número {num} es mayor que 50?", num > 50)  # El operador > compara y retorna True o False


# Ejercicio 9: Usar operadores lógicos para verificar si una persona es mayor de edad y tiene licencia
edad = 20
licencia = True
print("\n=== Ejercicio 9 ===")
print(f"Edad: {edad}, Tiene licencia: {licencia}")
# El operador 'and' retorna True solo si ambas condiciones son verdaderas
print("¿Es mayor de edad Y tiene licencia?", edad >= 18 and licencia)


# -------------------------------------------------------------
# 🔹 BLOQUE 4: ESTRUCTURAS DE DATOS
# -------------------------------------------------------------

# Ejercicio 10: Crear una lista con 5 frutas e imprimir la tercera
frutas = ["manzana", "banano", "mango", "fresa", "uva"]  # Lista con 5 frutas
print("\n=== Ejercicio 10 ===")
print("Lista de frutas:", frutas)
print("Tercera fruta:", frutas[2])  # Los índices empiezan en 0, entonces el índice 2 es la tercera fruta


# Ejercicio 11: Añadir un elemento a la lista anterior
frutas.append("naranja")  # append() agrega un elemento al final de la lista
print("\n=== Ejercicio 11 ===")
print("Lista actualizada con nueva fruta:", frutas)


# Ejercicio 12: Crear una tupla con 3 ciudades y recorrerla con un ciclo
ciudades = ("Bogotá", "Medellín", "Cartagena")  # Las tuplas se definen con paréntesis y no se pueden modificar
print("\n=== Ejercicio 12 ===")
print("Ciudades en la tupla:")
for ciudad in ciudades:  # El ciclo for recorre cada elemento de la tupla
    print(" -", ciudad)


# Ejercicio 13: Crear un diccionario con productos y precios, mostrar solo las claves
productos = {
    "leche": 3500,
    "pan": 2000,
    "arroz": 4500,
    "aceite": 8000
}  # Un diccionario almacena pares clave:valor
print("\n=== Ejercicio 13 ===")
print("Productos disponibles (claves):", list(productos.keys()))  # .keys() retorna solo los nombres de los productos


# -------------------------------------------------------------
# 🔹 BLOQUE 5: CONTROL DE FLUJO
# -------------------------------------------------------------

# Ejercicio 14: Determinar si un número es par o impar
numero = 47  # Puedes cambiar este número para probar
print("\n=== Ejercicio 14 ===")
if numero % 2 == 0:  # El operador % (módulo) da el residuo de la división; si es 0 el número es par
    print(f"El número {numero} es PAR")
else:
    print(f"El número {numero} es IMPAR")


# Ejercicio 15: Usar un ciclo for para imprimir números del 1 al 10
print("\n=== Ejercicio 15 ===")
print("Números del 1 al 10:")
for i in range(1, 11):  # range(1, 11) genera números desde 1 hasta 10 (el 11 no se incluye)
    print(i, end=" ")  # end=" " hace que los números se impriman en la misma línea separados por espacio
print()  # Salto de línea al final


# Ejercicio 16: Usar un ciclo while para contar regresivamente desde 5 hasta 1
print("\n=== Ejercicio 16 ===")
print("Cuenta regresiva:")
contador = 5  # Variable que empieza en 5
while contador >= 1:  # El ciclo se repite mientras contador sea mayor o igual a 1
    print(contador, end=" ")
    contador -= 1  # Resta 1 al contador en cada iteración
print("\n¡Despegue! 🚀")


# Ejercicio 17: Clasificar una nota con estructura condicional (A, B, C o D)
nota = 3.7  # Puedes cambiar este valor para probar distintas notas
print("\n=== Ejercicio 17 ===")
print(f"Nota ingresada: {nota}")
if nota >= 4.5:
    clasificacion = "A"   # Excelente
elif nota >= 4.0:
    clasificacion = "B"   # Sobresaliente
elif nota >= 3.0:
    clasificacion = "C"   # Aprobado
else:
    clasificacion = "D"   # Reprobado
print(f"Clasificación: {clasificacion}")


# -------------------------------------------------------------
# 🔹 BLOQUE 6: INTEGRACIÓN DE CONCEPTOS
# -------------------------------------------------------------

# Ejercicio 18: Lista de 5 calificaciones, calcular promedio y verificar si aprueba (≥3.0)
calificaciones = [3.5, 2.8, 4.0, 3.9, 3.1]  # Lista con 5 notas del estudiante
print("\n=== Ejercicio 18 ===")
promedio = sum(calificaciones) / len(calificaciones)  # sum() suma todos los valores, len() cuenta cuántos hay
print(f"Calificaciones: {calificaciones}")
print(f"Promedio: {promedio:.2f}")  # :.2f muestra solo 2 decimales
if promedio >= 3.0:
    print("Estado: ✅ APRUEBA")
else:
    print("Estado: ❌ REPRUEBA")


# Ejercicio 19: Leer datos desde una lista de nombres e imprimirlos en mayúsculas
nombres = ["carlos", "maria", "juan", "ana", "pedro"]  # Simulación de lectura de datos desde una fuente
print("\n=== Ejercicio 19 ===")
print("Nombres en mayúsculas:")
for nombre in nombres:  # Recorre cada nombre de la lista
    print(nombre.upper())  # .upper() convierte el texto a mayúsculas


# Ejercicio 20: Pedir la edad al usuario y mostrar su rango etario
print("\n=== Ejercicio 20 ===")
edad = int(input("Ingresa tu edad: "))  # input() pide datos al usuario; int() convierte el texto a número entero
if edad <= 12:
    print("Eres un niño 🧒")
elif edad <= 17:
    print("Eres un adolescente 🧑")
elif edad <= 59:
    print("Eres un adulto 🧑‍💼")
else:
    print("Eres un adulto mayor 👴")


# =============================================================
# FIN DEL TALLER
# =============================================================
