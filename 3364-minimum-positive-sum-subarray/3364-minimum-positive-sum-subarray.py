from sortedcontainers import SortedList
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        window = SortedList()
        ans = float('inf')

        for j in range(l, n + 1):

            window.add(prefix[j - l])

            if j - r - 1 >= 0:
                window.remove(prefix[j - r - 1])

            idx = window.bisect_left(prefix[j])

            if idx > 0:
                candidate = prefix[j] - window[idx - 1]
                ans = min(ans, candidate)

        return ans if ans != float('inf') else -1