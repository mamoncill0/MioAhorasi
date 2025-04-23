"""
#1 Doble y triple  
#Pide un número entero y muestra el doble y el triple de ese número, separados por coma.

numero = int(input("Pon un número: "))
variable = numero+numero
variable2 = numero+numero+numero
print(numero, variable, variable2)


#2 Repetir palabra  
#Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces.

palabra = str(input("Pon palabra: "))
numero = int(input("Pon numero: "))
conjuncion = ' '.join([palabra] * numero) #Me ayuda la IA para poder separar las palabras
print(conjuncion)
#Segunda opcion Hecha completamente por la IA
palabra = input("Pon palabra: ")
numero = int(input("Pon numero: "))

for _ in range(numero):
    print(palabra)


#3 Mayor de edad (sin condicional)  
#Pide la edad del usuario y muestra si es mayor de 18 (solo usando comparación).

edad = int(input("Pon edad: "))  #Una MRD no sirve
mayor = edad >= 18 
menor = edad <= 17
comparacion = mayor == edad != menor == edad
print(comparacion)

#Siguiente con IA
edad = int(input("¿Cuántos años tienes? "))
es_mayor = edad >= 18
print("¿Eres mayor de edad?", es_mayor)


#4 Divisible por 5  
#Pide un número entero y muestra si es divisible entre 5 (usar `%` y `==`).

numero = int(input("Pon un numero: "))
divisible = (numero %5 == 0)
print(divisible)


#5  Intercambio de variables
#Pide dos valores al usuario e imprime los valores intercambiados.
#Ejemplo: Entrada → a = 3, b = 5 → Salida → a = 5, b = 3

a = 9
b = 12

a, b = b, a

print(a, b)


#6 Inverso de número de tres cifras
#Pide un número de tres cifras (ej. 123) y muestra sus cifras en orden inverso (321).
#Usa operaciones matemáticas para extraer centenas, decenas y unidades.

#Hecho por IA HPPPP no sé matematicas
numero = int(input("Pon un numero de tres cifras: "))
centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10
inverso = (unidades * 100) + (decenas * 10) + centenas
print("Numero inverso", inverso)


#7 Extraer hora, minuto y segundo de segundos totales
#Pide al usuario un número de segundos y muestra cuántas horas, minutos y segundos son.
#Ejemplo: 3665 segundos → 1 hora, 1 minuto, 5 segundos.

numero = int(input("pon un numero grande: "))
hora = numero // 3600
resto = numero % 3600
minutos = numero // 3600
segundos = resto % 60
print(f"\nHora: {hora} Minutos: {minutos} segundos: {segundos}")


#8 Fecha formateada
#Pide al usuario el día, mes y año por separado e imprime la fecha en formato: "DD/MM/AAAA" y también "AAAA-MM-DD"

dia = int(input("¿Que dia es? "))
mes = int(input("Pon el mes: "))
año = int(input("¿Que año es? "))

print(dia, "/",mes, "/", año)
print(año, "/", mes, "/", dia)


#9 Cálculo de propina y cuenta total
#Pide el costo de una comida y calcula el 10%, 15% y 20% de propina. Muestra el total a pagar en cada caso.

costoComida = float(input("Precio: "))
propina = int(input("Cuanta propina deseas dejar "))
propina2 = costoComida * (propina/100)
total = round(costoComida + propina2)

print("El total de tu compra y la propina seria: ", total)
"""

#10 Conversor de minutos a días y horas
#Pide una cantidad de minutos y muestra a cuántos días, horas y minutos equivale.

minutos = int(input("Pon un numero grande perrito: "))