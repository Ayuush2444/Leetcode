class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]
        prefix = [[0] * (k + 1) for _ in range(n)]

        # Zero segments = 1 way for every prefix
        for i in range(n):
            dp[i][0] = 1
            prefix[i][0] = i + 1

        for i in range(1, n):
            for j in range(1, k + 1):

                # Don't use point i
                dp[i][j] = dp[i - 1][j]

                # Add a segment ending at i
                if i >= 1:
                    dp[i][j] += prefix[i - 1][j - 1]

                dp[i][j] %= MOD

                # Update prefix sum
                prefix[i][j] = prefix[i - 1][j] + dp[i][j]
                prefix[i][j] %= MOD

        return dp[n - 1][k]