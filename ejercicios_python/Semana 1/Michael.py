print("\nBienvenidos a tiendas Micha")
productos = str(input("Elige un producto: "))
precio = float(input("Elige el precio: "))
cantidad = int(input("Elige la cantidad: "))
descuento = float(input("Cuanto descuento deseas hacer: "))
prom = descuento//100
resultado = precio*cantidad
descontado = resultado * (descuento/100)
total = resultado - descontado

if  0 <= precio <=100:
    print(f"Total: \nSin descuento: {resultado:.2f} \nCon descuento {total:.2f} \nTu compra fue: {productos}")
else:
    print("Te excediste")