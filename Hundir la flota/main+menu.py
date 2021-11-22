import pygame
from constants import *
import os

FPS = 60
GAMEBOARD = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "battleship_board.png")), (WIDTH, HEIGHT))
MENU = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_menu.png")), (WIDTH, HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hundir la flota")


def draw_menu(boton_iniciar, boton_cargar, boton_guardar, boton_salir):
    WIN.blit(MENU, (0,0))
    if boton_iniciar: WIN.blit(BOTON_INICIAR_PARTIDA, INICIAR_COORDS)
    if boton_cargar: WIN.blit(BOTON_CARGAR_PARTIDA, CARGAR_COORDS)
    if boton_guardar: WIN.blit(BOTON_GUARDAR_PARTIDA, GUARDAR_COORDS)
    if boton_salir: WIN.blit(BOTON_SALIR, SALIR_COORDS)

    pygame.display.update()


def draw_gameboard(pressed_square_x, pressed_square_y, cuadrados_verdes):
    WIN.blit(GAMEBOARD, (0,0))
    WIN.blit(PRESSED_SQUARE, (pressed_square_x, pressed_square_y)) # cuadrado verde
    for coord_cuadrado in cuadrados_verdes: # pongo un cuadrado verde sobre los cuadrados en los que se ha hecho click
        WIN.blit(PRESSED_SQUARE, coord_cuadrado)
    pygame.display.update()


def menu():
    iniciar = pygame.Rect(INICIAR_COORDS, BOTON_DIM)
    cargar = pygame.Rect(CARGAR_COORDS, BOTON_DIM)
    guardar = pygame.Rect(GUARDAR_COORDS, BOTON_DIM)
    salir = pygame.Rect(SALIR_COORDS, BOTON_DIM)

    clock = pygame.time.Clock()
    menu = True
    pressed = False
    boton_iniciar = boton_cargar = boton_guardar = boton_salir = False

    while menu: # bucle principal menú
        clock.tick(FPS)
        boton_iniciar = boton_cargar = boton_guardar = boton_salir = False

        pos = pygame.mouse.get_pos() # da la posición del puntero
        if iniciar.collidepoint(pos):
            boton_iniciar = True
            if pressed == True:
                menu = False
        elif cargar.collidepoint(pos):
            boton_cargar = True
            if pressed == True:
                print("cargar")
        elif guardar.collidepoint(pos):
            boton_guardar = True
            if pressed == True:
                print("guardar")
        elif salir.collidepoint(pos):
            boton_salir = True
            if pressed == True:
                pygame.quit()

        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        draw_menu(boton_iniciar, boton_cargar, boton_guardar, boton_salir)


def main():
    # creo en una lista rectángulos = a los cuadraditos del tablero 1
    squares_1 = [pygame.Rect((SQUARE_SIZE*(2+num_1), SQUARE_SIZE*(5+num_2)), (SQUARE_SIZE, SQUARE_SIZE)) for num_1 in range(16) for num_2 in range(16)]
    # creo en una lista rectángulos = a los cuadraditos del tablero 2
    squares_2 = [pygame.Rect((SQUARE_SIZE*(20+num_1), SQUARE_SIZE*(5+num_2)), (SQUARE_SIZE, SQUARE_SIZE)) for num_1 in range(16) for num_2 in range(16)]

    game = True
    pressed = False
    clock = pygame.time.Clock()
    cuadrados_verdes = []
    
    while game: # bucle principal juego
        clock.tick(FPS)

        pressed_square_x, pressed_square_y = -100, -100 # pongo el cuadrado verde fuera de la pantalla
        pos = pygame.mouse.get_pos() # da la posición del puntero

        for square in squares_1: # compruebo todos los cuadrados en el tablero 1
            if square.collidepoint(pos): # si el puntero está encima del cuadrado, cambio las coord del cuadrado verde
                pressed_square_x, pressed_square_y = square.left, square.top
                if pressed == True: # si se hace click, añado a la lista cuadrados_verdes las coord del cuadrado en el que se hace click
                    if (square.left, square.top) not in cuadrados_verdes:
                        cuadrados_verdes.append((square.left, square.top))
        
        for square in squares_2: # hago lo mismo con el tablero 2
            if square.collidepoint(pos):
                pressed_square_x, pressed_square_y = square.left, square.top
                if pressed == True:
                    if (square.left, square.top) not in cuadrados_verdes:
                        cuadrados_verdes.append((square.left, square.top))

        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si le doy a la cruz, que se salga del programa
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN: # si presiono un botón del ratón, y si es click izquierdo, pressed = True
                if event.button == 1: 
                    pressed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False

        if len(cuadrados_verdes) == 3:
            cuadrados_verdes = [cuadrados_verdes[-1]]
        
        draw_gameboard(pressed_square_x, pressed_square_y, cuadrados_verdes) # paso a la función dibujar tablero la posición del cuadrado verde


if __name__ == "__main__":
    while True:
        menu()
        main()
