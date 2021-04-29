from math import degrees
import pygame as pg
import sys
from random import randint, choice

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO=(255,255,255)
ANCHO = 800
ALTO = 600
newValues = list(range(-10, -4)) + list(range(5, 11))


pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()


class Bola():
    def __init__(self, x, y, vx, vy, color, radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = radio

    def actualiza(self):
        self.x += self.vx
        self.y += self.vy

        if self.y <= 0 or self.y >= ALTO:
            self.vy = -self.vy
        if self.x <= 0 or self.x >= ANCHO:
            self.vx = -self.vx

    def dibujaBola(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.radio)


bolas = []

for _ in range(10):
    bola = Bola(randint(0, ANCHO),
                randint(0, ALTO),
                choice(newValues),
                choice(newValues),
                (randint(0, 255),
                randint(0, 255),
                randint(0, 255)))

    bolas.append(bola)


def main():
    game_over = False
    while not game_over:
        v = reloj.tick(30)

        # Gestion de eventos
        for evento in pg.event.get():
            # print(evento)
            if evento.type == pg.QUIT:
                game_over = True

        # Modificación de estado
        for bola in bolas:
            bola.actualiza()

        # Gestión de la pantalla
        pantalla.fill(BLANCO)

        for bola in bolas:
            bola.dibujaBola(pantalla)
            
        pg.display.flip()

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
