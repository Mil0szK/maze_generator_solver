import random
from dataclasses import dataclass
from enum import Enum
import matplotlib.pyplot as plt
import math


class CellState(Enum):
    BLOCKED = 0
    PASSAGE = 1

@dataclass
class Cell:
    x: int
    y: int
    state: CellState


class Maze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y, CellState.BLOCKED) for x in range(self.width)] for y in range(self.height)]
        self.start = None
        self.end = None

    def grid_creation(self):

        initial = (random.randint(1, self.width - 2), random.randint(1, self.height - 2))
        self.grid[initial[1]][initial[0]].state = CellState.PASSAGE

        # Initialize the frontier with neighbors of the starting cell
        frontier = self.neighbors(*initial, step=2)
        while frontier:
            # Randomly select a cell from the frontier
            current = random.choice(frontier)
            frontier.remove(current)

            if current[0] == 0 or current[0] == self.width - 1 or current[1] == 0 or current[1] == self.height - 1:
                continue

            # Check for neighbors that are passages (to connect a path)
            passage_neighbors = [
                n for n in self.neighbors(*current, step=2)
                if self.grid[n[1]][n[0]].state == CellState.PASSAGE
            ]
            if passage_neighbors:
                # Connect the current cell to one of the passage neighbors
                chosen_neighbor = random.choice(passage_neighbors)
                self.carve_path(current, chosen_neighbor)

                # Add the current cell to the grid as a passage
                self.grid[current[1]][current[0]].state = CellState.PASSAGE

                # Add the neighbors of the current cell to the frontier
                for neighbor in self.neighbors(*current, step=2):
                    if (
                        1 <= neighbor[0] < self.width - 1 and
                        1 <= neighbor[1] < self.height - 1 and
                        self.grid[neighbor[1]][neighbor[0]].state == CellState.BLOCKED and
                        neighbor not in frontier
                    ):
                        frontier.append(neighbor)

    def start_end(self, min_distance = 15):
        edges_passages = []

        # Loop through the grid to find edge passages
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].state == CellState.PASSAGE:
                    if (x == 0 or x == self.width - 1 or
                            y == 0 or y == self.height - 1 or
                            x > 0 and self.grid[y][x - 1].state != CellState.PASSAGE or
                            x < self.width - 1 and self.grid[y][x + 1].state != CellState.PASSAGE or
                            y > 0 and self.grid[y - 1][x].state != CellState.PASSAGE or
                            y < self.height - 1 and self.grid[y + 1][x].state != CellState.PASSAGE):
                        edges_passages.append((x, y))

        print(edges_passages)

        if len(edges_passages) >= 2:
            valid_pair_found = False
            attempts = 0
            max_attempts = 100

            while not valid_pair_found and attempts < max_attempts:
                start, end = random.sample(edges_passages, 2)
                distance = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)

                if distance >= min_distance:
                    valid_pair_found = True
                    self.start, self.end = start, end
                attempts += 1

            # If no valid pair found within max_attempts, set to None
            if not valid_pair_found:
                self.start, self.end = None, None
        else:
            self.start, self.end = None, None

    def neighbors(self, x, y, step=1):
        directions = [(0, -step), (0, step), (-step, 0), (step, 0)]
        return [
            (x + dx, y + dy)
            for dx, dy in directions
            if 0 <= x + dx < self.width and 0 <= y + dy < self.height
        ]

    def carve_path(self, cell1, cell2):
        x1, y1 = cell1
        x2, y2 = cell2
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        self.grid[mid_y][mid_x].state = CellState.PASSAGE

    def display_grid(self):
        for row in self.grid:
            print("".join(" " if cell.state == CellState.PASSAGE else "#" for cell in row))

    def draw_maze(self, path=None, visited=None):
        # Create a grid for visualization
        maze_array = [[cell.state.value for cell in row] for row in self.grid]

        fig, ax = plt.subplots(figsize=(10, 10))

        # Display the maze using a binary colormap
        ax.imshow(maze_array, cmap=plt.cm.binary.reversed(), interpolation='nearest')

        # Highlight visited cells in yellow
        visited_label_added = False
        if visited is not None:
            for cell in visited:
                ax.scatter(cell[0], cell[1], color='yellow', s=50,
                           label="Visited" if not visited_label_added else None)
                visited_label_added = True

        # Highlight the start and end points
        if self.start:
            ax.scatter(self.start[0], self.start[1], color='green', s=100, label="Start")
        if self.end:
            ax.scatter(self.end[0], self.end[1], color='blue', s=100, label="End")

        # Plot the solution path if provided
        if path is not None:
            x_coords = [x[0] for x in path]
            y_coords = [x[1] for x in path]
            ax.plot(x_coords, y_coords, color='red', linewidth=2, label="Path")

        ax.set_xticks([])
        ax.set_yticks([])
        ax.legend(loc='upper right')
        plt.show()

