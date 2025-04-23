"""
#1
numero = int(input("Pon un numero: "))
if numero %3 == 0 and numero %5 == 0:
    print("FizzBuzz")
elif numero %3 == 0:
    print("Fizz")
elif numero %5 == 0:
    print("Buzz")
else: 
    print(numero)
"""
#2 
print("\nBienvenidos a Club unicornio ninja")
edad = int(input("\nIngrese su edad: "))
pase = str(input("Tienes pase dorado? (Si/No)"))

if edad >= 18:
    if pase == "Si":
        print("Pasa rey")
    elif 18 <= edad <=25 and pase == "No":
        print("Pasa bombom")
    elif edad > 25 and pase == "No":
        print("Lo siento anciano")
else:
    print("Pa la casa Chinito")