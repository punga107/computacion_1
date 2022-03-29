import os

path = r'D:\Uni\computacion\SecretKey'
listas = os.listdir(path)
print(listas)
print(listas[1])
os.chdir(path)
os.rename(listas[0], 'cairo.jpg')

