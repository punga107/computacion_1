# ej 5


def loro(hablando, hora):
    if hablando == 1 and hora < 20:
        print("estamos en problemas")
    elif hablando == 1 and hora > 7:
        print('estamos en problemas')
    if hablando == 0:
        print('no estamos en problemas')
    elif hablando == 1 and hora > 20:
        print('no estamos en peligro')

    return


print(loro(1, 20))
