import pytest
from maze_generator.maze_generator import Maze, CellState


def test_maze_start_and_end():
    width, height = 10, 10
    maze = Maze(width, height)

    valid_positions = {(1, 1): (width - 2, height - 2), (1, height - 2): (width - 2, 1),
                       (width - 2, 1): (1, height - 2), (width - 2, height - 2): (1, 1)}

    assert maze.start in valid_positions, f"Start point {maze.start} is not valid."
    assert maze.end == valid_positions[
        maze.start], f"End point {maze.end} does not match the expected position for start {maze.start}."


def test_grid_creation():
    width, height = 10, 10
    maze = Maze(width, height)
    maze.grid_creation()

    # Check that the grid has the correct dimensions
    assert len(maze.grid) == height, f"Grid height should be {height}, but got {len(maze.grid)}."
    assert len(maze.grid[0]) == width, f"Grid width should be {width}, but got {len(maze.grid[0])}."

    # Verify all cells are initially BLOCKED except start and end
    for y in range(height):
        for x in range(width):
            cell = maze.grid[y][x]
            if (x, y) == maze.start:
                assert cell.state == CellState.PASSAGE, f"Start cell at {maze.start} should be PASSAGE."
            elif (x, y) == maze.end:
                assert cell.state == CellState.PASSAGE, f"End cell at {maze.end} should be PASSAGE."
            else:
                assert cell.state == CellState.BLOCKED, f"Cell at {(x, y)} should be BLOCKED."

    # Check start and end points are different
    assert maze.start != maze.end, "Start and end points should not be the same."


def test_neighbours():
    width, height = 10, 10
    maze = Maze(width, height)
    maze.grid_creation()

    assert maze.neighbors(3, 3) == [(3, 2), (3, 4), (2, 3), (4, 3)], "Incorrect neighbours for cell (3, 3)."

if __name__ == "__main__":
    pytest.main()