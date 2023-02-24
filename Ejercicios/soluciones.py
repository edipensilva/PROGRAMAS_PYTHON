#1.definir una función max()   que tome como argumento dos numeros y devueva el mayor de ellos.

def custom_max(n1: int, n2: int):
    """ Dado dos números de entrada retorna el máximo de ambos
    Args:
        n1 (int): Primer número a comparar
        n2 (int): Segundo número a comparar
    Returns:
        int : mayor de ambos
    """

    if n2 > n1:
        return n2
    elif n1 > n2 :
        return n1
    elif n1 == n2:
        raise Exception('Los Valores no pueden ser iguales')   
    else:
        raise Exception('Algo salio mal')   

#print(custom_max(1,2))


def max_de_tres(n1: int, n2: int, n3: int):
    """ Dado tres números de entrada retorna el máximo de ambos
    Args:
        n1 (int): Primer número a comparar
        n2 (int): Segundo número a comparar
        n3 (int): tercer numero a comparar
    Returns:
        int : mayor de los tres numeros
    """
    n =  custom_max(n1, n2)
    n_final = custom_max(n3, n)

    return n_final

print(max_de_tres(10,2,3))

