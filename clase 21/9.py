# ej 9




def cadena():
    cadena1 = str(input("ingrese una palabra: "))

    list = []
    list.extend(cadena1)

    if list[0] == 'n' and list[1] == 'o':
        print(cadena1)
    elif list[0] != 'n' and list[1] != 'o':
        print("no", cadena1)

    return

print(cadena())