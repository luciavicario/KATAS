from random import randint

options = ["Piedra", "Papel", "Tijeras"]
piedra = options[0].lower()
papel = options[1].lower()
tijeras = options[2].lower()

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    
    if(player==ai):
        resultado = 'Empate!'
    elif (player == piedra and ai == papel) or (player == tijeras and ai == piedra) or (player == tijeras and ai == papel):
        resultado = 'Perdiste!'
    elif (player == papel and ai == piedra) or (player == piedra and ai == tijeras) or (player == tijeras and ai == papel):
        resultado = 'Ganaste!'
    return resultado


# Entry Point
def Game():
    player = input('Introduce piedra, papel o tijeras: ')
    player = player.lower()
    condition = True

    while (condition):
        if (player != piedra)and(player != papel)and(player != tijeras):
            player = input('Introduce de nuevo piedra, papel o tijeras: ')
        else:
            condition = False

    player_2 = randint(0,2)
    ai = options[player_2].lower()
    
    print('El otro usuario ha eligido ' + ai)

    winner = quienGana(player, ai)

    print(winner)

Game()