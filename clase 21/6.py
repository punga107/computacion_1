# ej 6


def make10 (num1, num2):
    total = num1 + num2
    if num1 == 10 or num2 == 10 or total == 10:
        print('true')
    elif num1 or num2 != 10:
        print('false')
    return


print(make10(6, 10))