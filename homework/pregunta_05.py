"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    letters_count = {}    
    with open('./files/input/data.csv', 'r') as file:
        for line in file:
            data = line.split()
            letter = data[0]
            value = int(data[1])            
            if letter in letters_count:
                letters_count[letter][0] = max(letters_count[letter][0], value)
                letters_count[letter][1] = min(letters_count[letter][1], value)
            else:
                letters_count[letter] = [value, value]
    letters_count = [(letter, max_val, min_val) for letter, (max_val, min_val) in letters_count.items()]
    letters_count = sorted(letters_count, key=lambda x: x[0])
    return letters_count    