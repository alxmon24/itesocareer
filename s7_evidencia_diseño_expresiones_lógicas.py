import math
a=4
b=7
c=8.6
d="sol"

#Segundo ejercicio

menor_de_edad= a>=18 or b>=18
"""
menor_de_edad = a>=18 or b>=18
menor de edad = 4>=18 or b>=18
menor_de_edad = False or False
menor_de_edad = False
"""
#Tercer ejercicio
check = c>=0 and c<=10
"""
check = c>=0 and c<=10
check = 8.6>=0 and 8.6<=10
check= True and True
check = True
"""
#Cuarto ejercicio
check2 = c<=0 and c>=10
"""
check2 = c<=0 and c>=10
check2 = 8.6<=0 and c>=10
check2 = False and False
check2 = False
"""
#Quinto ejercicio
check3 = check and c>=6
"""
check3 = check and c>=6
check3 = True and 8.6>=6
check3 = True and True
check3 = True
"""
#Sexto ejercicio
e6 = d < d.upper()
"""
e6 = D < D.upper()
e6 = "sol" < "SOL"
e6 = False   # 's' minúscula no es menor que 'S' mayúscula en orden ASCII/Unicode
"""
#Septimo
e7 = len(d) < a
"""
e7 = len(D) < A
e7 = 3 < 4
e7 = True
"""