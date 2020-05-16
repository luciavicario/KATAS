contraseña= 'contraseña'
user_contraseña = input ('Introduzca su contraseña: ')

if (user_contraseña.lower() == contraseña.lower()):
    print ('El password es correcto')
else:
    print('El password no coincide')