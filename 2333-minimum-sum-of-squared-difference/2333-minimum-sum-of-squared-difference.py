class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)

        n = len(diff)

        diff.append(0)

        for i in range(n):
            count = i + 1
            cost = (diff[i] - diff[i + 1]) * count

            if k >= cost:
                k -= cost

            else:
                q, r = divmod(k, count)

                level = diff[i] - q
                for j in range(r):
                    diff[j] = level - 1

                for j in range(r, count):
                    diff[j] = level

                k = 0
                break

        return sum(x * x for x in diff[:n])