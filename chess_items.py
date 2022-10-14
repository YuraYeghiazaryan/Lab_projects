from pieces import*
import board_data

pg.init()
fnt_obj = pg.font.Font(pg.font.get_default_font(), fnt_size)


class Chessboard:
    def __init__(self, parent_surface: pg.Surface):
        self.__screen = parent_surface
        self.__table = board_data.board
        self.__cells = cells
        self.__size = cell_size
        self.__pieces_types = PIECES_TYPES
        self.__pressed_cell = None
        self.__picked_piece = None
        self.__all_cells = pg.sprite.Group()
        self.__all_pieces = pg.sprite.Group()
        self.__prepare_screen()
        self.__draw_playboard()
        self.__draw_all_pieces()
        pg.display.update()

    def __prepare_screen(self):
        back_img = pg.image.load(IMG_PATH)
        back_img = pg.transform.scale(back_img, win_size)
        self.__screen.blit(back_img, (0, 0))

    def __draw_playboard(self):
        total_width = self.__cells * self.__size
        num_fields = self.__create_num_fields()
        self.__all_cells = self.__create_all_cells()
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
        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)
        cells_offset = (
            playboard_rect.x + num_fields_depth,
            playboard_rect.y + num_fields_depth,
        )
        self.__draw_cells_on_playbord(cells_offset)

    def __create_num_fields(self):
        n_lines = pg.Surface((self.__cells * self.__size, self.__size // 3))
        n_rows = pg.Surface((self.__size // 3, self.__cells * self.__size))
        for i in range(self.__cells):
            letter = fnt_obj.render(chr(65 + i), True, (255, 255, 255))
            number = fnt_obj.render(str(cells - i), True, (255, 255, 255))
            n_lines.blit(letter, (
                i * cell_size + (cell_size - letter.get_rect().width) // 2,
                (n_lines.get_height() - letter.get_rect().height) // 2
            ))
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,
                i * cell_size + (cell_size - number.get_rect().height) // 2
            ))
        return n_rows, n_lines

    def __create_all_cells(self):
        group = pg.sprite.Group()
        cell_color_index = 0
        for y in range(self.__cells):
            for x in range(self.__cells):
                cell = Cell(
                    cell_color_index,
                    self.__size,
                    (x, y),
                    LTRS[x] + str(self.__cells - y)
                )
                group.add(cell)
                cell_color_index ^= True
            cell_color_index ^= True
        return group

    def __draw_cells_on_playbord(self, offset):
        for cell in self.__all_cells:
            cell.rect.x += offset[0]
            cell.rect.y += offset[1]
        self.__all_cells.draw(self.__screen)

    def __draw_all_pieces(self):
        self.__setup_board()
        self.__all_pieces.draw(self.__screen)

    def __setup_board(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    piece = self.__create_piece(field_value, (j, i))
                    self.__all_pieces.add(piece)
        for piece in self.__all_pieces:
            for cell in self.__all_cells:
                if piece.field_name == cell.field_name:
                    piece.rect = cell.rect

    def __create_piece(self, piece_symbol: str, table_coord: tuple):
        field_name = self.__to_field_name(table_coord)
        piece_tuple = self.__pieces_types[piece_symbol]
        classname = globals()[piece_tuple[0]]
        return classname(self.__size, piece_tuple[1], field_name)

    def __get_cell(self, position: tuple):
        for cell in self.__all_cells:
            if cell.rect.collidepoint(position):
                return cell
        return None

    def __to_field_name(self, table_coord: tuple):
        return LTRS[table_coord[1]] + str(self.__cells - table_coord[0])

    def btn_down(self, button_type: int, position: tuple):
        self.__pressed_cell = self.__get_cell(position)

    def btn_up(self, button_type: int, position: tuple):
        released_cell = self.__get_cell(position)
        if (released_cell is not None) and (released_cell == self.__pressed_cell):
            if button_type == 1:
                self.__pick_cell(released_cell)
            else:
                pass
        self.__grand_update()

    def __pick_cell(self, cell):
        if self.__picked_piece is None:
            for piece in self.__all_pieces:
                if piece.field_name == cell.field_name:
                    self.__picked_piece = piece
                    break
        else:
            for piece in self.__all_pieces:
                if piece.field_name == cell.field_name and self.__picked_piece != piece:
                    piece.kill()
            else:
                self.__picked_piece.rect = cell.rect
                self.__picked_piece.field_name = cell.field_name
                self.__picked_piece = None

    def __grand_update(self):
        self.__all_cells.draw(self.__screen)
        self.__all_pieces.draw(self.__screen)
        pg.display.update()


class Cell(pg.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str):
        super().__init__()
        x, y = coords
        #self.__picked = False
        self.color = color_index
        self.field_name = name
        self.image = pg.image.load(COLORS_FOR_BOARD[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)
