"""
#1 DEF
def saludar(nombre):
    print(f"Hola {nombre}, ¿Como estas? ")
saludar(nombre=str(input("Pon tu nombre: ")))


#2
def sumar(num1,num2):
    return num1+num2

num1 = int(input("Pon un numero: "))
num2 = int(input("Pon un numero bro: "))
print(sumar(num1,num2))


#3
def doble(x):
    return x * 2

x = int(input("Pon un número que quieres el doble: "))
print(doble(x))


#4
mano = "Hermano"

def palabra():
    print(mano)
palabra()


#5 DA ERROR, PORQUE NO ESTA DEFINIDA AFUERA, COSA QUE SI TIENE EL ANTERIOR EJERCICIO
def saludo():
    mensaje = "Hola"  # variable local
    print(mensaje)

saludo()        # Hola
print(mensaje) #Como no es una variable global da error
# print(mensaje)  # ❌ Error: mensaje no está definida fuera de la función


#6
def aumentar():
    global contador
    contador += 1

contador = int(input("Pon un numero: "))
aumentar()
print(contador)


#7
contador = int(input("Pon un numero: "))

def aumentar(numero):
    numero += int(input("Pon un numero a agregar: "))
    return numero

print(aumentar(contador))
print(contador)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#1 DICCIONARIOS

#Varios Diccionarios
midiccionario=[
    {"Nombre": "Maik", "Edad": 18, "Profesion": "Estudiante"},
    {"Nombre": "Michelle", "Edad": 19, "Profesion": "Modelo"},
    {"Nombre": "Luis", "Edad": 17, "Profesion": "Vendedor"}
]

midiccionario[0]["Edad"] = int(input("¿Cual es tu edad? "))
midiccionario[1]["Profesion"] = str(input("¿Cual es tu profesion? "))

#Agregar diccionarios a diccionarios (Listas)

newdiccionario = {"Nombre": "Sari", "Edad": 23, "Profesion": "Heladera"}
midiccionario.append(newdiccionario)

for valor in midiccionario:
    print(valor["Nombre"], "Tiene", valor["Edad"], "Años", "Profesion", valor["Profesion"])


personas = {"Nombre": "Elizabeth", 
            "Edad": 26,
            "Ciudad": "Cundinamarca"}

#Agregamos nuevos Elementos o Cambiamos edades

personas["Edad"] = int(input("Agrega la edad: "))
personas["Profesion"] = str(input("¿Cual es tu profesion? "))

#for clave in personas:         #Solo muestra las claves (osea Nombre, edad, ciudad, profesion. No muestra el valor de la clave)
#    print(clave)


for valor in personas.values():
    print(personas)

#Ejemplo completo de como se pediria los valores con FOR

for clave, valor in personas.items():
    print(f"{clave} --> {valor}")

##########print(personas.keys())   Obtener solo claves
##########print(personas.values())  Obtener solo valores
##########print(personas.items())   Divide la lista en pares (Osea Nombre con su respectivo nombre , edad con su respectiva edad)

#Estas funciones son para borrar

del personas["Ciudad"]
personas.pop("Edad")
#########personas.clear() Elimina todo lo que esta dentro del diccionario "personas"

if "Nombre" in personas:
    print("Existe la clave 'Nombre'")

print(personas["Nombre"])
print(personas.get("Edad", "No existe"))
print(personas.get("Correo", "No existe"))
print(personas.get("Ciudad", "No existe"))
print(personas.get("Profesion", "No existe"))


productos = [
    {"nombre": "Laptop", "precio": 1200, "tienda": "Samsung"},
    {"nombre": "Mouse", "precio": 25, "tienda": "Huawei"},
    {"nombre": "Teclado", "precio": 45, "tienda": "Compumax"}
]

#productos.pop(2)    #Quita el diccionario 3
#del productos[0]    #Quita el primer diccionario
#print(productos)

for p in productos:
    print(f"{p['nombre']} cuesta ${p['precio']}")   #Creo que no necesita explicacion

for p in productos:
    p["precio"] *= 1.10 #Aumenta el precio en 10%
    
print("\nPrecios actualizados:")
for p in productos:
    print(f"{p['nombre']} ahora cuesta ${p['precio']:.2f}")     #Precios actualizados y con :.2f recondea a los primeros dos numeros decimales


#Buscar dentro de la lista

usuarios = [{"nombre": "Michael"}, 
            {"nombre": "Ana"}, 
            {"nombre": "Alexa"}
]

for usuario in usuarios:
    if usuario["nombre"] == "Ana":
        print("Usuario encontrado:", usuario)
"""