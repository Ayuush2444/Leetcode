class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):

                if r == 0 and c == 0:
                    continue

                if grid[r][c] == '(':
                    change = 1
                else:
                    change = -1

                if r > 0:
                    for balance in dp[r - 1][c]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

                if c > 0:
                    for balance in dp[r][c - 1]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

        return 0 in dp[m - 1][n - 1]