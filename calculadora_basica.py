#Alan Castellón Sánchez
numero4=0
numero1=1
#Desplegamos el menu
seleccion=str(input("Ingresa la operacion que quieres realizar\n 1.Suma\n 2.Resta\n 3.Multiplicar\n 4.Dividir\n"))
if seleccion.lower().strip()=="suma" or seleccion=="1":
    cantidad_de_numeros=eval(input("Ingresa la cantidad de numeros que vas a sumar: "))
    for i in range(1,cantidad_de_numeros+1):
        numero1=eval(input(f"Ingresa el numero {i}: "))
        numero4+=numero1

elif seleccion.lower().strip()=="resta" or seleccion=="2":
    numero1=eval(input("Ingresa el primer numero: "))
    numero2=eval(input("Ingresa el segundo numero: "))
    numero4=numero1-numero2

elif seleccion.lower().strip()=="multiplicacion" or seleccion=="3":
    numero1=eval(input("Ingresa el primer numero: "))
    numero2=eval(input("Ingresa el segundo numero: "))
    numero4=numero1*numero2
elif seleccion.lower().strip()=="division" or seleccion=="4":
    numero1=eval(input("Inserta el primer numero: "))
    numero2=eval(input("Ingresa el segundo numero: "))
    numero4=numero1/numero2
print(numero4)



