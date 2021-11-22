import pygame
import os

WIDTH, HEIGHT = 1080, 720
ROWS, COLS = 17, 17
SQUARE_SIZE = 29
LINE_WIDTH = 3

#coord y dim imagenes
INICIAR_COORDS = (338, 247)
CARGAR_COORDS =(338, 363)
GUARDAR_COORDS = (338, 479)
SALIR_COORDS = (338, 595)
BOTON_DIM = (400, 52)

#imagenes
BOTON_INICIAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_nueva_partida.png")), BOTON_DIM)
BOTON_CARGAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_cargar_partida.png")), BOTON_DIM)
BOTON_GUARDAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_guardar_partida.png")), BOTON_DIM)
BOTON_SALIR = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_salir.png")), BOTON_DIM)

PRESSED_SQUARE = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "casilla.png")), (SQUARE_SIZE, SQUARE_SIZE))

#rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 180)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
