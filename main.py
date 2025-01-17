from maze_generator import Maze
from maze_solver import MazeSolver

if __name__ == "__main__":
    # Generate the maze
    maze = Maze(51, 51)
    maze.grid_creation()
    maze.start_end(min_distance=15)  # Adjust the distance to the size of the maze

    print(f"Start: {maze.start}, End: {maze.end}")

    # Solve the maze with visualization
    solver = MazeSolver(maze)
    dfs_result = solver.dfs()

    # Display results
    print(f"Path found: {dfs_result['path']}")
    print(f"Cells visited: {dfs_result['cells_visited']}")
    print(f"Max frontier size: {dfs_result['max_frontier_size']}")

    # Final visualization with the full path
    maze.draw_maze(path=dfs_result['path'], visited=dfs_result['visited'])

    print()
    astar_result = solver.astar()
    print(f"Path found: {astar_result['path']}")
    print(f"Cells visited: {astar_result['cells_visited']}")
    print(f"Max frontier size: {astar_result['max_frontier_size']}")
    maze.draw_maze(path=astar_result['path'], visited=astar_result['visited'])

    print()
    bfs_result = solver.bfs()
    print(f"Path found: {bfs_result['path']}")
    print(f"Cells visited: {bfs_result['cells_visited']}")
    print(f"Max frontier size: {bfs_result['max_frontier_size']}")
    maze.draw_maze(path=bfs_result['path'], visited=bfs_result['visited'])