# De Alan Castellón Sánchez
import random

# Ejercicio 1 (librería random): generar 5 contraseñas numéricas de 6 dígitos
def generar_contrasenas():
    print("Contraseñas generadas:")
    for i in range(5):  # Generar 5 contraseñas
        contrasena = ""
        for j in range(6):  # Cada contraseña tiene 6 dígitos
            contrasena += str(random.randint(0, 9))  # Dígito aleatorio entre 0 y 9
        print(contrasena)

# Ejercicio 2 (librería random): simular 10 tiradas de moneda
def tiradas_moneda():
    aguila = 0
    sello = 0
    for i in range(10):  # 10 tiradas
        tiro = random.randint(0, 1)  # 0 = sello, 1 = águila
        if tiro == 1:
            aguila += 1
        else:
            sello += 1
    print(f"Después de 10 tiradas:")
    print(f"Águilas: {aguila}")
    print(f"Sello: {sello}")

# Ejercicio 3 (librería random): separar 450 personas en dos grupos aleatorios
def separar_personas():
    grupo1 = random.randint(0, 450)  # Tamaño del primer grupo
    grupo2 = 450 - grupo1            # El resto va al segundo grupo
    print(f"Grupo 1: {grupo1} personas")
    print(f"Grupo 2: {grupo2} personas")

# Ejercicio 4 (librería random): simular temperaturas diarias de una semana
def temperaturas_semana():
    d1 = random.randint(15, 35)
    d2 = random.randint(15, 35)
    d3 = random.randint(15, 35)
    d4 = random.randint(15, 35)
    d5 = random.randint(15, 35)
    d6 = random.randint(15, 35)
    d7 = random.randint(15, 35)

    print("Temperaturas de la semana:")
    print(d1, d2, d3, d4, d5, d6, d7)

    promedio = (d1 + d2 + d3 + d4 + d5 + d6 + d7) / 7
    print(f"Promedio semanal: {promedio:.2f} °C")


temperaturas_semana()