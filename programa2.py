import msvcrt

def area_triangulo():
    base=int(input("Ingrese la base el triangulo:"))
    altura=int(input("Ingrese la altura del triangulo: "))
    print("El area del triangulo es :"+str(base*altura/2))

def area_cuadrado():
    lado=int(input("Ingres el lado del cuadrado: "))
    print("El areal del cuadrado es: "+str(lado*lado))

def area_circulo():
    r=int(input("Ingrese el raio del circulo: "))
    print("El area del circulo es: "+str(r*r*3.1416))

def edad():
    año_nac=int(input("Ingrese su año de nacimiento: "))
    print("Su edad es: "+str(2021-año_nac))

def menu():
    print("1. Area Triangulo 2. Area Cuadrado 3. Area del Circulo 4. Que edad Tengo 5. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if(opcion==1):
        area_triangulo()
    elif(opcion==2):
        area_cuadrado()
    elif(opcion==3):
        area_circulo()
    elif(opcion==4):
        edad()
    else:
        print("El programa ha terminado")


menu()



msvcrt.getch()