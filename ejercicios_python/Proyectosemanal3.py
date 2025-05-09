inventario = {}

def agregar():
    nombre = str(input("Ingresa el nombre del producto a agregar: ")).capitalize()
    price = float(input("Ingresa el precio del producto "))
    cant = int(input("¿Cual es la cantidad de productos? "))
    inventario[nombre]={"Producto": nombre, "Precio": price, "Cantidad": cant}
    print(f"Producto : {nombre}\n Precio : {price}\n Cantidad: {cant}")

def consultar():
    nombre = str(input("Ingresa el nombre del producto a consultar: ")).capitalize()
    if nombre in inventario:
        print(inventario[nombre])
    else:
        print("Ese producto no existe, agregalo")

def actualizar():
    nombre = str(input("Ingresa el nombre del producto a actualizar: ")).capitalize()
    if nombre in inventario:
        actuali = float(input("Nuevo precio: "))
        inventario[nombre]["Precio"] = actuali
        print("Precio actualizado con exito")
    else:
        print("Ese producto no esta disponible o no existe")

def eliminar():
    nombre = str(input("Ingresa el nombre del producto a eliminar: ")).capitalize()
    if nombre in inventario:
        del inventario[nombre]
    else:
        print("Ese elemento no existe, por cual no se puede eliminar")

def calcular():
    valor_total = sum(map(lambda producto: producto["Precio"] * producto["Cantidad"], inventario.values()))
    print(f"El valor total del inventario es: {valor_total}")

while True:

    print("""Elige una opcion
                         1. Añadir productos: 
                         2. Consultar productos: 
                         3. Actualizar precios: 
                         4. Eliminar productos: 
                         5. Calcular el valor total del inventario: 
                         6. Salir
                         --> """)

    opcion= input(" Escribe una de las opciones:  ")

    match opcion:
        case "1":
            agregar()
        case "2":
            consultar()
        case "3":
            actualizar()
        case "4":
            eliminar()
        case "5":
            calcular()
        case "6":
            print("Saliste con exito")
            break
        case _: 
            print("Eso no es correcto")


   
  