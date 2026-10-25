from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [
            (1, 0),
            (-1, 0),  
            (0, 1),   
            (0, -1)   
        ]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            closed = True

            while queue:
                row, col = queue.popleft()

                if (row == 0 or row == rows - 1 or
                    col == 0 or col == cols - 1):
                    closed = False

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 0 and
                        (nr, nc) not in visited):

                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return closed

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    if bfs(r, c):
                        count += 1

        return count