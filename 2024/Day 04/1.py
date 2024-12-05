from Helpers import puzzle_data_handler, test_data_handler

DIRECTIONS_LIST = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
DIRECTIONS_DICT = {"N": (-1, 0), "NE": (-1, 1), "E": (0, 1), "SE": (1, 1), "S": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, -1)}
MAS_DICT = {"M": 1, "A": 2, "S": 3}
MAS_LIST = {"M", "A", "S"}

class GridSolver():
    def __init__(self):
        grid = list()
        grid_rows = 0
        grid_cols = 0
        xmas_count = 0
    
    def set_grid(self, data):
        self.grid = data
        self.grid_rows = len(data)
        self.grid_cols = len(data[0])

    def get_letter(self, row, col):
        return self.grid[row][col]

    def check_xmas_in_direction(self, row, col, direction):
        for letter in MAS_LIST:
            letter_row = row + (MAS_DICT[letter] * DIRECTIONS_DICT[direction][0])
            letter_col = col + (MAS_DICT[letter] * DIRECTIONS_DICT[direction][1])
            if not (self.get_letter(letter_row, letter_col) == letter):
                return 0
        return 1

    def is_col_in_bounds(self, end_col):
        if (end_col < 0) or (end_col >= self.grid_cols):
            return False
        return True

    def is_row_in_bounds(self, end_row):
        if (end_row < 0) or (end_row >= self.grid_rows):
            return False
        return True

    def is_out_of_bounds(self, row, col, direction):
        end_row = row + (3 * DIRECTIONS_DICT[direction][0])
        end_col = col + (3 * DIRECTIONS_DICT[direction][1]) 
        if (not self.is_row_in_bounds(end_row)) or (not self.is_col_in_bounds(end_col)):
            return False
        return True


    def xmas_per_x(self, row, col):
        xmas_count = 0
        for direction in DIRECTIONS_LIST:
            if self.is_out_of_bounds(row, col, direction):
                xmas_count += self.check_xmas_in_direction(row, col, direction)
        return xmas_count

    def xmas_counter(self):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                if self.grid[r][c] == 'X':
                    self.xmas_count += self.xmas_per_x(r, c)

    def reset(self):
        self.xmas_count = 0

    def get_answer(self):
        self.reset()
        self.xmas_counter()
        return self.xmas_count


def solve(data):
    solver = GridSolver()
    solver.set_grid(data)
    answer = solver.get_answer()
    return answer

test_input = test_data_handler()
puzzle_input = puzzle_data_handler()

assert solve(test_input) == 18, "Not there yet"
print("Test passed! Answer should be {}".format(solve(puzzle_input)))