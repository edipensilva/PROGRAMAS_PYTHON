#print ("Hola Mundo2!!!")
#print ("Hola Edipes2!!!")

#edad = 40
#nombre = 'EDIPES'
#precio = 25
#estado = True
#cant = 2

#nombre = input('Ingrese el nombre del producto: ')
#precio = int(input('Ingrese el precio: '))
#cant = int(input('Ingrese la cantidad: '))
#tot = precio * cant

#print('El total a pagar por el producto1 ', nombre, 'es',tot)

#print('El total a pagar por el producto2 ', nombre, 'es ' + str(tot))

"=========================================================="

#print(type(edad))   # int
#print(type(nombre)) # str 
#print(type(precio)) # int
#print(type(estado)) # bool
#print(type(cant))   # int


#import keyword

#print(keyword.kwlist)

#print(keyword.iskeyword('continue'))

"=========================================================="

#mensaje = 'Hola Edipes'
#cadena = mensaje.find('Edipes')
#print('Cadena: ',cadena)

"=========================================================="

'''nombre = input("¿Cual es tu nombre?: ")
print("Hola " + nombre + ",vamos a realizar una suma.")
num_uno = int(input("Por favor intoduzca el primer valor: "))
num_dos = int(input("Por favor intoduzca el segundo valor: "))
resultado = num_uno + num_dos
print(nombre + " el resultado de la suma es: ",resultado)
'''
"=========================================================="
'''
print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿Cúal es tu nombre?")

matematicas = float(input(nombre + "¿Cúal es tu calificación en matemáticas?: "))
quimica = float(input(nombre + "¿Cúal es tu calificación en quimica?: "))
biologia = float(input(nombre + "¿Cúal es tu calificación en biologia?: "))

promedio = (matematicas+quimica+biologia)/3

if promedio >= 6:
    print('Felicidades ' + nombre + '" Aprobaste" con un promedio de: ',round(promedio,2))
else:
    print('Lo sentimos ' + nombre + '" No Aprobaste" con un promedio de: ',round(promedio,2))

print("Fin.")
'''
"=========================================================="

'''
print("==========================================================")
print("CONVERTIDOR DE NUMERO A LETRAS")
print("==========================================================")
num_uno = int(input("¿Cúal es el número que deseas convertir?"))

if num_uno == 1:
    print("El número es 'Uno'")

elif num_uno == 2:
    print("El número es 'Dos'")

elif num_uno == 3:
    print("El número es 'Tres'")

elif num_uno == 4:
    print("El número es 'Cuatro'")

elif num_uno == 5:
    print("El número es 'Cinco'")

else:
    print("Este programa puede convertir solo hasta el número 5")
    
print("FIN.")

'''


'''
print("======================")
print("CONVERSOR")
print("======================\n")

print(" Menú de opciones: \n")
print("Presione 1 para convertir de número a palabra : ")
print("Presione 2 para convertir de palabra a número : \n")

opcion = int(input("¿Cúal es tu opción de deseada?: "))

if opcion == 1:
    print("\n Conversor de número a palabra.\n")
    opcion_uno = int(input("¿Cúal es el número que deseas convertir a palabra?: "))
    if opcion_uno == 1:
        print("El número es 'Uno'")
    elif opcion_uno == 2:
        print("El número es 'Dos'")
    elif opcion_uno == 3:
        print("El número es 'Tres'")
    elif opcion_uno == 4:
        print("El número es 'Cuatro'")
    elif opcion_uno == 5:
        print("El número es 'Cinco'")
    else:
        print("Este programa puede convertir solo hasta el número 5")

elif opcion == 2:
    print("\n Conversor de palabra a número.\n")
    opcion_dos = input("¿Cúal es la palabra que deseas convertir a número?: ")
    opcion_dos = opcion_dos.lower()
    if opcion_dos == "uno":
        print("El número es '1'")
    elif opcion_dos == "dos":
        print("El número es '2'")
    elif opcion_dos == "tres":
        print("El número es '3'")
    elif opcion_dos == "cuatro":
        print("El número es '4'")
    elif opcion_dos == "cinco":
        print("El número es '5'")
    else:
        print("El número seleccionado no esta registrado")
else:
    print("Opción no disponible.")
    
print("Fin.")
'''

'''
print("***************************************")
print("**concatenación f-strings**")
print("***************************************\n")

nombre = input("¿Cúal es tu nombre?: ")
num_uno = int(input("Introduce un número: "))
num_dos = int(input("Introduce un segundo número: "))
print(f"Hola {nombre} el resultado de {num_uno} + {num_dos} es: {num_uno+ num_dos}")
'''

#cadena = ' Hola Ernesto '
#print(cadena.strip("s tHo"))

'''
first_name = input("Nombre: ")
last_name = input("Apellido: ")
full_name = f"{first_name} {last_name}"

print(f"¿El formato del método istitle() se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el método title(): {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}")
'''

#string = "Hola mundo"
#print(string.count(""))
#rta = 11

'''
string = input("Introduce una frase: ")
palabra = input("Introduce la palabra que desea eliminar: ")
substring = ""
indice = string.find(palabra)
substring = string[0:indice]+string[indice + len(palabra) + 1: ]
print(f"Cadena resultante: {substring}")
'''

'''
print("\nModificando vocales[1] = 2")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[1] = 2
print(f"Lista vocales: {vocales}")

print("\nModificando vocales[-1] = 'x'")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[-1] = 'x'
print(f"Lista vocales: {vocales}")

print("\nModificando vocales[2:4] = ['x','y']")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[2:4] = ['x','y']
print(f"Lista vocales: {vocales}")

print("\nModificando vocales[1:3] = ['x','y','z']")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[1:3] = ['x','y','z']
print(f"Lista vocales: {vocales}")

print("\nModificando vocales[:2] = ['x','y','z']")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[:2] = ['x','y','z']
print(f"Lista vocales: {vocales}")

print("\nModificando vocales[0:3] = ['x','y']")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[0:3] = ['x','y']
print(f"Lista vocales: {vocales}")

print("\nModificando vocales[0:3] = 'x','y'")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[0:3] = 'x','y'
print(f"Lista vocales: {vocales}")


print("\nModificando vocales[:] = 'x'")
vocales = ["a","e","i","o","u"]
print(f"Lista vocales: {vocales}")
vocales[:] = 'x'
print(f"Lista vocales: {vocales}")
'''






        



      







