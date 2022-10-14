import pygame as pg
from config import *


class Pieces(pg.sprite.Sprite):
    def __init__(self, cell_size: int, color: str, field_name: str, file_posfix: str):
        super().__init__()
        picture = pg.image.load(PIECE_PATH + color + file_posfix)
        self.image = pg.transform.scale(picture, (cell_size, cell_size))
        self.rect = self.image.get_rect()  # 0 0 70 70
        self._color = color
        self.field_name = field_name
        self.allowed_steps = pg.sprite.Group()


class King(Pieces):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_king.png')

    def true_step(self):
        for cell in self.__all_cells:
            if cell.field_name[0]:
                pass



class Queen(Pieces):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_queen.png')



class Rook(Pieces):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_rook.png')


class Knight(Pieces):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_knight.png')


class Bishop(Pieces):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_bishop.png')


class Pawn(Pieces):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_pawn.png')
