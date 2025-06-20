"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    letters_count = {}    
    with open('./files/input/data.csv', 'r') as file:
        for line in file:
            data = line.split()
            letter = data[0]
            value = int(data[1])            
            if letter in letters_count:
                letters_count[letter] += value
            else:
                letters_count[letter] = value
    letters_count = sorted(letters_count.items(), key=lambda x: x[0])
    return letters_count

