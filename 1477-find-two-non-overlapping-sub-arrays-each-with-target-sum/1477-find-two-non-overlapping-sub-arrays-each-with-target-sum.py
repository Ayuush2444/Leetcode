class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        best = [INF] * (n + 1)
        prefix_map = {0: -1}

        prefix = 0
        ans = INF

        for i in range(n):
            prefix += arr[i]

            best[i + 1] = best[i]

            if prefix - target in prefix_map:
                start = prefix_map[prefix - target]
                length = i - start

                if best[start + 1] != INF:
                    ans = min(ans, length + best[start + 1])

                best[i + 1] = min(best[i + 1], length)

            prefix_map[prefix] = i

        return -1 if ans == INF else ans