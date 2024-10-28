import random
import curses
import time
from collections import deque

# Symbols
WALL = '█'
PLAYER = '@'
EXIT = '!'
ENEMY = 'M'

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

def print_maze(stdscr, maze, player_pos, enemies_pos, maze_count, player_hidden=False):
	stdscr.clear()
	for i, row in enumerate(maze):
		for j, cell in enumerate(row):
			if (i, j) == player_pos:
				stdscr.addch(PLAYER)
			elif (i, j) in enemies_pos:
				stdscr.addch(ENEMY)
			elif cell == ' ':
				stdscr.addch(' ')
			elif cell == EXIT:
				stdscr.addch(EXIT)
			else:
				stdscr.addch(cell)
		stdscr.addch('\n')

	stdscr.addstr(f"Mazes Completed: {maze_count}")
	stdscr.addstr(f" | Press 'P' to Panic")
	stdscr.addstr(f" | Hidden: {player_hidden}")
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

def bfs(maze, start_pos, end_pos):
	queue = deque([start_pos])
	visited = set([start_pos])
	parent = {}

	while queue:
		current_pos = queue.popleft()
		if current_pos == end_pos:
			path = []
			while current_pos != start_pos:
				path.append(current_pos)
				current_pos = parent[current_pos]
			return path[::-1]  # Reverse path to get from start to end
		row, col = current_pos
		neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
		for neighbor in neighbors:
			if neighbor not in visited and maze[neighbor[0]][neighbor[1]] != WALL:
				queue.append(neighbor)
				visited.add(neighbor)
				parent[neighbor] = current_pos

def move_enemies(maze, enemies_pos, player_pos, player_hidden):
	new_enemies_pos = []
	for enemy_pos in enemies_pos:
		if player_hidden:
			moved = False
			while not moved:
				random_move = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
				new_row = enemy_pos[0] + random_move[0]
				new_col = enemy_pos[1] + random_move[1]
				if maze[new_row][new_col] != WALL:
					new_enemies_pos.append((new_row, new_col))
					moved = True
				else:
					new_enemies_pos.append(enemy_pos)
		else:
			path = bfs(maze, enemy_pos, player_pos)
			if path:
				new_enemies_pos.append(path[0])
			else:
				new_enemies_pos.append(enemy_pos)
	return new_enemies_pos

def main(stdscr, num_enemies=1, enemy_speed=0.5, maze_height=15, maze_width=25):
	curses.curs_set(0)
	stdscr.nodelay(1)

	maze_count = 0
	last_player_move_time = time.time()  # Track the last move time of the player
	last_enemy_move_times = [time.time() for _ in range(num_enemies)]  # Track the last move time of each enemy

	while True:
		start_row = random.randint(1, maze_height - 2)
		start_col = random.randint(1, maze_width - 2)
		end_row = random.randint(1, maze_height - 2)
		end_col = random.randint(1, maze_width - 2)
		enemies_pos = [(random.randint(1, maze_height - 2), random.randint(1, maze_width - 2)) for _ in range(num_enemies)]

		maze = generate_maze(maze_height, maze_width, start_row, start_col, end_row, end_col)
		time_differential = 0

		player_pos = (start_row, start_col)
		print_maze(stdscr, maze, player_pos, enemies_pos, maze_count)

		panic = False
		while maze[player_pos[0]][player_pos[1]] != EXIT:
			current_time = time.time()
			
			key = stdscr.getch()

			# Calculate time difference for player
			if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
				last_player_move_time = time.time()
				
			# Determine if the player is hidden
			time_differential = current_time - last_player_move_time
			player_hidden = time_differential > 3

			# Calculate time difference for enemies
			for i, enemy_pos in enumerate(enemies_pos):
				if current_time - last_enemy_move_times[i] >= enemy_speed:
					# Move the enemy and update its last move time
					new_enemy_pos = move_enemies(maze, [enemy_pos], player_pos, player_hidden)[0]
					enemies_pos[i] = new_enemy_pos  # Update enemy position
					last_enemy_move_times[i] = current_time

			# Check if the player is hidden or if it's time for the enemies to move
			#if player_hidden or current_time - last_player_move_time >= enemy_speed:
				#enemies_pos = move_enemies(maze, enemies_pos, player_pos, player_hidden)
				#last_player_move_time = current_time

			if key == ord('p') or key == ord('P'):  # Regenerate maze if 'P' is pressed
				panic = True
				break
			player_pos = move_player(maze, player_pos, key)
			print_maze(stdscr, maze, player_pos, enemies_pos, maze_count, player_hidden)

			if player_pos in enemies_pos:
				panic = True
				break

		if not panic:
			maze_count += 1
			#maze_height += 10
			#maze_width += 10

if __name__ == "__main__":
	num_enemies = 2  # Adjust the number of enemies
	enemy_speed = .3  # Adjust the speed of enemies (in seconds)
	maze_height = 25  # Adjust the height of the maze
	maze_width = 75  # Adjust the width of the maze
	curses.wrapper(main, num_enemies, enemy_speed, maze_height, maze_width)
