import random
import curses

# Symbols
WALL = '█'
PLAYER = '@'
EXIT = '!'

def generate_maze(height, width, start_row, start_col, end_row, end_col):
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    def random_walk(row, col):
        maze[row][col] = ' '
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 < new_row < height-1 and 0 < new_col < width-1 and maze[new_row][new_col] == WALL:
                maze[row + dr // 2][col + dc // 2] = ' '
                maze[new_row][new_col] = ' '
                random_walk(new_row, new_col)

    # Set the perimeter of the maze as walls
    for i in range(1, width - 1):
        maze[0][i] = WALL
        maze[height - 1][i] = WALL
    for j in range(1, height - 1):
        maze[j][0] = WALL
        maze[j][width - 1] = WALL

    maze[start_row][start_col] = ' '
    maze[end_row][end_col] = EXIT

    # Ensure there is a clear path from start to end
    maze[start_row][start_col + 1] = ' '
    maze[end_row][end_col - 1] = ' '

    # Perform random walk to connect start and end points
    random_walk(start_row, start_col)

    return maze

def print_maze(stdscr, maze, player_pos, maze_count):
    stdscr.clear()
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                stdscr.addch(PLAYER)
            elif cell == ' ':
                stdscr.addch(' ')
            elif cell == EXIT:
                stdscr.addch(EXIT)
            else:
                stdscr.addch(cell)
        stdscr.addch('\n')

    stdscr.addstr(f"Mazes Completed: {maze_count}")
    stdscr.addstr(f" | Press 'R' to regenerate maze")
    stdscr.refresh()

def move_player(maze, player_pos, direction):
    row, col = player_pos
    if direction == curses.KEY_UP and row > 0 and maze[row - 1][col] not in [WALL]:
        return row - 1, col
    elif direction == curses.KEY_DOWN and row < len(maze) - 1 and maze[row + 1][col] not in [WALL]:
        return row + 1, col
    elif direction == curses.KEY_LEFT and col > 0 and maze[row][col - 1] not in [WALL]:
        return row, col - 1
    elif direction == curses.KEY_RIGHT and col < len(maze[0]) - 1 and maze[row][col + 1] not in [WALL]:
        return row, col + 1
    else:
        return player_pos

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    #height, width = 15, 25
    height, width = 20,50
    maze_count = 0

    while True:
        start_row = random.randint(1, height - 2)
        start_col = random.randint(1, width - 2)
        end_row = random.randint(1, height - 2)
        end_col = random.randint(1, width - 2)

        maze = generate_maze(height, width, start_row, start_col, end_row, end_col)

        player_pos = (start_row, start_col)
        print_maze(stdscr, maze, player_pos, maze_count)

        while maze[player_pos[0]][player_pos[1]] != EXIT:
            key = stdscr.getch()
            if key == ord('r') or key == ord('R'):  # Regenerate maze if 'R' is pressed
                break
            player_pos = move_player(maze, player_pos, key)
            print_maze(stdscr, maze, player_pos, maze_count)

        maze_count += 1

if __name__ == "__main__":
    curses.wrapper(main)
