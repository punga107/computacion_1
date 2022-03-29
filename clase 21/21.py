list = ['facu', 5, 'true', [1, 2]]

print(list)
## el [1] es para llamar el segundo objeto de la lista
print(list[1])
##el -1 funciona para llamar al archivo ultimo de la lista
print(list[-1])
##el 0 es inclusive y el 2 es exclusive, no toma el objeto.
print(list[0:2])
## si no pongo el valor excluyente, toma hasta el final de la lista
print(list[0:])
## el .append es para agregar un valor al final de la lista
list.append(-4)
print(list)
# el index es para mostrar el lugar donde esta el parametro que llamamos
print(list.index(5))
# extend es para agregar dos elementos al final de la lista
list.extend('12')
print(list)
# el len es para saber el tamanho de la lista
print(len(list))
# los tuples son lista que no se pueden modificar
tuple = (1, 2, 3)
# una coleccion de elementos que son accedidos a traves de una clave
x = {1: 'uno', 2: "dos"}
print(x[1])
print('termino lista')


# funciones

def suma(num1, num2):
    total = num1 + num2
    print(total)
    return


print(suma(1, 2))

a = 5


def function():
    print(a)
    return
