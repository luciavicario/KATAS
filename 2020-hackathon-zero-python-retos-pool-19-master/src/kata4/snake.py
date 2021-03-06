import pygame, sys, time, random
from pygame.locals import *

pygame.init()
play_surface = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

speed = 0

class Snake():
    position = [100,50]
    body = [[100,50],[90,50],[80,50]]
    direction = "RIGHT"
    change = direction

    # Manejo del pressed [KEYDOWN] de las teclas [K_RIGHT - K_LEFT - K_UP -K_DOWN ]
    def controller(self, event, pygame):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.direction = "UP"
            if event.key == pygame.K_DOWN:
                self.direction = "DOWN"
            if event.key == pygame.K_RIGHT:
                self.direction = "RIGHT"
            if event.key == pygame.K_LEFT:
                self.direction = "LEFT"
    
    # Controla el cambio de  las direcciones
    # Orientaciones
    # Vertical      -> Movimientos [RIGHT - LEFT]
    # Horizontal    -> Movimientos [UP - DOWN]
    # Incremento del movimiento 
    def changeDirection(self):
        if self.direction == "UP":
            self.position = [self.position[0], self.position[1] - 1]
            self.body.insert(0, list(self.position))
            self.body.pop()
        elif self.direction == "DOWN":
            self.position = [self.position[0], self.position[1] + 1]
            self.body.insert(0, list(self.position))
            self.body.pop()
        elif self.direction == "LEFT":
            self.position = [self.position[0] - 1, self.position[1]]
            self.body.insert(0, list(self.position))
            self.body.pop()
        elif self.direction == "RIGHT":
            self.position = [self.position[0] + 1, self.position[1]]
            self.body.insert(0, list(self.position))
            self.body.pop()
    
class Game():
    run = True
    food_pos = [0,0]
    score = 0

    def __init__(self):
        self.food_spawn()

    # función de salida
    def exit(self, event, pygame):
        if event.type == pygame.QUIT:
            self.run = False  
    
    # Posición aleatorio entre el rango [0,49] * 10  
    def food_spawn(self):
        self.food_pos[0] = 10 * random.choice(range(0, 49))
        self.food_pos[1] = 10 * random.choice(range(0, 49))

    # Si colisionas con una fruta, sumas 1
    # Sino decrementas en 1 el body del snake
    def eat(self, snake):
        last_pos = len(snake.body) -1
        if (self.food_pos[0] - 5 <= snake.position[0] <= self.food_pos[0] + 5) and (self.food_pos[1]-5 <= snake.position[1] <= self.food_pos[1]+5):
            self.score += 1
            if snake.body[0][1]<snake.body[last_pos][1]:
                pos = [snake.body[last_pos][0], snake.body[last_pos][1]+ 10]
            elif snake.body[0][1]>snake.body[last_pos][1]:
                pos = [snake.body[last_pos][0], snake.body[last_pos][1]- 10]
            elif snake.body[0][0]<snake.body[last_pos][0]:
                pos = [snake.body[last_pos][0] + 10, snake.body[last_pos][1]]
            elif snake.body[0][0]>snake.body[last_pos][0]:
                pos = [snake.body[last_pos][0] - 10, snake.body[last_pos][1]]
            snake.body.append(list(pos))
            self.food_spawn()



    # Mensajes de salida cuando el snake muere
    # Posición snake[0] >= 500 ó snake[0] <= 0                  -> Muere
    # Posición snake[1] >= 500 ó snake[1] <= 0                  -> Muere
    # Posición del snake choca con sigo mismo menos la cabeza   -> Muere 
    def dead(self, snake):
        positions = snake.body
        indices = range(1, len(snake.body) -1)
        pos_result = [positions[i] for i in indices]
        for pos in pos_result:
            if snake.position[0] == pos[0] and snake.position[1] == pos[1]:
                self.run = False
        
        if snake.position[0] >= 500 or snake.position[0] <= 0 or snake.position[1] >= 500 or snake.position[1] <= 0:
            self.run = False
  
# Entry Point
def main():
    # Descomentar para lanzar el juego en local
    # Comentar para validar con el oráculo

    snake = Snake()
    game = Game()

    # Bucle principal
    while game.run:
        for event in pygame.event.get():
            game.exit(event, pygame)
            snake.controller(event, pygame)
        
        snake.changeDirection()

        game.eat(snake)

        # Dibujar Snake
        play_surface.fill((0,0,0))
        for pos in snake.body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

        game.dead(snake)

        pygame.display.flip()
        fps.tick(60)

        
# Comienza la aventura!!!!
# Descomentar para lanzar el juego en local
# Comentar para validar con el oráculo
main()
pygame.quit()
