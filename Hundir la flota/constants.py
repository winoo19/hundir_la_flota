import pygame
import os

WIDTH, HEIGHT = 1080, 720
ROWS, COLS = 17, 17
SQUARE_SIZE = 29
AREA_SQUARE = (SQUARE_SIZE, SQUARE_SIZE)

# coord y dim imagenes
INICIAR_COORDS = (338, 247)
CARGAR_COORDS =(338, 363)
GUARDAR_COORDS = (338, 479)
SALIR_COORDS = (338, 595)
BOTON_MENU_DIM = (400, 52)

CONTINUAR_COORDS = (448, 537)
CONTINUAR_DIM = (187, 57)


# imagenes
BOTON_CONTINUAR = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_continuar.png")), CONTINUAR_DIM)

BOTON_INICIAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_nueva_partida.png")), BOTON_MENU_DIM)
BOTON_CARGAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_cargar_partida.png")), BOTON_MENU_DIM)
BOTON_GUARDAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_guardar_partida.png")), BOTON_MENU_DIM)
BOTON_SALIR = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_salir.png")), BOTON_MENU_DIM)

SPRITE_H_I = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_h_l.png")), AREA_SQUARE)
SPRITE_H_M = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_h_m.png")), AREA_SQUARE)
SPRITE_H_F = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_h_r.png")), AREA_SQUARE)
SPRITE_V_I = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_v_u.png")), AREA_SQUARE)
SPRITE_V_M = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_v_m.png")), AREA_SQUARE)
SPRITE_V_F = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_v_d.png")), AREA_SQUARE)

PRESSED_SQUARE = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "casilla.png")), (SQUARE_SIZE, SQUARE_SIZE))

# rgb
BLACK = (0, 0, 0)
