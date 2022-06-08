import curses
from curses import wrapper
import queue
import time
from types import new_class

# This is the maze that I am using for this project. The algo should work on any maze.
# The next thing I would like to do in this project is randomly generate a maze and have this algo solve it 
# The thing I would like to do after that is train an AI and see how close it gets to this algo and measure if it is better or worse
maze = [
    ["#", "#", "#", "#", "#", "#", "O", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# This function prints the maze and the ongoing algo in the terminal
def print_maze(maze, stdscr, path=[]):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", red)
            else:
                stdscr.addstr(i, j*2, value, blue)

# This function finds the coordinates of the start of the maze 
def find_start(maze, start_symbol):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start_symbol:
                return i, j
    return None

# This is a breadth-first algo to find the shortest solution to a maze 
def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.4)
        stdscr.refresh()

        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

        
# This function finds and makes a list of all of the valid neighbors to a position in the maze 
def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0: #up neighbor
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): #below neighbor
        neighbors.append((row + 1, col))
    if col > 0: #left neighbor
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): #right neighbor
        neighbors.append((row, col + 1))

    return neighbors
    

# This is the main function that calls the other needed functions for this maze solver 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # blue_and_black = curses.color_pair(1)
    # red_and_black = curses.color_pair(2)
    find_path(maze, stdscr)
    stdscr.getch()

# This is the function from curses that allows all of this to work 
wrapper(main)