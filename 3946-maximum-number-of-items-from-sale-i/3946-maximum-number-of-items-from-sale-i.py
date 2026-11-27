from typing import List
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        dp = [0] * (budget + 1)

        for i in range(n):
          factor_i, price_i = items[i]
          if price_i > budget:
            continue

          free_count = 0
          for j in range(n):
            if i != j and items[j][0] % factor_i == 0:
              free_count += 1

          first_copy_value = 1 + free_count
          for b in range(budget, price_i - 1, -1):
            dp[b] = max(dp[b], dp[b - price_i] + first_copy_value)
    
          for b in range(price_i, budget + 1):
            dp[b] = max(dp[b], dp[b - price_i] + 1)
        return dp[budget]