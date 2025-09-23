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
    print(nombre_completo.lower().capitalize().upper().count(s))
    
    # Ejercicio 5: Mostrar el nombre completo y su reverso
    print(nombre_completo + nombre_completo[::-1])
    
    # Ejercicio 6: Calcular cuántas letras tiene el nombre completo sin espacios
    cantidad_letras=len(nombre_completo.strip()) - nombre_completo.count(" ")+1
    print(cantidad_letras)
Punto1()

