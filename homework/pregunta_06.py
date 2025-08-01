"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    letters_count = {}    
    with open('./files/input/data.csv', 'r') as file:
        for line in file:
            data = line.split()
            dictionary = data[4].split(",")
            for item in dictionary:
                if ":" in item:
                    key, value = item.split(":")
                    value = int(value)
                    if key in letters_count:
                        letters_count[key][0] = min(letters_count[key][0], value)
                        letters_count[key][1] = max(letters_count[key][1], value)
                    else:
                        letters_count[key] = [value, value]

    letters_count = [(key, min_val, max_val) for key, (min_val, max_val) in letters_count.items()]
    letters_count = sorted(letters_count, key=lambda x: x[0])
    return letters_count