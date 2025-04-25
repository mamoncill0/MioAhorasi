print("\n¿Eres para mí?")
puntaje = 0
pregunta1 = str(input("Eres aseada: "))
if pregunta1 == "Si".lower():
    puntaje = puntaje + 60
    print("\nEso me gusta")
    pregunta2 = str(input("Te gusta el reggaeton: "))
else:
    puntaje = puntaje - 50
    print("\nQue asco")
    pregunta2 = str(input("Te gusta el reggaeton: "))
if pregunta2 == "si".lower():
    puntaje = puntaje -15
    print("\nGustos de mrd")
    pregunta3 = str(input("Te gusta perrear "))
elif pregunta2 == "no".lower():
    puntaje = puntaje + 26
    print("\nEso me gusta")
    pregunta3 = str(input("Te gusta perrear "))
if pregunta3 == "Si".lower():
    puntaje = puntaje - 20
    print("\nEso no me gusta socia")
    pregunta4 = str(input("¿Te gusta el anime? "))
elif pregunta3 == "No".lower():
    puntaje = puntaje + 28
    print("\nMe gustan princesas como tú")
    pregunta4 = str(input("¿Te gusta el anime? "))
if pregunta4 == "Si".lower():
    puntaje = puntaje - 20
    print("\nNo me gustan las onichan")
    pregunta5 = str(input("¿Te gusta cocinar? "))
elif pregunta4 == "No".lower():
    puntaje = puntaje + 25
    print("\nCada vez me atraes más")
    pregunta5 = str(input("¿Te gusta cocinar? "))
if pregunta5 == "Si".lower():
    puntaje = puntaje + 18
    print("\nOsea que tengo chef :D")
    pregunta6 = str(input("¿Eres educada con las personas que te rodean? "))
elif pregunta5 == "No".lower():
    puntaje = puntaje + 0
    print("\nNo hay problema")
    pregunta6 = str(input("¿Eres educada con las personas que te rodean? "))
if pregunta6 == "Si".lower():
    puntaje = puntaje + 44
    print("Eso me encanta")
else:
    print("Que mal")
    puntaje = puntaje - 30
print(puntaje)
if puntaje >= 100:
    print("\nEres la mujer de mi vida, te quiero conmigo siempre")
elif puntaje >= 85 and puntaje <= 99:
    print("\nEstoy enamorado de ti, pero hay cosas que puedes mejorar")
elif puntaje >= 73 and puntaje <= 84:
    print("\nTe falta mucho por mejorar, pero lo podriamos intentar")
else:
    puntaje < 73
    print("\nLo siento, pero no eres mi tipo")

