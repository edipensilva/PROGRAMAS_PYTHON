numeros =[]
longitud_lista = int(input("¿Cúantos números enteros contendra la lista?: "))

for _ in range(longitud_lista):
    numeros.append(int(input("Introduzca un número entero: ")))

print(f"\nLista: {numeros} \nLa suma total de los elementos es: {sum(numeros)} ")
