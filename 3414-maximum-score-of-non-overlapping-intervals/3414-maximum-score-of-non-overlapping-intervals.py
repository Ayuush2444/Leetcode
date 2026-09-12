from bisect import bisect_left
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: x[1]
        )
    
        ends = [x[1] for x in arr]
    
        prev = []
    
        for i in range(n):
            l = arr[i][0]
    
            pos = bisect_left(ends, l, hi=i)
            prev.append(pos - 1)
    
    
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            l, r, w, original_index = arr[i - 1]
    
            for k in range(1, 5):
                skip = dp[i - 1][k]
                p = prev[i - 1] + 1
    
                take_score = dp[p][k - 1][0] + w
                take_indices = tuple(sorted(
                    dp[p][k - 1][1] + (original_index,)
                ))
    
                take = (take_score, take_indices)
    
                if take[0] > skip[0]:
                    dp[i][k] = take
                elif take[0] < skip[0]:
                    dp[i][k] = skip
                else:
                    dp[i][k] = min(take, skip, key=lambda x: x[1])
    
        return list(dp[n][4][1])