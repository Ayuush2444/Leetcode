class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if all(nums[i] == i for i in range(n)):
            return 0

        ans = (1 << 31) - 1

        for i, x in enumerate(nums):
            if x != i:
                ans &= x

        return ans