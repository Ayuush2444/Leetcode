class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        LOG = n.bit_length()

        up = [[n] * n for _ in range(LOG)]
        sm = [[0] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]
            sm[0][i] = nums[i] * (nxt[i] - i)

        for j in range(1, LOG):
            for i in range(n):
                mid = up[j - 1][i]

                if mid < n:
                    up[j][i] = up[j - 1][mid]
                    sm[j][i] = sm[j - 1][i] + sm[j - 1][mid]
                else:
                    sm[j][i] = sm[j - 1][i]

        def get_max_sum(l, r):
            x = l
            total = 0

            for j in range(LOG - 1, -1, -1):
                nxt_pos = up[j][x]

                if nxt_pos <= r:
                    total += sm[j][x]
                    x = nxt_pos

            total += nums[x] * (r - x + 1)

            return total

        def operations(l, r):
            return get_max_sum(l, r) - (pref[r + 1] - pref[l])

        ans = 0
        r = -1

        for l in range(n):
            if r < l:
                r = l - 1

            while r + 1 < n and operations(l, r + 1) <= k:
                r += 1

            ans += r - l + 1

        return ans