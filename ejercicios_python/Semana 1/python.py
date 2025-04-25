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
conjuncion = palabra * numero
print(conjuncion)
#conjuncion = ' '.join([palabra] * numero) #Para separar las palabras


#3 Mayor de edad (sin condicional)  
#Pide la edad del usuario y muestra si es mayor de 18 (solo usando comparación).

edad = int(input("Pon tu edad para saber si eres mayor: "))
mayor = edad >= 18 
print(mayor)


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


#No lo hice yo :(
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


#10 Conversor de minutos a días y horas
#Pide una cantidad de minutos y muestra a cuántos días, horas y minutos equivale.


numero = int(input("Pon un numero grande perrito: "))
dias = numero / 1440
hora = numero // 3600
minutos = numero // 3600

print(f"Dias: {round(dias)} \nHora: {hora} \nMinutos: {minutos}")


#11 Calculadora de promedio con validación
#Pide al usuario 3 notas (entre 0 y 10).  
#- Si alguna nota está fuera del rango, muestra un mensaje de error.  
#- Si todas son válidas, calcula el promedio y muestra si el estudiante **aprueba** (≥ 6) o **reprueba**.
#print("arroz)

nota1 = float(input("Pon tu nota perrito "))
nota2 = float(input("Pon la segunda atolandrado "))
nota3 = float(input("La que falta estupido "))
sumatoria = (nota1+nota2+nota3)/3

if sumatoria >=6:
    print("Aprobado rey", "Tu nota es: ", sumatoria)
elif sumatoria <=5:
    print("Arroz", "Pesima nota", sumatoria)
else:
    print("Tu nota es invalida como tu padre")


#12 Años para jubilarse

#Pide la edad y el género del usuario (`"M"` para mujer, `"H"` para hombre).  
#- Mujer se jubila a los **60 años**  
#- Hombre se jubila a los **65 años**
#**Si ya se puede jubilar**, muestra un mensaje celebratorio.  
#**Si no**, indica cuántos años faltan para la jubilación.

edad = int(input("Pon tu edad: "))
genero = str(input("Pon tu genero (M/H): "))
comparacion = 65 - edad
comparacionMujer = 60 - edad
if edad >= 65 and genero == "H".lower():
    print("Ya te puedes jubilar ancianito")
elif edad < 65 and genero == "H".lower():
    print("Aun te falta viejo", comparacion)
elif edad >= 60 and genero == "M".lower():
    print("Aqui esta tu jubilacion sugar")
elif edad < 60 and genero == "M".lower():
    print("Aun te falta babe", comparacionMujer)
else:
    print("Hubo un error horroroso")


#13 Calculadora de salario neto
#Pide:
#- Sueldo bruto
#- Porcentaje de descuento (por ejemplo: `13`)
#Calcula el sueldo neto usando la fórmula:
#> sueldo_neto = sueldo_bruto - (sueldo_bruto * descuento / 100)
#Ejemplo de salida:
#> Sueldo bruto: 1000 Descuento: 13 Sueldo neto: 870.0

sueldoBruto = float(input("Pon tu salario bruto: "))
descuento = float(input("¿Cuanto es el descuento? "))
sueldoNeto = sueldoBruto - (sueldoBruto * descuento / 100)
print(f"\nSueldo bruto: {sueldoBruto} \nDescuento: {descuento} \nSueldo neto: {sueldoNeto}")
"""

#14 ¿Compatibles?
#Pide:
#- Nombre y edad de dos personas
#Verifica si:
#- Ambos tienen **al menos 18 años**
#- **Se llaman distinto**
#- La **diferencia de edad no supera los 10 años**
#Si cumplen todo, imprime un mensaje gracioso diciendo que **son compatibles** 💞  
#Si no, di por qué **no lo son**.

nombre = str(input("Cual es tu nombre(H)? "))
nombre1 = str(input("Cual es tu nombre(M)? "))
edad = int(input("Edad: "))
edad2 = int(input("edad: "))
comparacion = edad and edad2 >=18
resta = edad - edad2

if nombre != nombre1:
    comparacion >= 18
    print(f"Son compatibles \nEdades: {edad, edad2} \nNombres: {nombre, nombre1}")
elif nombre != nombre1:
    comparacion < 18
    print(f"Lo siento pero sus edades no son comparibles {edad,edad2}")
elif nombre == nombre1:
    comparacion >= 18
    print(f"Lo siento no son compatibles, debido a que se llaman igual {nombre, nombre1}")
elif resta <= 10:
        print("Tienen diez años de diferencia no son compatibles")
else:
    print("Hubo un error garrafal")