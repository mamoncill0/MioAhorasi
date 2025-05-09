
#1

#🐾 Ejercicio: Gestión de Animales
#Desarrolla un programa en Python que permita gestionar información sobre animales. El programa debe tener un menú usando funciones con las siguientes opciones: ** recuerda que pasa nombre, edad y enfermo cada uno debe de guardarse en su propia lista
#1. Agregar un animal:
#El usuario debe ingresar el nombre, la edad y si el animal está enfermo o no (sí/no). Esta información debe ser almacenada en tres listas separadas: una para los nombres de los animales, otra para sus edades y otra para su estado de salud.
#2. Eliminar un animal por su nombre:
#El usuario debe poder ingresar el nombre del animal que desea eliminar. Si el animal está registrado, debe ser removido de las tres listas. Si el animal no está registrado, se debe mostrar un mensaje indicando que no se encontró.
#3. Listar todos los animales registrados:
#El programa debe mostrar una lista con todos los animales registrados, incluyendo su nombre, edad y estado de salud (enfermo/sano).
#4. Salir:
#El programa debe permitir al usuario salir del menú.

nombreAnimales = []
edadesAnimales = []
enfermoAnimales = []
def mirarLista():
       
            for i in range(len(edadesAnimales)):

                print(f"""
                  nombres: {nombreAnimales[i]}
                  edades: {edadesAnimales[i]}
                  esta enfermo? {enfermoAnimales[i]}""")

def eliminarMascota():
    nombreA = str(input("Nombre mascota: "))
    eliminar = nombreAnimales.index(nombreA)
    del nombreAnimales[eliminar]
    del edadesAnimales[eliminar]
    del enfermoAnimales[eliminar]
    print("Tu macota fue eliminada con exito")

def agregarMascota():
    nameA = str(input("Nombre mascota: "))
    yearA = input("Pon la edad de tu mascota: ")
    stickA = str(input("Tu mascota esta enferma (Si/No) "))
    nombreAnimales.append(nameA)
    edadesAnimales.append(yearA)
    enfermoAnimales.append(stickA)
    print("\nYa se agrego tu mascota chaval")

while True:
    opcion = int(input("""
          1. Agregar mascota
          2. Eliminar mascota
          3. Mirar lista
          4. Salir\n
          Elige una opcion --> """))
    if opcion == 1:
        agregarMascota()
    elif opcion == 2:
        eliminarMascota()
    elif opcion == 3:
        mirarLista()
    elif opcion == 4:
         print("See you later bro")
         break
    else:
         print("Escribe bien pendejo")



#2

#Ejercicio 1: Registro de Estudiantes
#Objetivo:
#Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.
#Instrucciones:
#Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario con las claves edad y calificacion.
#El programa debe permitir al usuario realizar las siguientes operaciones:
#Agregar un nuevo estudiante (nombre, edad, calificación).
#Modificar la calificación de un estudiante.
#Mostrar la información de todos los estudiantes.
#Eliminar un estudiante por su nombre.

estudiantes = {}

def name():
    nombre = str(input("Agrega al estudiante: ")).lower()
    aye = int(input("Agrega edad estudiante: "))
    calif = float(input("Agrega la calificacion del estudiante: "))
    estudiantes[nombre]={"edad": aye, "calificacion": calif}
    print("El estudiante fue agregado con esito")

def modificar():
    nombre = input("Nombre del estudiante: ").lower()
    if nombre in estudiantes:
        nuevaCal = float(input("Nueva calificación: "))
        estudiantes[nombre]["calificacion"] = nuevaCal
        print("Calificación actualizada a la actualidad")
    else:
        print("Ese estudiante no existe carnalito")

def mostrar():
    if estudiantes: 
        print("Lista de estudiantes: ")
        for nombre, info in estudiantes.items():
            print(f"nombre: {nombre}, edad: {info['edad']}, calificacion: {info['calificacion']}")

def calificacion():
    for nombre, nota in estudiantes.items():
        print(f"{nombre} : {nota['calificacion']}")

def year():
    for nombre, age in estudiantes.items():
        print(f"{nombre}: {age['edad']}")

