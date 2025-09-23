#Alan Castellón Sánchez

#Desplegamos el menu
def musica():
    seleccion=eval(input(f"Elige tu estilo musical favorito:\n 1-. Rock\n 2.-Regueton\n 3-.Pop\n 4-.Jazz\n 5.-Clasica\n"))
    match seleccion:
        case 1: #Lo que pasa si el usuario elige rock
            print("Queen, The rolling stones etc.")
        case 2: #Si elige regueton
            print("Bad bunny, Raw Alejandro etc.")
        case 3:# POP
            print("Michael Jackson, Maddona, etc.")
        case 4:#Jazz
            print("Louis Armstrong, Duke Ellington, etc.")
        case 5:
            print("Mozart, Debussy, Bethoveen")
def calculadora():
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

calculadora()