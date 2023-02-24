def ordenar(lista):
    if len(lista)<=1:
        return lista

    pivote = lista[0]
    izquierda = []
    derecha = []

    for i in range(1,len(lista)):
        if lista[i] < pivote:
            izquierda.append(lista[i])
        else:
            derecha.append(lista[i])

    return ordenar(izquierda) + [pivote] + ordenar(derecha)

numeros = [23,45,16,37,3,99,22]
listaordenada = ordenar(numeros)
print(listaordenada)


            
