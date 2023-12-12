FILENAME = "input10.txt"
START = "S"
DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
CORNERS = {"J", "L", "F", "7"}


def find_start(maze: list[str]) -> tuple[int, int] or None:
    for i, row in enumerate(maze):
        for j, ele in enumerate(row):
            if ele == START:
                return i, j
    return None


def find_initial_direction(maze: list[str], start: tuple[int, int]) -> tuple[int, int] or None:
    valid = {
        (1, 0): {"|", "J", "L"},
        (0, -1): {"F", "L", "-"},
        (-1, 0): {"|", "7", "F"},
        (0, 1): {"J", "7", "-"},
    }
    for (offset_row, offset_col), valid_pipes in valid.items():
        new_row, new_col = start[0] + offset_row, start[1] + offset_col
        if (
                0 <= new_row < len(maze)
                and 0 <= new_col < len(maze[0])
                and maze[new_row][new_col] in valid_pipes
        ):
            return offset_row, offset_col
    return None


def calculate_next_direction(row_offset: int, col_offset: int, pipe: str) -> tuple[int, int]:
    mult = {"L": 1, "7": 1, "J": -1, "F": -1}
    return col_offset * mult[pipe], row_offset * mult[pipe]


def find_loop(maze: list[str], start: tuple[int, int]) -> list[tuple[int, int]]:
    dir_row, dir_col = find_initial_direction(maze, start)
    current = start
    loop = []
    while current != start or not loop:
        loop.append(current)
        row, col = current
        current = (row + dir_row, col + dir_col)
        pipe = maze[current[0]][current[1]]
        if pipe in CORNERS:
            dir_row, dir_col = calculate_next_direction(dir_row, dir_col, pipe)
    return loop


def calculate_polygon_area(coordinates: list[tuple[int, int]]) -> float:
    """Shoelace formula"""
    x, y = zip(*coordinates)
    return 0.5 * abs(
        sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(coordinates)))
    )


def part_one(loop: list[tuple[int, int]]) -> int:
    return len(loop) // 2 + len(loop) % 2


def part_two(area: float, loop_size: int) -> int:
    """Pick's theorem"""
    return int(area - 0.5 * loop_size + 1)


def main():
    with open(FILENAME, "r") as input_file:
        maze = input_file.read().split("\n")
    start = find_start(maze)
    loop = find_loop(maze, start)
    print(part_one(loop))
    area = calculate_polygon_area(loop)
    print(part_two(area, len(loop)))


if __name__ == "__main__":
    main()

