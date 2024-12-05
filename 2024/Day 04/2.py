from Helpers import puzzle_data_handler, test_data_handler

EAST_DIRECTIONS_LIST = ["NE", "SE"]
EAST_TO_WEST = {"NE": "SW", "SE": "NW"}
DIRECTIONS_DICT = {"NE": (-1, 1), "SE": (1, 1), "SW": (1, -1), "NW": (-1, -1)}

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

    def check_xmas(self, row, col):
        for direction in EAST_DIRECTIONS_LIST:
            other_direction = EAST_TO_WEST[direction]
            first_letter = self.get_letter(row + DIRECTIONS_DICT[direction][0], col + DIRECTIONS_DICT[direction][1])
            last_letter = self.get_letter(row + DIRECTIONS_DICT[other_direction][0], col + DIRECTIONS_DICT[other_direction][1])
            word = first_letter + 'A' + last_letter
            if not ((word == "MAS") or (word == "SAM")):
                return False
        return True

    def is_out_of_bounds(self, row, col):
        begin_row = row - 1
        end_row = row + 1
        begin_col = col - 1
        end_col = col + 1 
        if begin_row < 0 or begin_col < 0 or end_row >= self.grid_rows or end_col >= self.grid_cols:
            return False
        return True

    def is_xmas_per_a(self, row, col):
        if self.is_out_of_bounds(row, col):
            if self.check_xmas(row, col):
                return 1
        return 0

    def xmas_counter(self):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                if self.grid[r][c] == 'A':
                    self.xmas_count += self.is_xmas_per_a(r, c)

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
    print(answer)
    return answer

test_input = test_data_handler()
puzzle_input = puzzle_data_handler()

assert solve(test_input) == 9, "Not there yet"
print("Test passed! Answer should be {}".format(solve(puzzle_input)))