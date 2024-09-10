print("Generador de contraseñas\n")
import random
import string

caracter = string.ascii_letters
numbers =  string.digits
especiales = string.punctuation

longitud = int(input("Ingresa la longitud de tu contraseña: "))

contrasenia = ''

for _ in range(longitud):
    r = random.randrange(100)
    if r < 10:
        contrasenia += random.choice(especiales)
    elif r < 20:
        contrasenia += random.choice(numbers)
    else:
        contrasenia += random.choice(caracter)


print(f'La contraseña es: {contrasenia}')

#-----------------------------------------------------------------------------------------------------------------------------------

