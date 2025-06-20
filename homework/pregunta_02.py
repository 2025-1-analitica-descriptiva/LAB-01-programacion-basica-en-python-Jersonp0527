"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    letters_count = {}    
    with open('./files/input/data.csv', 'r') as file:
        for line in file:
            data = line.split()
            letter = data[0]
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
    letters_count = sorted(letters_count.items(), key=lambda x: x[0])
    return letters_count