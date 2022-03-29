file = open('tp 2.py', 'w')
file.write('hola mundo')
file.close()
file = open('tp 2.py', 'a')
file.write('\ntetris')
file.close()
file = open('tp 2.py', 'a')
file.write('fue')
file.close()
file = open('tp 2.py', 'r')
print(file.readlines())
file.close()

file = open('tp 2.py')
list = file.readlines()
print(list)
rem = '\n'
list = list.replace(rem)
print(list)
file.close()



