import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


longitud = int(input("escribe la longitud de tu contrasena: "))

comillas = ""



for i in range (longitud):
    comillas += random.choice(caracteres) 

print(comillas)
