# pruebas

word = 'cadena'
list = []
list.extend(word)
list.pop(3)
print(word)
string = ''.join(list)
print(string)
print(len(word))







'''list = ['libro']
list2 = ['no']
list3 = list2 + list
print(list3)


def cambioazo():
    cambioutil = []
    cadena1 = 'no libro'
    list = []
    print(cadena1)
    list.extend(cadena1)
    print(list)
    print(list[0:2])
    cambio = 1
    if list[0] == 'n' and list[1] == 'o':
        int(input('sui su palabra empieza con un no, este no es parte de la palabra?, 1:si 2:no'))
    elif cambio == 1:
        listfinal = cambioutil + list
        print(listfinal)
    elif cambio == 0:
        pass
    return


print(cambioazo())



