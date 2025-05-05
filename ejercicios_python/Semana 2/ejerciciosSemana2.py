"""
#1 Sistema de recomendaciones de películas 🎬
#Crea un programa que recomiende una película basada en la edad del usuario y sus preferencias (acción, comedia, terror, etc.).
#Si el usuario es menor de 13 años, evita películas con clasificación para adultos.

edad = int(input("¿Cual es tu edad? "))
pelicula = str(input("¿Qué tipo de peliculas de gusta (acción, comedia, terror, otra)? "))

match pelicula:
    case "acción":
        if edad <=13:
            print("Te gustara Bebes en pijama")
        else:
            print("Te gustara El caballero oscuro")
    case "comedia":
        if edad <=13:
            print("Te gustara Buscando a nemo")
        else:
            print("Te gustara Oh Ramona!")
    case "terror":
        if edad <=13:
            print("Te gustara Monster house")
        else:
            print("Te gustara El conjuro")
    case "otra":
        print("Genial te sales de los estandares")


#2 Asistente de productividad ⏳
#Diseña un asistente que, según la hora actual y si es un día laboral o fin de semana, sugiera actividades como:
#"trabajar"
#"descansar"
#"hacer ejercicio"
#Asegúrate de que los datos sean flexibles para futuras mejoras.

hora = int(input("Que hora es(Escribelo en la zona horaria de 24 horas)? "))
semana = str(input("Estas en dia laboral o estas en fin de semana(L/F) "))

match semana:
    case "l":
        if hora >=6 and hora <14:
            print("Tomate un break")
        elif hora >16 and hora <20:
            print("Haz un poco de ejercicio")
    case "f":
        if hora >5 and hora <=12:
            print("Haz ejercicio")
        elif hora >12 and hora <20:
            print("Tomate un break")
        else:
            print("Descansa")


#3 Control de acceso con doble autenticación 🔐
#Crea un sistema de inicio de sesión que solicite usuario y contraseña.
#Si la contraseña es correcta, debe solicitar un código de verificación (simulado).
#El acceso solo se concede si ambas verificaciones son correctas.


nameUsuario = str(input("Pon tu usuario: "))
usuario = "BenitoCamelo"
contraseñaUsuario = str(input("Ingrese la contraseña: "))
contraseña = "Schewinstaiger"

if usuario == nameUsuario and contraseña == contraseñaUsuario:
    print("Estas a un paso de acceder")
    solicitar = int(input("Pon el número de verificacion el cual te mandamos a tu correo: "))
    if solicitar == solicitar:
        print("Bienvenido")
else:
    print("Vos quien sos, largate de aqui")
"""

#4 Calculadora de presupuesto mensual 💰
#Desarrolla un programa que pida ingresos y gastos fijos del usuario.
#Luego, evalúa si puede ahorrar dinero y cuánto, o si necesita reducir gastos.
#Aplica buenas prácticas como modularidad y validaciones.

ingresos = int(input("Pon tus ingresos mensuales: "))
gastos = int(input("Pon la cantidad que te gastas: "))


#5 Asistente de clima y vestimenta 🌦️
#Crea un programa que pida la temperatura y si está lloviendo o no.
#Según los datos, sugiere qué ropa usar: abrigo, paraguas, ropa ligera, etc.
#Hazlo reutilizable para futuras ampliaciones.

#6 Sistema de registro de eventos con validación 🎟️
#Construye un programa que permita registrar asistentes a un evento.
#El sistema debe verificar que:
#La edad del usuario sea adecuada
#No se haya superado el límite de cupos disponibles

#7 Detector de spam en correos electrónicos 📧
#Simula un sistema que detecte si un mensaje es spam.
#Usa condiciones para verificar si el mensaje contiene palabras como:
#"gratis",
#"gana dinero",
#"descuento exclusivo", etc.
#Si hay coincidencias, márcalo como spam.

#8 Sistema de préstamos de biblioteca 📚
#Desarrolla un programa que permita a un usuario solicitar un libro.
#Solo puede hacerlo si:
#Tiene menos de 3 libros prestados
#No tiene sanciones pendientes

#9 Asistente de compras inteligentes 🛍️
#Crea un sistema que ayude al usuario a decidir si comprar un producto.
#Pide:
#Precio del producto
#Si hay descuentos
#Presupuesto del usuario
#Luego indica si la compra es recomendable o no.

#10 Evaluador de contraseñas seguras 🔑
#Diseña un programa que verifique si una contraseña es segura.
#Debe cumplir con:
#Al menos 8 caracteres
#Incluir números y letras
#No contener espacios
#Dale retroalimentación al usuario sobre cómo mejorar su contraseña.
