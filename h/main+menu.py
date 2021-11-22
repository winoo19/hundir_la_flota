from typing import Text
import pygame
from constants import *
import os

FPS = 60
TITULO = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_titulo.png")), (WIDTH, HEIGHT))
GAMEBOARD = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "battleship_board.png")), (WIDTH, HEIGHT))
MENU = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_menu.png")), (WIDTH, HEIGHT))

pygame.font.init()

TITULO = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_titulo.png")), (WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hundir la flota")

def draw_titulo(boton_continuar):
    WIN.blit(TITULO, (0,0))
    if boton_continuar: WIN.blit(BOTON_CONTINUAR, CONTINUAR_COORDS)

    pygame.display.update()

def draw_titulo(boton_continuar):
    WIN.blit(TITULO, (0,0))
    if boton_continuar: WIN.blit(BOTON_CONTINUAR, CONTINUAR_COORDS)

    pygame.display.update()


def draw_menu(boton_iniciar, boton_cargar, boton_guardar, boton_salir):
    WIN.blit(MENU, (0,0))
    if boton_iniciar: WIN.blit(BOTON_INICIAR_PARTIDA, INICIAR_COORDS)
    if boton_cargar: WIN.blit(BOTON_CARGAR_PARTIDA, CARGAR_COORDS)
    if boton_guardar: WIN.blit(BOTON_GUARDAR_PARTIDA, GUARDAR_COORDS)
    if boton_salir: WIN.blit(BOTON_SALIR, SALIR_COORDS)

    pygame.display.update()


def draw_gameboard(pressed_square_x, pressed_square_y, cuadrados_verdes, boats, len_barco):
    WIN.blit(GAMEBOARD, (0,0))
    WIN.blit(PRESSED_SQUARE, (pressed_square_x, pressed_square_y)) # cuadrado verde
    for coord_cuadrado in cuadrados_verdes: # pongo un cuadrado verde sobre los cuadrados en los que se ha hecho click
        WIN.blit(PRESSED_SQUARE, coord_cuadrado)
    for boat in boats:
        if boat[0][0] == boat[1][0]:
            vertical = True
        else:
            vertical = False

        for num in range(len(boat)):
            if vertical:
                if num == 0:
                    WIN.blit(SPRITE_V_I, boat[num])
                elif num == len(boat)-1:
                    WIN.blit(SPRITE_V_F, boat[num])
                else:
                    WIN.blit(SPRITE_V_M, boat[num])
            else:
                if num == 0:
                    WIN.blit(SPRITE_H_I, boat[num])
                elif num == len(boat)-1:
                    WIN.blit(SPRITE_H_F, boat[num])
                else:
                    WIN.blit(SPRITE_H_M, boat[num])

    if len_barco < 7:
        text = pygame.font.SysFont("timesnewroman", 40).render(f"Coloque el barco de dimensión {len_barco}", 1, BLACK)
        WIN.blit(text, (WIDTH//2 - text.get_width()//2, 40))

    pygame.display.update()

def titulo():
    continuar = pygame.Rect(CONTINUAR_COORDS, CONTINUAR_DIM)

    clock = pygame.time.Clock()
    titulo = True
    pressed = False
    boton_continuar = False

    while titulo: # bucle principal menú
        clock.tick(FPS)
        boton_continuar = False

        pos = pygame.mouse.get_pos() # da la posición del puntero
        if continuar.collidepoint(pos):
            boton_continuar = True
            if pressed == True:
                titulo = False
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        draw_titulo(boton_continuar)

def barco_correcto(cuadrados_verdes, len_barco, boats):
    casilla_1 = cuadrados_verdes[0]
    casilla_2 = cuadrados_verdes[1]
    barco = []
    disposicion = False

    if casilla_1[0] == casilla_2[0]: # vertical
        if abs(casilla_1[1]//SQUARE_SIZE-casilla_2[1]//SQUARE_SIZE)+1 == len_barco:
            for num in range(len_barco):
                barco.append((casilla_1[0], min(casilla_1[1], casilla_2[1])+num*SQUARE_SIZE))
            disposicion = True

    elif casilla_1[1] == casilla_2[1]: # horizontal
        if abs(casilla_1[0]//SQUARE_SIZE-casilla_2[0]//SQUARE_SIZE)+1 == len_barco:
            for num in range(len_barco):
                barco.append((min(casilla_1[0], casilla_2[0])+num*SQUARE_SIZE, casilla_1[1]))
            disposicion = True

    if disposicion:
        for boat in boats:
            for casilla in barco:
                if casilla in boat:
                    return False
    else:
        return False

    return barco


def titulo():
    continuar = pygame.Rect(CONTINUAR_COORDS, CONTINUAR_DIM)

    clock = pygame.time.Clock()
    titulo = True
    pressed = False
    boton_continuar = False

    while titulo: # bucle principal menú
        clock.tick(FPS)
        boton_continuar = False

        pos = pygame.mouse.get_pos() # da la posición del puntero
        if continuar.collidepoint(pos):
            boton_continuar = True
            if pressed == True:
                titulo = False
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        draw_titulo(boton_continuar)


def menu():
    iniciar = pygame.Rect(INICIAR_COORDS, BOTON_MENU_DIM)
    cargar = pygame.Rect(CARGAR_COORDS, BOTON_MENU_DIM)
    guardar = pygame.Rect(GUARDAR_COORDS, BOTON_MENU_DIM)
    salir = pygame.Rect(SALIR_COORDS, BOTON_MENU_DIM)

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
    squares_1 = [pygame.Rect((SQUARE_SIZE*(2+num_1), SQUARE_SIZE*(5+num_2)), (SQUARE_SIZE, SQUARE_SIZE))
                for num_1 in range(16) for num_2 in range(16)]

    # creo en una lista rectángulos = a los cuadraditos del tablero 2
    squares_2 = [pygame.Rect((SQUARE_SIZE*(20+num_1), SQUARE_SIZE*(5+num_2)), (SQUARE_SIZE, SQUARE_SIZE))
                for num_1 in range(16) for num_2 in range(16)]

    game = True
    pressed = False
    clock = pygame.time.Clock()
    cuadrados_verdes = []
    boats = []
    cond1 = False
    len_barco = 2
    
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

        if len(cuadrados_verdes) == 2 and len_barco < 7:
            if barco_correcto(cuadrados_verdes, len_barco, boats):
                boats.append(barco_correcto(cuadrados_verdes, len_barco, boats))
                len_barco += 1
            cuadrados_verdes = []
        
        draw_gameboard(pressed_square_x, pressed_square_y, cuadrados_verdes, boats, len_barco)


if __name__ == "__main__":
    titulo()
    while True:
        
        menu()
        main()