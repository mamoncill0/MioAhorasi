"""
#1 ¿Cómo accedemos a los elementos de una lista?
#¿Cómo se accede al primer elemento de una lista?
#¿Qué significa usar un índice negativo?
#¿Qué pasa si intento acceder a un índice que no existe?
#Ejemplo práctico:
#Crea una lista [10, 20, 30, 40] y muestra el primer y el último elemento.

miLista = [10,20,30,40]
extraer = (miLista[0], miLista[3])
print(extraer)


#2 ¿Qué es el "slicing" o rebanado de listas?
#¿Qué significa "slicing" en listas?
#¿Cómo se obtiene una sublista usando slicing?
#¿Qué significa dejar vacío el inicio o el final en el slicing?
#Ejemplo práctico:
#A partir de [10, 20, 30, 40, 50], obtén:
#Los elementos del índice 1 al 3.
#Los primeros 3 elementos.
#Los elementos desde el índice 2 hasta el final.

miLista = [10,20,30,40,50]
print(miLista[1:3])
print(miLista[0:3])
print(miLista[2:])


#3 ¿Cómo modificamos los elementos de una lista?
#¿Cómo se cambia el valor de un elemento de la lista?
#¿Qué pasa si modificamos un índice que no existe?
#Ejemplo práctico:
#Cambia el tercer elemento de [10, 20, 30, 40] por 99.

miLista = [10,20,30,40]
miLista[2] = 99
print(miLista)


#4 ¿Cómo agregamos nuevos elementos a una lista?
#¿Cómo se agrega un elemento al final de la lista?
#¿Cómo se inserta un elemento en una posición específica?
#¿Cómo se combinan dos listas en una sola?
#Ejemplo práctico:
#A una lista [10, 20, 30] agrega:
#El número 40 al final.
#El número 15 en la posición 1.
#Los números 50 y 60 al final de la lista.

#Mio
sub = [1,2,3,4]
miLista = [10,20,30]
miLista += [40]
miLista[1] = 15
miLista += 50,60 
print(miLista)

#Hecho por IA
# numeros inicial
numeros = [10, 20, 30]
# 1. Agregar 40 al final
numeros.append(40)  # [10, 20, 30, 40]
# 2. Insertar 15 en la posición 1 (segundo lugar)
numeros.insert(1, 15)  # [10, 15, 20, 30, 40]
# 3. Agregar 50 y 60 al final
numeros.extend(sub)  # [10, 15, 20, 30, 40, 50, 60]
# Resultado final
print(numeros)  # [10, 15, 20, 30, 40, 50, 60]


#5 ¿Cómo eliminamos elementos de una lista?
#¿Cómo se elimina un valor específico de una lista?
#¿Qué hace el método pop()?
#¿Cómo se elimina un elemento usando del?
#Ejemplo práctico:
#De la lista [10, 20, 30, 40, 50], realiza las siguientes acciones:
#Elimina el número 30.
#Elimina el último elemento.
#Elimina el segundo elemento (índice 1).

miLista = [10,20,30,40,50]
miLista.remove(30)
miLista.pop()
del miLista[1]
print(miLista)


#6 ¿Cómo buscamos elementos dentro de una lista?
#¿Cómo se verifica si un elemento está presente en una lista?
#¿Cómo encontrar el índice de un elemento?
#¿Cómo contar cuántas veces aparece un valor en la lista?
#Ejemplo práctico:
#Con la lista [10, 20, 30, 40, 50]:
#Verifica si el número 20 está en la lista.
#Encuentra el índice del número 30.
#Cuenta cuántas veces aparece el número 20.

lista = [10,20,30,40,50]
if 20 in lista:
    print("El numero esta en la lista")
else:
    pass
print("El indice en el cual se encuentra tu numero es: ", lista.index(30))
print("Las veces que aparece el indice son ", lista.count(20))


#7 ¿Cómo ordenamos los elementos de una lista?
#¿Cómo se ordena una lista de manera ascendente?
#¿Cómo se ordena en orden descendente?   
#¿Qué diferencia hay entre sort() y sorted()?
#Ejemplo práctico:
#Ordena la lista [40, 10, 30, 20]:
#Primero en orden ascendente.
#Luego en orden descendente.
#Crea una nueva lista ordenada sin modificar la original.

lista = [40,10,30,20]
lista.sort()
print(lista)
print(lista[::-1])


#8 ¿Cómo invertimos el orden de los elementos de una lista?

    ¿Cómo invertir una lista usando reverse()?
    ¿Cómo invertir una lista usando slicing?

Ejemplo práctico:

    Invierte el orden de [10, 20, 30, 40] utilizando ambas técnicas.


#9 ¿Cómo invertimos el orden de los elementos de una lista?
#¿Cómo invertir una lista usando reverse()?
#¿Cómo invertir una lista usando slicing?
#Ejemplo práctico:
#Invierte el orden de [10, 20, 30, 40] utilizando ambas técnicas.

#.reverse
lista = [10, 20, 30, 40]  
lista.reverse()  
print(lista)  
#slicing
lista.sort()
print(lista[::-1])


#10 ¿Cómo hacemos una copia de una lista?
#¿Cómo copiar una lista usando slicing?
#¿Cómo copiarla usando list()?
#¿Cómo copiarla usando copy()?
#Ejemplo práctico:
#Copia la lista [10, 20, 30] de tres maneras diferentes.

#(Slicing)
lista = [10, 20, 30]  
copia = lista[:]
copia[0] = 19 
print(lista)  
#(List)
lista = [10,20,30]
copia = list(lista)
copia[-1] = 29
print(lista)
#(Copy)
lista = [10,20,30]
copia = lista.copy()
copia[1] = 39
print(lista)


#11 ¿Cómo comprobamos si una lista está vacía?
#¿Cómo podemos saber si una lista no tiene elementos?
#Ejemplo práctico:
#Crea una lista vacía y escribe un código que imprima "La lista está vacía" si no contiene datos.

#Mio
lista = []
if not lista:
    print("La lista esta vacia")
else:
    print("La lista tiene elementos")

#Hecho por IA
lista = []  
if not lista:  
    print("La lista está vacía")  # Este bloque se ejecuta[^1^][3][6]  
else:  
    print("La lista tiene elementos")  
#Segunda opcion
lista = [10, 20]  
if len(lista) == 0:  
    print("Vacía")  
else:  
    print("No vacía")  # Este bloque se ejecuta[^1^][3][6]  
#Tercer opcion
lista = ["a", "b"]  
if lista == []:  
    print("Vacía")  
else:  
    print("No vacía")  # Este bloque se ejecuta[^1^][3][6]  


#12 ¿Cómo pedir varios datos al usuario y almacenarlos en una lista?
#¿Cómo pedimos al usuario la cantidad de datos que quiere ingresar?
#¿Cómo almacenamos esos datos en una lista usando un ciclo for?
#Ejemplo práctico:
#Escribe un programa que:
#Pregunte al usuario cuántos elementos quiere ingresar.
#Luego pida esos elementos uno por uno.
#Finalmente, muestre la lista completa.

lista = []
numero = int(input("Pon un numero de repeticiones: "))
for i in range(numero):
    valor = int(input(f"Ingrese el dato {i+1}"))
    lista.append(valor)
    lista.sort()
    print(lista)
"""

