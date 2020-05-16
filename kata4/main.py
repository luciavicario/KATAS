import pygame
import random

#Variables
screen_width = 500
screen_height = 300

#Colors
back_color=(200,200,200)
light_gray = pygame.Color('grey12')

# Reloj
pygame.init()
clock = pygame.time.Clock()

# Definir pantalla con altura y anchura
screen = pygame.display.set_mode((screen_width,screen_height))

# Objetos: 
# 10 pixeles parte superior e izquierda, y base y altura
rectangulo = pygame.Rect (5,5,5,70)
bola = pygame.Rect (25,5,25,25)

speed = 0
speed_bola_x = 3
speed_bola_y = 3

def start_bola():
    global speed_bola_x, speed_bola_y

    # Rebotar en las paredes ( + anchura de 50 )  igual a posición incicial
    if bola.left + 50 > screen_width or bola.left <0:
        bola.top = 50
        bola.left = 10
        
        speed_bola_x = 3 * random.choice((1,-1))
        speed_bola_y = 3 * random.choice((1,-1))

def mover_bola():
    global speed_bola_x, speed_bola_y

    # Rebotar abajo y arriba ( + altura de 50) invertir velocidad
    if bola.top + 50 > screen_height:
        speed_bola_x = -speed_bola_x
    if bola.top < 0:
        speed_bola_x = -speed_bola_x

    # Rebotar en la plataforma
    if bola.left < 10 and rectangulo.top < bola.top < rectangulo.top + 140:
        speed_bola_y = -speed_bola_y

    start_bola()

    bola.top += speed_bola_x
    bola.left += speed_bola_y

def mover_rectangulo():
    global speed
    # Si no llega a la altura completa que siga bajando, si no que pare
    if rectangulo.top +50 < screen_height:
        rectangulo.top += speed


#El juego debe funcionar siempre
while True:
    #Color aplicado
    screen.fill(light_gray)

    # Evento tipo tecla PULSAR (KEYDOWN)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -3
            if event.key == pygame.K_DOWN:
                speed = 3
        else:
            speed = 0

    mover_rectangulo()
    mover_bola()

    # Dibujarlo y hacer que se mueva llamando a la funcion antes
    pygame.draw.rect(screen,back_color,rectangulo)
    pygame.draw.ellipse(screen, back_color,bola)

    #Movimiento fuido
    pygame.display.flip()

    #Calcular el tiempo entre 2 frames, para 60 frames/s
    clock.tick(60)