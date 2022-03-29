# ej 10


def missing_letter(word, num):
    max = len(word)
    if num >= max:
        print('error, su num nunca puede ser mayor a la cantidad de letras de la palabra')
    else:
        list = []
        list.extend(word)
        list.pop(num)
        print(word)
        string = ''.join(list)
        print(string)
    return


print(missing_letter('cadena', 5))