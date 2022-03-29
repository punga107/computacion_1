# ej 1

print('dia de semana = 1, fin de semana = 0')
dia_semana = int(input("es un dia de semana: "))


list2 = "0 no estas de vacaciones, 1 estas de vacaciones"
print(list2)
vacaciones = int(input("ingrese 0 o 1 para saber si esta de vacaciones: "))


def dormimos(dia_semana, vacaciones):
    if dia_semana == 0 and vacaciones == 0:
        print("dormimos")

    if dia_semana == 1 and vacaciones == 0:
        print("no dormimos")

    if dia_semana == 0 and vacaciones == 1:
        print("dormimos")

    return



print(dormimos(0, 0))



