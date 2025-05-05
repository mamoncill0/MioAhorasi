"""
#1 Contar del 1 al 10:
#Escribe un programa que use un for para imprimir los números del 1 al 10.

for i in range(1,11):
    print(i)


#2 Contar hacia atrás:
#Usa un for para imprimir los números del 10 al 1 en orden descendente.

for i in range(10,1,-1):
    print(i)


#3 Sumar los primeros 10 números:
#Usa un for para sumar los números del 1 al 10 e imprime el resultado.

suma = 0
for numero in range(1,11):
    suma += numero
    print(suma)


#4 Números pares del 1 al 20:
#Usa un for y condicionales para imprimir solo los números pares del 1 al 20.

for pares in range(2,21,2):
    print(pares)


#5 Detectar múltiplos de 3:
#Escribe un programa que use un for y condicionales para imprimir los números del 1 al 30 que sean múltiplos de 3.

for multiplo in range(3,31,3):
    print(multiplo)


#6 Contar letras "a":
#Pide al usuario una palabra y usa un for con un condicional para contar cuántas veces aparece la letra "a".

palabra = str(input("Escribe una palabra: "))
letra = 0

for x in palabra:
    if x == "a":
        letra += 1

print(f"La letra 'a' aparece {letra} veces.")


#7 Tabla de multiplicar del 5:
#Usa un for para imprimir la tabla de multiplicar del 5 (del 1 al 10).

for i in range(1, 11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")


#8 Números positivos en una lista:
#Dada una lista de números (por ejemplo, [3, -1, 5, -2, 7, -8]), usa un for y condicionales para imprimir solo los positivos.

lista = [3,-1,5,-2,7,-8]
for lista in lista:
    if lista > 0:
        print(lista)

        
#9 Mayúsculas y minúsculas:
#Pide al usuario una palabra y usa un for para contar cuántas letras son mayúsculas y cuántas son minúsculas.

palabra = input("Escribe una palabra: ")
mayusculas = 0
minusculas = 0

for letra in palabra:
    if letra.isupper():     #IS es para verificar si la letra es (En este caso mayuscula)
        mayusculas += 1
    elif letra.islower():
        minusculas += 1

print("Letras mayúsculas: ", mayusculas)
print("Letras minúsculas: ", minusculas)



#10 Simulación de contraseña:
#Pide al usuario que ingrese una contraseña e imprime "Acceso permitido" solo si la contraseña es "python123", usando un for para simular tres intentos.

contraseña = "python123"

for intentos in range(3):
    usContra = str(input("Ingrese la contraseña"))
    if contraseña == usContra:
        print("Acceso permitido")
        break
    else:
        print("sorri baibi bolale tu contlaseña")


#11 Invertir una lista:
#Dada una lista de números (por ejemplo, [1, 2, 3, 4, 5]), usa un for para invertir la lista sin usar funciones incorporadas.

numeros = [1, 2, 3, 4, 5]
invertida = []

for i in range(5):
    invertida.append(numeros[4 - i])
print(invertida)


#12 Eliminar los números negativos:
#Dada una lista de números (por ejemplo, [3, -1, 5, -2, 7]), usa un for para crear una nueva lista que contenga solo los números positivos.

numeros=[3,-1,5,-2,7]
positivos=[]

for i in numeros:
    if i >0:
        positivos.append(i)
print(positivos)      


#13 Encontrar la suma de los cuadrados:
#Dada una lista de números (por ejemplo, [1, 2, 3, 4]), usa un for para calcular la suma de los cuadrados de los números en la lista.

numeros = [1, 2, 3, 4]
suma_cuadrados = 0

for numero in numeros:
    cuadrado = numero ** 2
    print(f"El número es {numero} y su cuadrado es {cuadrado}")     #Hecho por IA ni idea de como se hacía esto
    suma_cuadrados += cuadrado

print("La suma de los cuadrados es:", suma_cuadrados)



#14 Duplicar los valores de una lista:
#Dada una lista de números, usa un for para crear una nueva lista donde cada número sea el doble del valor original.

numeros = [1, 2, 3, 4, 5]
dobles = []

for num in numeros:
    dobles.append(num * 2)

print("Lista original:", numeros)
print("Lista con números dobles:", dobles)


#15 Contar elementos específicos:
#Pide al usuario que ingrese un número y una lista. Usa un for para contar cuántas veces aparece el número ingresado en la lista.

numero = int(input("Ingresa el número que quieres buscar: "))

lista = []
print("Ingresa 7 números para la lista:")
for i in range(7):
    numeros = int(input("Número: "))
    lista.append(numeros)

contador = 0
for elemento in lista:
    if elemento == numero:
        contador += 1

print(f"El número {numero} aparece {contador} veces en la lista {lista}.")


#16 Eliminar duplicados de una lista:
#Dada una lista con elementos repetidos, usa un for para crear una nueva lista sin elementos duplicados.

lista = [1,2,2,3,4,4,5,5,6,7,8,8,9,10,11,11]
lista2 = []

for numero in lista:
    if numero not in lista2:
        lista2.append(numero)

print(lista2)


#17 Generar una lista de múltiplos de un número:
#Pide al usuario un número N y usa un for para crear una lista con los primeros 10 múltiplos de N.

numeros = int(input("Pon un número del cual desees su multiplo "))
multiplos = []

for i in range(1,11):
    multiplos.append(numeros * i)
    print(multiplos)

    
#18 Sumar los elementos en las posiciones pares:
#Dada una lista de números, usa un for para sumar los números que se encuentran en las posiciones pares (índices 0, 2, 4, etc.).

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
suma = 0

for i in range(1,len(numeros),2):
    suma += numeros[i]
    print(suma)


#19 Filtrar cadenas con más de 5 caracteres:
#Dada una lista de cadenas de texto, usa un for para crear una nueva lista con solo aquellas cadenas que tengan más de 5 caracteres.

cadenas = ["Hola", "Michael", "Pene", "Arroz", "Arepa", "Canabis", "Carton", "Agricola", "Especial"]
lista = []

for i in cadenas:
    if len(i) >5:
        lista.append(i)
        print(lista)


#20 Ordenar una lista de manera ascendente:
#Dada una lista de números, usa un for para ordenar la lista de menor a mayor sin utilizar las funciones sorted() o sort().

numeros = [1, 0, 2, 9, 3, 8, 4, 7, 5, 12, 48, 22, 24, 64, 11]
ordenado = []

for num in numeros:
    for i in range(len(ordenado)):
        if num < ordenado[i]:
            ordenado.insert(i, num)
            break
    else:
        ordenado.append(num)


print("Lista ordenada:", ordenado)


#21 Imprimir caracteres de una cadena:
#Pide al usuario una cadena y usa un for para imprimir cada carácter de la cadena en una línea separada.

cadena = str(input("Escribe lo que quieras: "))

for i in cadena:
    print(i)

    
#22 Sumar los números en una lista:
#Dada una lista de números (por ejemplo, [1, 2, 3, 4, 5]), usa un for para sumar todos los números e imprimir el resultado.

lista = [1, 2, 3, 4, 5]
suma = 0

for i in lista:
    suma += i
    print(suma)

#23 Números impares del 1 al 30:
#Usa un for y un condicional para imprimir solo los números impares del 1 al 30.

for x in range(1,31,3):
    print(x)

    
#24 Encontrar la letra más frecuente:
#Pide al usuario una palabra y usa un for para encontrar cuál es la letra que más veces se repite en la palabra.

palabra = input("Ingresa una palabra: ").lower()
letra_mas_repetida = ""
max_repeticiones = 0

for letra in set(palabra):  # Recorremos solo letras únicas(Para eso sirve la funcion SET)
    repeticiones = palabra.count(letra) #Cuenta cuantas veces aparece la misma letra(COUNT)
    if repeticiones > max_repeticiones:
        max_repeticiones = repeticiones
        letra_mas_repetida = letra

print(f"La letra que más se repite es '{letra_mas_repetida}' ({max_repeticiones} veces).")


#25 Verificar si un número es primo:
#Escribe un programa que pida un número y use un for para determinar si el número es primo (sin usar la función isprime()).

numero = int(input("Escribe un numero: "))

for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} NO es un número primo.")
        break
else:
    if numero < 2:
        print(f"{numero} NO es un número primo.")
    else:
        print(f"{numero} es un número primo.")


#26 Sumar números negativos:
#Dada una lista de números (por ejemplo, [4, -2, -6, 7, -3]), usa un for para sumar solo los números negativos e imprimir el resultado.

lista = [4, -2, -6, 7, -3]
suma = 0

for lista in lista:
    if lista <0:
        suma += lista
        print(suma)


#27 Contar palabras con más de 3 letras:
#Pide al usuario una oración y usa un for con un condicional para contar cuántas palabras tienen más de 3 letras.

palabra = input("Expresate brother: ")
contar = 0

for i in palabra.split():  #split() divide la oración en palabras pa que sepa
    if len(i) > 3:
        contar += 1

print("El número de palabras con más de 3 letras es:", contar)


#28 Imprimir los primeros N números:
#Pide al usuario un número N y usa un for para imprimir los primeros N números enteros.

numero = int(input("Pon un numero: "))
for i in range(numero):
    print(i)


#29 Número mayor en una lista:
#Dada una lista de números (por ejemplo, [10, 2, 30, 4]), usa un for para encontrar el número mayor.

numeros = [10, 2, 30, 4]
mayor = []

for numero in numeros:
    if not mayor:  # Si la lista 'mayor' está vacía
        mayor.append(numero)  # Agregamos el primer número
    elif numero > mayor[0]:  # Comparamos con el actual mayor
        mayor[0] = numero  # Actualizamos el mayor

print("El número mayor es:", mayor[0])
"""

#30 Divisores de un número:
#Pide al usuario un número y usa un for para imprimir todos sus divisores (excepto el número en sí).

numero = int(input("Pon un numero: "))

for i in range(1, numero):
    if numero % i == 0:
        print(i)