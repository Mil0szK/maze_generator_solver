from maze_generator import Maze, CellState
import heapq


class MazeSolver:
    def __init__(self, maze: Maze):
        self.maze = maze

    def dfs(self):
        start, end = self.maze.start, self.maze.end
        visited = set()
        path = []
        cells_visited = 0  # Count of visited cells
        max_frontier_size = 0  # Maximum size of the stack during execution

        def dfs_recursive(cell):
            nonlocal cells_visited, max_frontier_size

            if cell in visited or cell[0] < 0 or cell[1] < 0 or cell[0] >= self.maze.width or cell[1] >= self.maze.height:
                return False
            if self.maze.grid[cell[1]][cell[0]].state == CellState.BLOCKED:
                return False
            if cell == end:
                path.append(cell)
                return True

            visited.add(cell)
            cells_visited += 1
            path.append(cell)

            neighbors = self.maze.neighbors(cell[0], cell[1])
            max_frontier_size = max(max_frontier_size, len(neighbors))

            for neighbor in neighbors:
                if dfs_recursive(neighbor):
                    return True

            # Backtrack
            path.pop()
            return False

        dfs_recursive(start)

        return {
            "path": path,
            "cells_visited": cells_visited,
            "max_frontier_size": max_frontier_size,
            "visited": list(visited),
        }

    def astar(self):
        start, end = self.maze.start, self.maze.end
        visited = set()
        came_from = {}
        cells_visited = 0
        max_frontier_size = 0

        # Heuristic function: Manhattan distance
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # Priority queue for A*
        frontier = []
        heapq.heappush(frontier, (0, start))
        g_score = {start: 0}  # Cost from start to the current node
        f_score = {start: heuristic(start, end)}  # Estimated total cost

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier))

            _, current = heapq.heappop(frontier)
            if current == end:
                # Reconstruct path
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return {
                    "path": path,
                    "cells_visited": cells_visited,
                    "max_frontier_size": max_frontier_size,
                    "visited": list(visited),
                }

            visited.add(current)
            cells_visited += 1

            for neighbor in self.maze.neighbors(current[0], current[1]):
                if neighbor in visited or self.maze.grid[neighbor[1]][neighbor[0]].state == CellState.BLOCKED:
                    continue

                tentative_g_score = g_score[current] + 1  # Assume uniform cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(frontier, (f_score[neighbor], neighbor))

        return {
            "path": [],
            "cells_visited": cells_visited,
            "max_frontier_size": max_frontier_size,
            "visited": list(visited),
        }

    def bfs(self):
        start, end = self.maze.start, self.maze.end
        visited = set()
        came_from = {}
        cells_visited = 0
        max_frontier_size = 0

        # Queue for BFS
        queue = [start]
        visited.add(start)

        while queue:
            max_frontier_size = max(max_frontier_size, len(queue))

            current = queue.pop(0)
            cells_visited += 1

            if current == end:
                # Reconstruct path
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return {
                    "path": path,
                    "cells_visited": cells_visited,
                    "max_frontier_size": max_frontier_size,
                    "visited": list(visited),
                }

            for neighbor in self.maze.neighbors(current[0], current[1]):
                if neighbor not in visited and self.maze.grid[neighbor[1]][neighbor[0]].state != CellState.BLOCKED:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)

        return {
            "path": [],
            "cells_visited": cells_visited,
            "max_frontier_size": max_frontier_size,
            "visited": list(visited),
        }
