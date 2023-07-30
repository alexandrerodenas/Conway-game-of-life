import copy


class Board:
    def __init__(self, matrix: [[bool]]):
        self.__cells = matrix

    def get_cells(self):
        return copy.deepcopy(self.__cells)

    @property
    def get_rows_number(self):
        return len(self.__cells)

    @property
    def get_columns_number(self):
        return len(self.__cells[0])

    def compute_next_generation(self):
        new_generation: [[bool]] = self.get_cells()
        for i in range(self.get_rows_number):
            for j in range(self.get_columns_number):
                live_neighbours = self.__get_live_neighbours(i, j)
                if not self.__get_cell_at(i, j) and live_neighbours == 3:
                    new_generation[i][j] = True
                elif self.__get_cell_at(i, j) and (live_neighbours < 2 or live_neighbours > 3):
                    new_generation[i][j] = False

        return Board(new_generation)

    def __get_live_neighbours(self, i, j):
        live_cells_count = 0
        live_cells_count += self.__get_top_left_cell_alive_from(i, j) if 1 else 0
        live_cells_count += self.__get_top_cell_alive_from(i, j) if 1 else 0
        live_cells_count += self.__get_top_right_cell_alive_from(i, j) if 1 else 0
        live_cells_count += self.__get_left_cell_alive_from(i, j) if 1 else 0
        live_cells_count += self.__get_right_cell_alive_from(i, j) if 1 else 0
        live_cells_count += self.__get_bottom_left_cell_alive_from(i, j) if 1 else 0
        live_cells_count += self.__get_bottom_cell_alive_from(i, j) if 1 else 0
        live_cells_count += self.__get_bottom_right_cell_alive_from(i, j) if 1 else 0
        return live_cells_count

    def __get_top_left_cell_alive_from(self, i, j):
        if i - 1 < 0 or i - 1 > self.get_rows_number - 1:
            return False
        if j - 1 < 0 or j - 1 > self.get_columns_number - 1:
            return False
        return self.__get_cell_at(i - 1, j - 1)

    def __get_top_cell_alive_from(self, i, j):
        if i - 1 < 0 or i - 1 > self.get_rows_number - 1:
            return False
        return self.__get_cell_at(i - 1, j)

    def __get_top_right_cell_alive_from(self, i, j):
        if i - 1 < 0 or i - 1 > self.get_rows_number - 1:
            return False
        if j + 1 < 0 or j + 1 > self.get_columns_number - 1:
            return False
        return self.__get_cell_at(i - 1, j + 1)

    def __get_left_cell_alive_from(self, i, j):
        if j - 1 < 0 or j - 1 > self.get_columns_number - 1:
            return False
        return self.__get_cell_at(i, j - 1)

    def __get_right_cell_alive_from(self, i, j):
        if j + 1 < 0 or j + 1 > self.get_columns_number - 1:
            return False
        return self.__get_cell_at(i, j + 1)

    def __get_bottom_cell_alive_from(self, i, j):
        if i + 1 < 0 or i + 1 > self.get_rows_number - 1:
            return False
        return self.__get_cell_at(i + 1, j)

    def __get_bottom_right_cell_alive_from(self, i, j):
        if i + 1 < 0 or i + 1 > self.get_rows_number - 1:
            return False
        if j + 1 < 0 or j + 1 > self.get_columns_number - 1:
            return False
        return self.__get_cell_at(i + 1, j + 1)

    def __get_bottom_left_cell_alive_from(self, i, j):
        if i + 1 < 0 or i + 1 > self.get_rows_number - 1:
            return False
        if j - 1 < 0 or j - 1 > self.get_columns_number - 1:
            return False
        return self.__get_cell_at(i + 1, j - 1)

    def __get_cell_at(self, x, y):
        return self.__cells[x][y]

    def resize_by(self, new_size):
        old_rows, old_columns = self.get_rows_number, self.get_columns_number

        if old_rows == new_size and old_columns == new_size:
            return self.__cells

        resized_matrix = [[False for _ in range(new_size)] for _ in range(new_size)]

        row_offset = (new_size - old_rows) // 2
        col_offset = (new_size - old_columns) // 2

        for i in range(old_rows):
            for j in range(old_columns):
                resized_matrix[i + row_offset][j + col_offset] = self.__cells[i][j]

        self.__cells = resized_matrix



