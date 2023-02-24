numero_de_matrix = int(input("¿Cúantas matrices quieres sumar?: "))

if numero_de_matrix > 1:

    filas = int(input("¿Cuantas filas tendrá las matrices?: "))
    columnas = int(input("¿Cuantas columnas tendrá las matrices?: "))

    lista_matrix = []
    print("\n")
    
    #llenado de matrices
    for numero in range(numero_de_matrix):
        matrix = []
        for fila in range(filas):
            nueva_fila = []
            for columna in range(columnas):
                nueva_fila.append(
                    int(input(f"Introduce un elemento para la matriz {numero + 1} fila {fila} columna {columna}: ") ))
            matrix.append(nueva_fila)
        lista_matrix.append(matrix)    
        print()
        
    #sumar de matrices
    matrix = []
    for fila in range(filas):
        nueva_fila = []
        for columna in range(columnas):
            suma_matrix = 0
            for posicion_matrix in range(len(lista_matrix)):
                suma_matrix = suma_matrix + lista_matrix[posicion_matrix][fila][columna]
            nueva_fila.append(suma_matrix)
        matrix.append(nueva_fila)
    lista_matrix.append(matrix)

    # imprimir matrices
    for fila_matrix in range(filas):
        for lista_matrix_posicion in range(len(lista_matrix)):
            if fila_matrix != 1:
                    print(f"{lista_matrix[lista_matrix_posicion][fila_matrix]} ", end="  ")
            else:
                if lista_matrix_posicion < len(lista_matrix) - 2:
                    print(f"{lista_matrix[lista_matrix_posicion][fila_matrix]}", end=" + ")
                elif lista_matrix_posicion < len(lista_matrix) - 1:    
                    print(f"{lista_matrix[lista_matrix_posicion][fila_matrix]}", end=" = ")
                else:
                    print(f"{lista_matrix[lista_matrix_posicion][fila_matrix]}", end="   ")
        print()           
else:
    print("Se necesita dos o más matrices para realizar la suma.")
    
