from collections import defaultdict
from typing import List
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = defaultdict(int)
        max_len = 0

        for num in nums:
          dp[num + 1] = dp[num] + 1

          dp[num] = dp[num - 1] + 1

          max_len = max(max_len, dp[num], dp[num + 1])

        return max_len