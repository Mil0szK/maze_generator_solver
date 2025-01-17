## Maze Generator and Solver

# Overview
This project is a maze generator and solver. The maze is generated using a recursive backtracking algorithm.
The maze is created using Prim's Algorithm. The maze is displayed using a matplotlib library.
Visualization contains start and end points, visited cells, and the path from start to end.

# Prim's Algorithm Generation
1) The grid is initialized where every cell is marked as BLOCKED (unreachable).
2) A random cell within the inner grid (avoiding edges) is selected as the starting point and marked as a PASSAGE.
3) The algorithm adds all neighboring cells of the starting cell to the frontier.
   These are potential candidates for carving into passages.
4) The algorithm iteratively selects a random cell from the frontier:
*If it can connect to an existing passage (a neighboring cell already marked as a PASSAGE),
the path between them is "carved" (the connecting wall is removed). 
*The selected cell itself is marked as a PASSAGE, and its neighbors are added to the frontier (if they are still BLOCKED).
5) The algorithm continues until the frontier is empty.
6) Start and end points are randomly selected with a minimum distance requirement chosen by the user.

# Solving the Maze
The maze can be solved using the following algorithms:
1) Depth-First Search (DFS)
2) A* Search Algorithm
3) Breadth-First Search (BFS)

# Instructions to Run
1) Clone the repository:
```bash
git clone
```
2) Install the required libraries:
```bash
pip install -r requirements.txt
```
3) Run the main.py file:
```bash
python main.py
```

# Usage
1) In main.py file, set the following parameters:
width of maze, height of maze, and minimum distance between start and end points.