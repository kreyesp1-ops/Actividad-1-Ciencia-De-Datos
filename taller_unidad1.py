# Ejercicio 1
edades = [18, 20, 22, 19, 21]

print(edades)
print(type(edades))

# Ejercicio 2
comentario = "Este curso de programacion es muy interesante"

palabras = comentario.split()

print("Cantidad de palabras:", len(palabras))

# Ejercicio 3
estudiante = {
    "nombre": "Kevin",
    "edad": 20,
    "carrera": "Ingenieria"
}

print(estudiante["nombre"])
print(estudiante["edad"])
print(estudiante["carrera"])

# Ejercicio 4
entero = 10
flotante = 3.5
cadena = "Python"
booleano = True

print(type(entero))
print(type(flotante))
print(type(cadena))
print(type(booleano))

# Ejercicio 5
nombre = "Kevin"
apellido = "Reyes"

completo = nombre + " " + apellido

print(completo)

# Ejercicio 6
numero = "15"

numero_entero = int(numero)

resultado = numero_entero + 10

print(resultado)

# Ejercicio 7
a = 4
b = 3
c = 5

promedio = (a + b + c) / 3

print(promedio)

# Ejercicio 8
num = 60

print(num > 50)

# Ejercicio 9
edad = 20
licencia = True

print(edad >= 18 and licencia)
