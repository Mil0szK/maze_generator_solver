import random
from dataclasses import dataclass
from enum import Enum


class CellState(Enum):
    BLOCKED = 0
    PASSAGE = 1

@dataclass
class Cell:
    x: int
    y: int
    state: CellState


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        start_end = {(1, 1): (width-2, height-2), (1, height-2): (width-2, 1), (width-2, 1): (1, height-2), (width-2, height-2): (1, 1)}
        self.start = random.choice(list(start_end.keys()))
        self.end = start_end[self.start]


    def grid_creation(self):
        self.grid = [[Cell(x, y, CellState.BLOCKED) for x in range(self.width)] for y in range(self.height)]
        # Set the start and end points
        self.grid[self.start[1]][self.start[0]].state = CellState.PASSAGE
        self.grid[self.end[1]][self.end[0]].state = CellState.PASSAGE

if __name__ == "__main__":
    maze = Maze(10, 10)
    print(maze.start, maze.end)
    print(maze.grid)