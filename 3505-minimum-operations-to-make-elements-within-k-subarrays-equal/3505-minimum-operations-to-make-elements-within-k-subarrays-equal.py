from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        minOps = self.getMinOps(nums, x)

        n = len(nums)
        INF = float('inf')

        mem = [[-1] * (k + 1) for _ in range(n + 1)]

        def dp(i, k):
            if k == 0:
                return 0

            if i == n:
                return INF

            if mem[i][k] != -1:
                return mem[i][k]

            # Skip current index
            skip = dp(i + 1, k)

            # Pick current window
            pick = INF

            if i + x <= n:
                pick = minOps[i] + dp(i + x, k - 1)

            mem[i][k] = min(skip, pick)

            return mem[i][k]

        return dp(0, k)

    def getMinOps(self, nums, x):

        minOps = []

        lower = SortedList()
        upper = SortedList()

        lowerSum = 0
        upperSum = 0

        for i in range(len(nums)):

            num = nums[i]

            # Insert element
            if not lower or num <= lower[-1]:
                lower.add(num)
                lowerSum += num
            else:
                upper.add(num)
                upperSum += num

            # Remove outgoing element
            if i >= x:
                outNum = nums[i - x]

                if outNum in lower:
                    lower.remove(outNum)
                    lowerSum -= outNum
                else:
                    upper.remove(outNum)
                    upperSum -= outNum

            # Balance both halves
            if len(lower) < len(upper):
                val = upper.pop(0)
                lower.add(val)

                upperSum -= val
                lowerSum += val

            elif len(lower) - len(upper) > 1:
                val = lower.pop()

                upper.add(val)

                lowerSum -= val
                upperSum += val

            # Calculate window cost
            if i >= x - 1:

                median = lower[-1]

                ops = (
                    median * len(lower) - lowerSum
                    + upperSum - median * len(upper)
                )

                minOps.append(ops)

        return minOps
