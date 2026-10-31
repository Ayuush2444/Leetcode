class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def move(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                if dr == 0:  
                    dr, dc = 1, 0
                else:        
                    dr, dc = 0, 1

                r += dr
                c += dc

            if 0 <= r < m and 0 <= c < n:
                return r, c

            return -1, -1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                if j + 1 < n:
                    r, c = move(i, j + 1, 0, 1)
                    if r != -1:
                        dp[r][c] = (dp[r][c] + dp[i][j]) % MOD

                if i + 1 < m:
                    r, c = move(i + 1, j, 1, 0)
                    if r != -1:
                        dp[r][c] = (dp[r][c] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]