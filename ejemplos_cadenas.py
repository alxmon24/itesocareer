#ejemplos para manejo de cadenas en Python.

#iniciar una cadena, string, str abreviatura.
#inicio de una cadena vacía
s1 = ''
s2 = str()#crea una cadena

#inicio de una cadena con datos
s3 = str(3.141592)
s4 = "Hola"
s5 = input("Ingresa texto: ")

#calcular el tamaño o largo (lenght) de una cadena
lenght_s5 = len(s5)

print(s5,lenght_s5,type(s5))

#funciones de cadena
s5 = s5.strip()
lenght_s5 = len(s5)
print(s5,lenght_s5,type(s5))

#indexación de cadenas
primer_caracter_s5 = s5[0]
ultimo_caracter_s5 = s5[lenght_s5-1]
#ultimo_caracter_s5 = s5[lenght_s5] esta línea marca error fuera de rango.
print(primer_caracter_s5)
print(ultimo_caracter_s5)

#inmutabilidad de cadenas           
#s5[0] = "A" #esta línea marca error de no puedo asignar directamente.
#¿Cómo la cambiamos?

#indexación para obtener subcadenas
s6 = str(input("Ingrese "))
partebaja= s6[0:len(s6)//2]
partealta=s6[len(s6)//2:len(s6)]
print(partebaja)
print(partealta)
