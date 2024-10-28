import random
import curses

def main(stdscr):
    # Set up the game window
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Set up the player
    player_y = 0
    player_x = 1
    player_size = 1

    # Set up the walls
    walls = [
        (2, 1, 1, 1),
        (2, 3, 1, 1),
        (4, 1, 1, 1),
        (4, 3, 1, 1),
    ]

    while True:
        # Clear the screen
        stdscr.clear()

        # Draw the player
        stdscr.addch(player_y, player_x, 'P')

        # Draw the walls
        for wall in walls:
            stdscr.addch(wall[0], wall[1], '#')

        # Move the player
        move = stdscr.getch()
        if move == curses.KEY_UP:
            if player_y > 0:
                player_y -= 1
        elif move == curses.KEY_DOWN:
            if player_y < 8:
                player_y += 1
        elif move == curses.KEY_LEFT:
            if player_x > 0:
                player_x -= 1
        elif move == curses.KEY_RIGHT:
            if player_x < 17:
                player_x += 1

        # Check for collision
        for wall in walls:
            if player_y == wall[0] and player_x == wall[1]:
                break
        else:
            for wall in walls:
                if player_y == wall[2] and player_x == wall[3]:
                    break
            else:
                # Check if player is out of the screen
                if player_x < 0 or player_x > 17 or player_y < 0 or player_y > 8:
                    break

                # Generate a new wall
                new_wall = (
                    random.randint(0, 8),
                    random.randint(0, 17),
                    random.randint(0, 8),
                    random.randint(0, 17),
                )

                # Check if the new wall is overlapping with another wall
                if not (
                    wall[0] == new_wall[0]
                    and wall[1] == new_wall[1]
                    and wall[2] == new_wall[2]
                    and wall[3] == new_wall[3]
                    for wall in walls
                ):
                    walls.append(new_wall)

    # Game over
    stdscr.addstr(10, 8, "Game Over")
    stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
