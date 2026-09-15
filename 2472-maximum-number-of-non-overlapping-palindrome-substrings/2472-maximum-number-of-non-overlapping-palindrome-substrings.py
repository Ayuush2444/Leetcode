class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        dp = [0] * (n + 1)

        pal = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length <= 2:
                        pal[left][right] = True
                    else:
                        pal[left][right] = pal[left + 1][right - 1]
        for i in range(n):
            dp[i + 1] = max(dp[i + 1], dp[i])

            for j in range(i + k - 1, n):
                if pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]