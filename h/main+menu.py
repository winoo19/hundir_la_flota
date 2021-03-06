import pygame
from constants import *
import os

FPS = 60
TITULO = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_titulo.png")), (WIDTH, HEIGHT))
OPTIONS = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_options.png")), (WIDTH, HEIGHT))
MENU = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_menu.png")), (WIDTH, HEIGHT))
GAMEBOARD = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "battleship_board.png")), (WIDTH, HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hundir la flota")


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


def draw_options(cuadricula, cantidad_barcos, jugar):
    WIN.blit(OPTIONS, (0,0))

    if cuadricula == 16:
        WIN.blit(BOTON_CUAD_16, CUAD_16_COORDS)
    elif cuadricula == 10:
        WIN.blit(BOTON_CUAD_10, CUAD_10_COORDS)

    if cantidad_barcos == 2:
        WIN.blit(BOTON_BARCOS_2, BOTON_BARCOS_2_COORDS)
    elif cantidad_barcos == 3:
        WIN.blit(BOTON_BARCOS_3, BOTON_BARCOS_3_COORDS)
    elif cantidad_barcos == 4:
        WIN.blit(BOTON_BARCOS_4, BOTON_BARCOS_4_COORDS)
    elif cantidad_barcos == 5:
        WIN.blit(BOTON_BARCOS_5, BOTON_BARCOS_5_COORDS) 

    if jugar:
        WIN.blit(BOTON_JUGAR, BOTON_JUGAR_COORDS)

    pygame.display.update()


def draw_gameboard(pressed_square_x, pressed_square_y, cuadrados_verdes, boats, len_barco,
 cantidad_barcos, ataque, resultado, casillas_agua, casillas_tocado, barcos_hundidos_1, barcos_hundidos_2,
 boats_player_1, boats_player_2):
    dict_barco = {2:TEXTO_BARCO_2, 3:TEXTO_BARCO_3, 4:TEXTO_BARCO_4, 5:TEXTO_BARCO_5, 6:TEXTO_BARCO_6}
    WIN.blit(GAMEBOARD, (0,0))
    WIN.blit(PRESSED_SQUARE, (pressed_square_x, pressed_square_y)) # cuadrado verde
    if len_barco != 8:
        for coord_cuadrado in cuadrados_verdes: # pongo un cuadrado verde sobre los cuadrados en los que se ha hecho click
            WIN.blit(PRESSED_SQUARE, coord_cuadrado)
        if len_barco < cantidad_barcos+2:
            WIN.blit(dict_barco[len_barco], TEXTO_COORDS)
    
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
    else:
        for numero in range(len(casillas_agua)):
            WIN.blit(CASILLA_AGUA, casillas_agua[numero])
        for numero in range(len(casillas_tocado)):
            WIN.blit(CASILLA_TOCADO, casillas_tocado[numero])
        
        for numero in barcos_hundidos_1:
            print(numero)
            print(boats_player_1)
            if boats_player_1[numero][0][0] == boats_player_1[numero][1][0]:
                vertical = True
            else:
                vertical = False

            for num in range(len(boats_player_1[numero])):
                if vertical:
                    if num == 0:
                        WIN.blit(SPRITE_V_I, boats_player_1[numero][num])
                    elif num == len(boats_player_1[numero])-1:
                        WIN.blit(SPRITE_V_F, boats_player_1[numero][num])
                    else:
                        WIN.blit(SPRITE_V_M, boats_player_1[numero][num])
                else:
                    if num == 0:
                        WIN.blit(SPRITE_H_I, boats_player_1[numero][num])
                    elif num == len(boats_player_1[numero])-1:
                        WIN.blit(SPRITE_H_F, boats_player_1[numero][num])
                    else:
                        WIN.blit(SPRITE_H_M, boats_player_1[numero][num])        

    pygame.display.update()


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

    while titulo: # bucle principal men??
        clock.tick(FPS)
        boton_continuar = False

        pos = pygame.mouse.get_pos() # da la posici??n del puntero
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

    while menu: # bucle principal men??
        clock.tick(FPS)
        boton_iniciar = boton_cargar = boton_guardar = boton_salir = False

        pos = pygame.mouse.get_pos() # da la posici??n del puntero
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


def options():
    cuadricula_16 = pygame.Rect(CUAD_16_COORDS, BOTON_CUAD_DIM)
    cuadricula_10 = pygame.Rect(CUAD_10_COORDS, BOTON_CUAD_DIM)
    barcos_2 = pygame.Rect(BOTON_BARCOS_2_COORDS, BOTON_BARCOS_DIM)
    barcos_3 = pygame.Rect(BOTON_BARCOS_3_COORDS, BOTON_BARCOS_DIM)
    barcos_4 = pygame.Rect(BOTON_BARCOS_4_COORDS, BOTON_BARCOS_DIM)
    barcos_5 = pygame.Rect(BOTON_BARCOS_5_COORDS, BOTON_BARCOS_DIM)
    jugar = pygame.Rect(BOTON_JUGAR_COORDS, BOTON_JUGAR_DIM)

    clock = pygame.time.Clock()
    options = True
    pressed = False

    cuadricula = cantidad_barcos = 0
    cuadricula_pressed = cantidad_barcos_pressed = jugar_on_top = False

    while options:
        clock.tick(FPS)

        if not cuadricula_pressed: cuadricula = 0
        if not cantidad_barcos_pressed: cantidad_barcos = 0
        jugar_on_top = False

        pos = pygame.mouse.get_pos()
        if cuadricula_16.collidepoint(pos) and not cuadricula_pressed:
            cuadricula = 16
            if pressed:
                cuadricula_pressed = True
        elif cuadricula_10.collidepoint(pos) and not cuadricula_pressed:
            cuadricula = 10
            if pressed:
                cuadricula_pressed = True
        elif barcos_2.collidepoint(pos) and not cantidad_barcos_pressed:
            cantidad_barcos = 2
            if pressed:
                cantidad_barcos_pressed = True
        elif barcos_3.collidepoint(pos) and not cantidad_barcos_pressed:
            cantidad_barcos = 3
            if pressed:
                cantidad_barcos_pressed = True
        elif barcos_4.collidepoint(pos) and not cantidad_barcos_pressed:
            cantidad_barcos = 4
            if pressed:
                cantidad_barcos_pressed = True
        elif barcos_5.collidepoint(pos) and not cantidad_barcos_pressed:
            cantidad_barcos = 5
            if pressed:
                cantidad_barcos_pressed = True
        elif jugar.collidepoint(pos) and cantidad_barcos_pressed and cuadricula_pressed:
            jugar_on_top = True
            if pressed:
                options = False

        pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        draw_options(cuadricula, cantidad_barcos, jugar_on_top)
    
    return cuadricula, cantidad_barcos


def main(cuadricula, cantidad_barcos):

    # creo en una lista rect??ngulos = a los cuadraditos del tablero 1
    squares_1 = [pygame.Rect((SQUARE_SIZE*(2+num_1), SQUARE_SIZE*(5+num_2)), (SQUARE_SIZE, SQUARE_SIZE))
                for num_1 in range(16) for num_2 in range(16)]

    # creo en una lista rect??ngulos = a los cuadraditos del tablero 2
    squares_2 = [pygame.Rect((SQUARE_SIZE*(20+num_1), SQUARE_SIZE*(5+num_2)), (SQUARE_SIZE, SQUARE_SIZE))
                for num_1 in range(16) for num_2 in range(16)]

    game = True
    pressed = False
    clock = pygame.time.Clock()
    cuadrados_verdes = []
    boats = []
    len_barco = 2
    boats_player_2 = []
    boats_player_1 = []
    ataque = []
    ataque1 = []
    ataque2 = []
    turno_1, turno_2 = True, False
    resultado = ""
    casillas_agua = []
    casillas_tocado = []
    barcos_hundidos_1 = []
    barcos_hundidos_2 = []

    while game: # bucle principal juego
        clock.tick(FPS)
        
        pressed_square_x, pressed_square_y = -100, -100 # pongo el cuadrado verde fuera de la pantalla
        pos = pygame.mouse.get_pos() # da la posici??n del puntero

        if len_barco == cantidad_barcos+2:
            pygame.time.delay(1000)
            if turno_1:
                turno_1, turno_2 = False, True
                boats_player_1 = boats
                restantes_1 = boats_player_1
                boats, len_barco = [], 2
            else:
                boats_player_2 = boats
                restantes_2 = boats_player_2
                boats, len_barco = [], 8

        if turno_1:
            
            for square in squares_1: # compruebo todos los cuadrados en el tablero 1
                if square.collidepoint(pos): # si el puntero est?? encima del cuadrado, cambio las coord del cuadrado verde
                    pressed_square_x, pressed_square_y = square.left, square.top
                    if pressed == True: # si se hace click, a??ado a la lista cuadrados_verdes las coord del cuadrado en el que se hace click
                        if (square.left, square.top) not in cuadrados_verdes:
                            cuadrados_verdes.append((square.left, square.top))
        elif turno_2:
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

            if event.type == pygame.MOUSEBUTTONDOWN: # si presiono un bot??n del rat??n, y si es click izquierdo, pressed = True
                if event.button == 1: 
                    pressed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False

        if len_barco < cantidad_barcos+2:
            if len(cuadrados_verdes) == 2:
                if barco_correcto(cuadrados_verdes, len_barco, boats):
                    boats.append(barco_correcto(cuadrados_verdes, len_barco, boats))
                    len_barco += 1
                cuadrados_verdes = []

        elif turno_1 and cuadrados_verdes not in ataque1:
            if cuadrados_verdes:
                ataque = cuadrados_verdes[0]
                ataque1.append(ataque)
                resultado = "a"
                print("esto es el turno 1: ", ataque)
                print(boats_player_1)
                for i in range(len(restantes_1)):
                    if ataque in restantes_1[i]:
                        restantes_1[i].remove(ataque)
                        if not restantes_1[i]:
                            if not restantes_1: # victoria
                                pass
                            else:
                                resultado = "h"
                                barcos_hundidos_1.append(i)
                        else:
                            resultado = "t"
                if resultado == "a":
                    casillas_agua.append(ataque)
                if resultado == "t":
                    casillas_tocado.append(ataque)
                turno_1 = not turno_1
                turno_2 = not turno_2
            cuadrados_verdes = []

        elif turno_2 and cuadrados_verdes not in ataque2:
            if cuadrados_verdes:
                ataque = cuadrados_verdes[0]
                print("esto es el turno 2:", ataque)
                print(boats_player_2)
                ataque2.append(ataque)
                resultado = "a"
                for i in range(len((restantes_2))):
                    if ataque in restantes_2[i]:
                        restantes_2[i].remove(ataque)
                        if not restantes_2[i]:
                            if not restantes_2: # victoria
                                pass
                            else:
                                resultado = "h"
                                barcos_hundidos_2.append(i)
                        else:
                            resultado = "t"
                if resultado == "a":
                    casillas_agua.append(ataque)
                if resultado == "t":
                    casillas_tocado.append(ataque)
                turno_1 = not turno_1
                turno_2 = not turno_2
            cuadrados_verdes = []

        
        draw_gameboard(pressed_square_x, pressed_square_y, cuadrados_verdes,
                        boats, len_barco, cantidad_barcos, ataque, resultado, casillas_agua,
                         casillas_tocado, barcos_hundidos_1, barcos_hundidos_2, boats_player_1, boats_player_2)


if __name__ == "__main__":
    titulo()
    while True:
        menu()
        option = options()
        main(option[0], option[1])
