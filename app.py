import sys 
import pygame as pg
#import edad
#import ball

def fin_juego():
  pg.quit()
  sys.exit()

pg.init()
#Tamañao pantalla
width = 800
height = 600
size = (width, height)

# Definir colores: RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Crear pantalla
title = 'Juego de... Rompe cubos'
pantalla = pg.display.set_mode(size)
pg.display.set_caption(title)

#Definir Reloj para controlar los FPS
clock = pg.time.Clock()

#Crear bucle principal infinito
game_over = False
while not game_over:
    #Frames
    clock.tick(60)
    for event in pg.event.get():
        print(event)  
        #ball()      
        if event.type == pg.QUIT:
            game_over = True
 
    
    pantalla.fill(WHITE)
  
    #Actualizar pantalla
    pg.display.flip()

fin_juego()