# ej 8


def negative(num1, num2):
    if num1 >= 0 and num2 < 0:
        print('true')
    elif num1 < 0  and num2 < 0:
        print('true')
    elif num1 < 0 and num2 > 0:
        print('false')
    elif num1 > 0 and num2 > 0:
        print('flase')

    return


print(negative(10, 2))