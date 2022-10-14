from config import *
import pygame as pg
from chess_items import *


clock = pg.time.Clock()
screen = pg.display.set_mode(win_size)
pg.display.set_caption("Pair to pair Chess")
screen.fill((150, 100, 25))

chessboard = Chessboard(screen)

run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

        if event.type == pg.MOUSEBUTTONDOWN:
            chessboard.btn_down(event.button, event.pos)
        if event.type == pg.MOUSEBUTTONUP:
            chessboard.btn_up(event.button, event.pos)
