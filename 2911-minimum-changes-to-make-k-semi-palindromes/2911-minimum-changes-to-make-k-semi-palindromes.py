class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        divisors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)

        cost = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            for length in range(2, n - i + 1):
                best = float('inf')

                for d in divisors[length]:
                    changes = 0

                    for r in range(d):
                        left = r
                        right = r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[i + left] != s[i + right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][i + length - 1] = best

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
