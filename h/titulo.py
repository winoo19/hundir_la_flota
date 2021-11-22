#ESTO EN COORDENADAS
#coord y dim imagenes
CONTINUAR_DIM = (187, 57)
CONTINUAR_COORDS = (448, 537)
#imagenes
BOTON_CONTINUAR = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "continuar.png")), CONTINUAR_DIM)


import pygame
from constants import *
import os

TITULO = pygame.transform.scale(pygame.image.load(os.path.join("imagenes", "fondo_titulo.png")), (WIDTH, HEIGHT))

def draw_titulo(boton_continuar):
    WIN.blit(TITULO, (0,0))
    if boton_continuar: WIN.blit(BOTON_CONTINUAR, CONTINUAR_COORDS)

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

if __name__ == "__main__":
    titulo()
    while True:
        
        menu()
        main()