from typing import List 
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {value: i for i, value in enumerate(arr)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps