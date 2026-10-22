class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        p = nums.index(0)

        increasing = all(
            nums[(p + i) % n] == i
            for i in range(n)
        )

        if increasing:
            return min(p, n - p + 2)

        decreasing = all(
            nums[(p - i) % n] == i
            for i in range(n)
        )

        if decreasing:
            return min(n - p, p + 2)

        return -1