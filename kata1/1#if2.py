edad = int(input('Introduce tu edad: '))
precio = 0
condition = True

while (condition):
    if (2 <= edad <=4):
        print('Entrada: Gratis')
        condition = False
    # edad >=4 and edad<=18
    elif (4 <= edad <=18):
        precio = 5
        print ('Entrada:' + str(precio))
        condition = False
    elif (edad>18):
        precio = 10
        print ('Entrada:' + str(precio))
        condition = False
    else:
        edad = int(input('Introduce de nuevo tu edad: '))
        condition = True
