filas = int(input("¿Cuantas filas tendra la matrix?: "))
columnas = int(input("¿Cuantas columnas tendra la matrix?: "))

matrix = []

for filas_posicion in range(filas):
    filita = []
    for elemento in range(columnas):
        filita.append(int(input(f"Introduce un elemento a la fila {filas_posicion}: ")))
    matrix.append(filita)

for row in matrix:
    print(row)
    
        
