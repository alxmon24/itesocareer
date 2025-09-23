# Alan Castellón Sánchez
print(f"{'Hola':>9s}Mundo")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

# Primer gasto
id1 = int(input("Ingresa el ID del producto: "))
descripcion = input("Ingresa el nombre del gasto: ")
monto = float(input("Ingresa el monto: "))

# Segundo gasto
id2 = int(input("Ingresa el segundo ID: "))
descripcion2 = input("Ingresa la descripcion: ")
monto2 = float(input("Ingresa el monto: "))

# Tercer gasto
id3 = int(input("Ingresa el tercer ID: "))
descripcion3 = input("Ingresa la descripcion: ")
monto3 = float(input("Ingresa el monto: "))

# Cuarto gasto
id4 = int(input("Ingresa el Cuarto ID: "))
descripcion4 = input("Ingresa la descripcion: ")
monto4 = float(input("Ingresa el monto: "))

# Quinto gasto
id5 = int(input("Ingresa el Quinto ID: "))
descripcion5 = input("Ingresa la descripcion: ")
monto5 = float(input("Ingresa el monto: "))

# Encabezado y tabla
print("-" * 50)
print(f"Registro de egresos de: {apellido}, {nombre}", end=" - ")
print("Hoja de Calculo")

print(f"{'\"Id\"':>5s} --- {'\"Descripción\"':20s} --- {'\"Monto\"':>9s}")
print(f"{id1:>5d} --- {descripcion:20s} --- ${monto:9.2f}")
print(f"{id2:>5d} --- {descripcion2:20s} --- ${monto2:9.2f}")
print(f"{id3:>5d} --- {descripcion3:20s} --- ${monto3:9.2f}")
print(f"{id4:>5d} --- {descripcion4:20s} --- ${monto4:9.2f}")
print(f"{id5:>5d} --- {descripcion5:20s} --- ${monto5:9.2f}")
