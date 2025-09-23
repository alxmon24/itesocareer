def ejercicio1():
    numero=eval(input("Ingresa un numero: "))
    numero=numero%2
    if numero == 0:
        print("Tu numero es par")
    else:
        print("No es par")

def ejercicio2():
    calificacion=eval(input("Ingresa tu calificacion: "))
    if calificacion in range (0,10):
        if calificacion >= 6:
            print("Aprobaste")
        else:
            print("Reprobaste")
    else:
        print("Calificacion no valida")
def ejercicio3():
    costo=eval(input("Introduce el costo de tu compra: "))
    if costo >= 1500:
        if costo >=3000:
            if costo>= 5000:
                costof=costo-(costo*0.15)
            else:
                costof=costo-(costo*0.10)
        else:
            costof=costo-(costo*0.05)
    else:
        print("El precio se queda igual")
    print(f"El costo con descuento es {costof}")
ejercicio3()

