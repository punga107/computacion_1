# ej 2.
print("si esta sonriendo ponga 1, sino 0 ")



def problema_monos(mono1, mono2):
    if mono1 == 1 and mono2 == 1:
        print("estamos en peligro")

    if mono1 == 0 and mono2 == 0:
        print("estamos en peligro")

    if mono1 == 1 and mono2 == 0:
        print("estamos seguros")

    if mono1 == 0 and mono2 == 1:
        print("estamos seguros")

    return


print(problema_monos(0, 0))