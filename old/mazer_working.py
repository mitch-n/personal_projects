import random
import os
import curses

def generate_maze(height, width):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    def random_walk(row, col):
        maze[row][col] = ' '
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < height and 0 <= new_col < width and maze[new_row][new_col] == '#':
                maze[row + dr // 2][col + dc // 2] = ' '
                maze[new_row][new_col] = ' '
                random_walk(new_row, new_col)

    start_row, start_col = 1, 1
    end_row, end_col = height - 2, width - 2
    maze[start_row][start_col] = ' '
    maze[end_row][end_col] = ' '

    # Ensure there is a clear path from start to end
    maze[start_row][start_col + 1] = ' '
    maze[end_row][end_col - 1] = ' '

    # Perform random walk to connect start and end points
    random_walk(start_row, start_col)

    return maze

def print_maze(stdscr, maze, player_pos):
    stdscr.clear()
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                stdscr.addch('@')
            elif cell == ' ':
                stdscr.addch(' ')
            else:
                stdscr.addch(cell)
        stdscr.addch('\n')
    stdscr.refresh()

def move_player(maze, player_pos, direction):
    row, col = player_pos
    if direction == curses.KEY_UP and row > 0 and maze[row - 1][col] not in ['#']:
        return row - 1, col
    elif direction == curses.KEY_DOWN and row < len(maze) - 1 and maze[row + 1][col] not in ['#']:
        return row + 1, col
    elif direction == curses.KEY_LEFT and col > 0 and maze[row][col - 1] not in ['#']:
        return row, col - 1
    elif direction == curses.KEY_RIGHT and col < len(maze[0]) - 1 and maze[row][col + 1] not in ['#']:
        return row, col + 1
    else:
        return player_pos


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    height, width = 15, 25
    start_row, start_col = 1, 1

    while True:
        maze = generate_maze(height, width)
        end_row, end_col = height - 2, width - 2
        maze[start_row][start_col] = ' '
        maze[end_row][end_col] = '!'

        player_pos = (start_row, start_col)
        print_maze(stdscr, maze, player_pos)

        while maze[player_pos[0]][player_pos[1]] != '!':
            key = stdscr.getch()
            player_pos = move_player(maze, player_pos, key)
            print_maze(stdscr, maze, player_pos)


if __name__ == "__main__":
    curses.wrapper(main)
