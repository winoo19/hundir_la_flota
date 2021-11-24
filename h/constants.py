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


CUAD_16_COORDS = (406,300.5)
CUAD_10_COORDS = (564.75,309)
BOTON_CUAD_DIM = (109,42)

BOTON_BARCOS_2_COORDS = (430.5,482)
BOTON_BARCOS_3_COORDS = (492.25,483.25)
BOTON_BARCOS_4_COORDS = (552,480.75)
BOTON_BARCOS_5_COORDS = (614,482.75)
BOTON_BARCOS_DIM = (36,47)

BOTON_JUGAR_COORDS = (484,572.25)
BOTON_JUGAR_DIM = (109,47)


TEXTO_COORDS = (WIDTH//2- 945/2, 20)
TEXTO_DIM = (945,36)
# imagenes
BOTON_CONTINUAR = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_continuar.png")), CONTINUAR_DIM)


BOTON_INICIAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_nueva_partida.png")), BOTON_MENU_DIM)
BOTON_CARGAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_cargar_partida.png")), BOTON_MENU_DIM)
BOTON_GUARDAR_PARTIDA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_guardar_partida.png")), BOTON_MENU_DIM)
BOTON_SALIR = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_salir.png")), BOTON_MENU_DIM)


BOTON_CUAD_16 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_cuad_16.png")), BOTON_CUAD_DIM)
BOTON_CUAD_10 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_cuad_10.png")), BOTON_CUAD_DIM)
BOTON_BARCOS_2 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_barcos_2.png")), BOTON_BARCOS_DIM)
BOTON_BARCOS_3 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_barcos_3.png")), BOTON_BARCOS_DIM)
BOTON_BARCOS_4 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_barcos_4.png")), BOTON_BARCOS_DIM)
BOTON_BARCOS_5 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_barcos_5.png")), BOTON_BARCOS_DIM)
BOTON_JUGAR = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "boton_jugar.png")), BOTON_JUGAR_DIM)


SPRITE_H_I = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_h_l.png")), AREA_SQUARE)
SPRITE_H_M = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_h_m.png")), AREA_SQUARE)
SPRITE_H_F = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_h_r.png")), AREA_SQUARE)
SPRITE_V_I = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_v_u.png")), AREA_SQUARE)
SPRITE_V_M = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_v_m.png")), AREA_SQUARE)
SPRITE_V_F = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "hundido_v_d.png")), AREA_SQUARE)

TEXTO_BARCO_2 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "texto_2.png")), TEXTO_DIM)
TEXTO_BARCO_3 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "texto_3.png")), TEXTO_DIM)
TEXTO_BARCO_4 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "texto_4.png")), TEXTO_DIM)
TEXTO_BARCO_5 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "texto_5.png")), TEXTO_DIM)
TEXTO_BARCO_6 = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "texto_6.png")), TEXTO_DIM)

PRESSED_SQUARE = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "casilla.png")), (SQUARE_SIZE, SQUARE_SIZE))

CASILLA_AGUA = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "casilla_agua.png")), (SQUARE_SIZE, SQUARE_SIZE))
CASILLA_TOCADO = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "casilla_tocado.png")), (SQUARE_SIZE, SQUARE_SIZE))