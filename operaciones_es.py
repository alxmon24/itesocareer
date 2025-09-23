#operaciones básica, entrada y salida
#25/08/2025
#nombre: Alan Castellón Sánchez

'''
comentario de varias líneas
ejemplo: solicitar la edad al usuario y decirle su año de nacimiento.

algoritmo en pseudocódigo
1. Inicio
2. Ingresar edad
#= operador de almacenamiento, o asignación
3. anio=2025- edad
4. Imprimir anio
Fin

'''
print("hola mundo")
while True:
    try:
        edad=int(input("ingresa la edad:"))
        break
    except:
        print("Tiene que ser un numero")
pregunta1=str(input("ya cumpliste años?"))
if pregunta1 == "si" or pregunta1=="Si":
    nacimiento=2025-edad
else:
    nacimiento=2025-edad-1
print("Tu edad es", edad, ", y naciste en", nacimiento)
