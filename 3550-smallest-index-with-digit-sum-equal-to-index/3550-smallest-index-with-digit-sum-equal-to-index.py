class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = sum(int(d) for d in str(nums[i]))
            if i==x:
                return i
        return -1