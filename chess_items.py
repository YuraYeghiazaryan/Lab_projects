import pygame as pg
from config import *


pg.init()
fnt_obj = pg.font.Font(pg.font.get_default_font(), fnt_size)


class Chessboard():
    def __init__(self, parent_surface: pg.Surface):
        self.__screen = parent_surface
        self.__prepare_screen()
        self.__draw_playboard(cells, size_cell)
        pg.display.update()

    def __prepare_screen(self):
        back_img = pg.image.load(img_path)
        back_img = pg.transform.scale(back_img, win_size)
        self.__screen.blit(back_img, (0, 0))

    def __draw_playboard(self, cells, size_cell):
        total_width = cells * size_cell
        num_fields = self.__create_num_fields(cells, size_cell)
        fields = self.__create_all_cells(cells, size_cell)
        num_fields_depth = num_fields[0].get_width()
        playboard_view = pg.Surface((
            2 * num_fields_depth + total_width,
            2 * num_fields_depth + total_width
        ))

        playboard_view.blit(num_fields[0],
                            (0, num_fields_depth))
        playboard_view.blit(num_fields[0],
                            (num_fields_depth + total_width, num_fields_depth))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, 0))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, num_fields_depth + total_width))
        playboard_view.blit(fields,
                            (num_fields_depth, num_fields_depth))
        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)


    def __create_num_fields(self, cells, size_cell):
        n_lines = pg.Surface((cells * size_cell, size_cell // 3))
        n_rows = pg.Surface((size_cell // 3, cells * size_cell))
        for i in range(cells):
            letter = fnt_obj.render(chr(65 + i), True, (255, 255, 255))
            number = fnt_obj.render(str(cells - i), True, (255, 255, 255))
            n_lines.blit(letter, (
                i * size_cell + (size_cell - letter.get_rect().width) // 2,
                (n_lines.get_height() - letter.get_rect().height) // 2
            ))
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,
                i * size_cell + (size_cell - number.get_rect().height) // 2
            ))
        return n_rows, n_lines

    def __create_all_cells(self, cells, size_cell):
        fields = pg.Surface((cells * size_cell, cells * size_cell))
        col_index = 0
        for i in range(cells):
            for j in range(cells):
                cell = pg.Surface((size_cell, size_cell))
                cell.fill(colors[col_index])
                fields.blit(cell, (i * size_cell, j * size_cell))
                col_index ^= True
            col_index ^= True
        return fields

