import math
import random
# De Alan Castellón Sánchez

def Punto1():
    # Ejercicio 1: Pedir nombre, segundo nombre y apellidos por separado
    nombre=str(input("Inserte su nombre: "))+" "
    nombre2=str(input("Inserte el segundo nombre, (En caso de no tener segundo nombre ponga NA)"))
    apellidop=str(input("Introduzca su apellido paterno: "))+" "
    apellidom=str(input("Introduzca su apellido materno: "))+" "
    
    # Validar si el segundo nombre es "NA" y eliminarlo en ese caso
    if nombre2.strip().lower() == "na":
        nombre2=""
    
    # Ejercicio 2: Concatenar todos los datos en una sola variable nombre_completo
    nombre_completo=nombre+nombre2+apellidop+apellidom
    print(nombre_completo)
    
    # Ejercicio 3: Crear un acrónimo con las iniciales en mayúsculas
    acronimo=nombre.capitalize()[0]
    if nombre2: # Solo si existe segundo nombre
        acronimo+=nombre.capitalize()[0]
    acronimo+=apellidop.capitalize()[0]
    acronimo+=apellidom.capitalize()[0]
    print(acronimo)
    
    # Ejercicio 4: Pedir una frase o letra y verificar si está en el nombre completo
    s=str(input("Introduzca su frase: "))
    # Verificar si s está en nombre_completo (True o False)
    print(s in nombre_completo)
    # Contar cuántas veces aparece s en nombre_completo
    print(nombre_completo.lower().count(s))
    
    # Ejercicio 5: Mostrar el nombre completo y su reverso
    print(nombre_completo + nombre_completo[::-1])
    
    # Ejercicio 6: Calcular cuántas letras tiene el nombre completo sin espacios
    cantidad_letras=len(nombre_completo.strip()) - nombre_completo.count(" ")+1
    print(cantidad_letras)

# Ejercicio 1 (librería math): calcular la magnitud de la diferencia de temperaturas
def diferencia_de_temperaturas():
    # Pedir las dos temperaturas al usuario
    t1 = float(input("Ingrese la temperatura inicial: "))
    t2 = float(input("Ingrese la temperatura final: "))
    
    # Calcular la diferencia absoluta usando math.fabs
    t3 = math.fabs(t1 - t2)
    
    # Mostrar el resultado en pantalla
    print(f"La diferencia de temperatura es de {t3}°C")

# Ejercicio 2 (librería math): calcular coordenadas (x, y) en una circunferencia
def operaciones_trigonometricas():
    a = math.pi  # Valor de la constante pi
    print(a)     # Mostrar pi como referencia
    
    # Pedir el radio de la circunferencia
    r = float(input("Ingrese el radio de la circunferencia: "))
    
    # Pedir el ángulo en grados
    O = float(input("Ingresa los grados: "))
    
    # Convertir los grados a radianes (necesario para usar sin y cos)
    radianes = math.radians(O)
    
    # Calcular la coordenada x = r * cos(θ)
    x = r * math.cos(radianes)
    
    # Calcular la coordenada y = r * sin(θ)
    y = r * math.sin(radianes)
    
    # Mostrar las coordenadas calculadas
    print(f"La coordenada es ({x},{y})")

# Ejercicio 3 (librería math): promedio de 3 calificaciones con diferentes redondeos
def promedio_calificaciones():
    # Pedir tres calificaciones al usuario
    c1 = float(input("Ingrese la primera calificación: "))
    c2 = float(input("Ingrese la segunda calificación: "))
    c3 = float(input("Ingrese la tercera calificación: "))
    
    # Calcular el promedio real
    promedio = (c1 + c2 + c3) / 3
    
    # Promedio redondeado hacia abajo
    promedio_floor = math.floor(promedio)
    
    # Promedio redondeado hacia arriba
    promedio_ceil = math.ceil(promedio)
    
    # Promedio con redondeo normal (round)
    promedio_round = round(promedio)
    
    # Mostrar resultados
    print("PROMEDIOS:")
    print(f"Sin redondeo: {promedio}")
    print(f"Redondeado hacia abajo: {promedio_floor}")
    print(f"Redondeado hacia arriba: {promedio_ceil}")
    print(f"Redondeo normal: {promedio_round}")
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

#Gracias a esta tarea aprendi a utilizar las funciones de las librerias math, y random. Tambien reforze mi conocimiento acerca del ciclo for ya que estaba algo oxidado. 