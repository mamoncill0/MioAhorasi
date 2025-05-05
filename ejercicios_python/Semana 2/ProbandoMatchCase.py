"""
#1 MATCH/CASE
opcion = input("Elige una fruta (piña, arandano, naranja): ")

match opcion:
    case "piña":
        print("Elegiste piña")
    case "arandano":
        print("Elegiste arandano")
    case "naranja":
        print("Elegiste naranja")
    case _:
        print(f"Fruta no reconocida {opcion} no esta en las opciones")

#2 While
contador = 0
while contador <=5:
    print("Número: ", contador)
    contador += 1

#3 (1) For
nombre = "Michael"
for letras in nombre:
    print("Hola", letras)
#(2)
for i in range(1,6):
    print(i)
#(3)
for i in range(2,21,2):
    print(i)
#(4)
for i in range(5):
    print(i)
#(5)
for i in range(5):
    if i == 3:
        break  # se detiene al llegar a 3
    print(i)
"""