while True:
    opcion = int(input("""
                       1. Agregar estudiante
                       2. Modificar datos
                       3. Mostrar datos
                       4. Calificaciones estudiantes
                       5. Edades estudiantes
                       6. Salir\n
                       Elije una opcion bro -->\n"""))
    if opcion == 1:
        name()
    elif opcion == 2:
        modificar()
    elif opcion == 3:
        mostrar()
    elif opcion == 4:
        calificacion()
    elif opcion == 5:
        year()
    elif opcion == 6:
        print("Bye-bye baiby")
        break
'''



#3

#Ejercicio: Gestión de Contactos
#Objetivo:
#Crear un diccionario para gestionar los contactos, donde la clave sea el nombre del contacto y el valor sea su número de teléfono. El programa permitirá agregar nuevos contactos.
#Instrucciones:
#Crea un diccionario llamado contactos donde cada clave sea el nombre de un contacto y su valor sea el número de teléfono.
#El programa debe permitir al usuario realizar las siguientes operaciones:
# Agregar un nuevo contacto (nombre, número de teléfono).
# Mostrar todos los contactos almacenados.
# Buscar un contacto por su nombre.

contactos = {"Michael": 3226103500}

def agregar():
    nombre = str(input("Ingresa un nuevo contacto: ")).capitalize()
    tel = int(input("Ingresa el numero de telefono: "))
    contactos[nombre]={"tel": tel}
    print("Contacto agregado con exzito")

def mostrar():
    print(contactos)

def buscar():
    busco = str(input("Busca por el nombre: ")).capitalize()
    if busco in contactos:
        print(f"{busco}: {contactos[busco]['tel']}")
    else:
        print("Contacto no encontrado.")

def eliminar():
    nombre = input("Nombre del contacto a eliminar: ").capitalize()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print("Ese contacto no existe.")

while True:
    aronou = int(input("""
                       1. Agregar contacto
                       2. Mostrar contactos
                       3. Buscar contactos
                       4. Eliminar contacto :(
                       5. Salir\n
                       Elige una opcion --> """))
    if aronou == 1:
        agregar()
    elif aronou == 2:
        mostrar()
    elif aronou == 3:
        buscar()
    elif aronou == 4:
        eliminar()
    elif aronou == 5:
        print("See you later bro")
        break
    else:
        print("Que elijas una opcion estupido")





#4

#📒 Mini-Proyecto: Agenda de Contactos
#📝 Descripción
#Crea una pequeña agenda que permita:
#Agregar un nuevo contacto (nombre y número de teléfono).
#Buscar un contacto por su nombre.
#Mostrar todos los contactos.
#Eliminar un contacto.
#📦 Requisitos
#Usar un diccionario donde el nombre sea la clave y el número sea el valor.
#Crear un pequeño menú en consola para elegir las acciones.

"Es la misma mierda que hice arriba"

contactos = {}

def agregar():
    nombre = str(input("Ingresa un nuevo contacto: ")).capitalize()
    tel = int(input("Ingresa el numero de telefono: "))
    contactos[nombre]={"tel": tel}
    print("Contacto agregado con exzito")

def mostrar():
    print(contactos)

def buscar():
    busco = str(input("Busca por el nombre: ")).capitalize()
    if busco in contactos:
        print(f"{busco}: {contactos[busco]['tel']}")
    else:
        print("Contacto no encontrado.")

def eliminar():
    nombre = input("Nombre del contacto a eliminar: ").capitalize()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print("Ese contacto no existe.")

while True:
    aronou = int(input("""
                       1. Agregar contacto
                       2. Mostrar contactos
                       3. Buscar contactos
                       4. Eliminar contacto :(
                       5. Salir\n
                       Elige una opcion --> """))
    if aronou == 1:
        agregar()
    elif aronou == 2:
        mostrar()
    elif aronou == 3:
        buscar()
    elif aronou == 4:
        eliminar()
    elif aronou == 5:
        print("See you later bro")
        break
    else:
        print("Que elijas una opcion estupido")
'''