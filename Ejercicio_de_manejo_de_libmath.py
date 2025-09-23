# De Alan Castellón Sánchez
import math

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

promedio_calificaciones()