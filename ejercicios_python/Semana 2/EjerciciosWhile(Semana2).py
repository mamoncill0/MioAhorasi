"""
#1 Contar del 1 al 10:
#Usa un while para imprimir los números del 1 al 10.

contador = 1
while contador <10:
    contador = contador +1
    print(contador)

    """
#2 Contar hacia atrás:
#Usa un while para imprimir los números del 10 al 1 en orden descendente.

contador = [1,3,2,5,4,9,8,7,6,10]
ordenado = contador[:-1]
while ordenado:
    print(ordenado)
    break
"""

#3 Suma de los primeros 10 números:
#Usa un while para sumar los números del 1 al 10 e imprimir el resultado.

contador = 1
numeros = 0
while contador <=10:
    numeros += contador
    contador +=1
    print(numeros)


#4 Solicitar número positivo:
#Pide al usuario un número y usa un while para seguir pidiendo hasta que ingrese un número positivo.

numero = int(input("Pon un numero positivo "))
while numero < 0:
    print("No es positivo")
    numero = int(input("Pon un numero positivo "))
print("Es positivo")


#5 Menú interactivo:
#Crea un menú con while que permita al usuario elegir entre opciones (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y solo termine cuando elija la opción de salir.

print("Hola, ¿Como estas?")
print("\nQue deseas hacer? " 
        "\n1. Saludar"                      
        "\n2. Despedirse"                      
        "\n3. Salir")

deseo = int(input("\nPon el número de lo que quieres hacer "))
while deseo:
    if deseo == 1:
        print("Hola, ¿Como te encuentras el dia de hoy? ")
        deseo = int(input("Pon el número de lo que quieres hacer "))
    elif deseo == 2:
        print("Bye, see you later")
        deseo = int(input("Pon el número de lo que quieres hacer "))
    elif deseo == 3:
        print("Vuelve pronto")
        break


#6 Adivina el número:
#Genera un número secreto (puedes usar una variable fija) y usa un while para pedirle al usuario que lo adivine. Da pistas si el número es mayor o menor.

secreto = 43
numero = int(input("Adivina el número secreto "))
while secreto:
    if numero == secreto:
        print(f"Adivinaste el número, tu numero fue {numero} y el secreto era {secreto}")
        break
    elif numero < secreto:
        print("Tu numero es menor")
        numero = int(input("Adivina el número secreto "))
    elif numero > secreto:
        print("Tu número es mayor")
        numero = int(input("Adivina el número secreto "))


#7 Contar vocales en una palabra:
#Pide al usuario una palabra y usa un while para contar cuántas vocales tiene.

palabra = str(input("Escribe una palabra: "))

while
    

#8 Validar contraseña:
#Pide al usuario una contraseña y usa un while para seguir pidiendo hasta que ingrese "python123".

contraseña = "python123"
buscar = str(input("Pon una contraseña "))

while True:
    if buscar != contraseña:   
        print("Incorrecto")
        buscar = str(input("Ingresa nuevamente la contraseña "))
    else:
        print("Bienvenido")
        break


#9 Sumar hasta detenerse:
#Pide números al usuario y súmalos hasta que ingrese "0", momento en el que se imprimirá el total.

numero = 0
pedir = int(input("Pon un numero "))

while True:
    if pedir == 0:
        numero += pedir
        print("Este es el resultado ", numero)
        break
    elif pedir != numero:
        numero += pedir
        pedir = int(input("Pon un numero(0 para terminar) "))
    else:
        pass
"""

#10 Número de intentos:
#Pide al usuario que ingrese un número entre 1 y 10. Si no lo hace, sigue pidiéndolo hasta que lo haga correctamente.


numero = int(input("Pon un número: "))

while numero:
        if numero >0 and numero < 11:
            print("Tu número es correcto")
            break
        elif numero >10:
              print("Sigue intentado")
              numero = int(input("Pon un número: "))
        else:
              pass
