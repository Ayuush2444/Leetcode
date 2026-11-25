from collections import Counter
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base1, mod1 = 1315423911, 10**9 + 7
        base2, mod2 = 2654435761, 10**9 + 9
    
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
    
        for i, x in enumerate(nums):
            val = x + 1_000_000_007
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + val) % mod1
            pref2[i + 1] = (pref2[i] * base2 + val) % mod2
    
        def get_hash(l: int, r: int) -> tuple[int, int]:
            length = r - l
            h1 = (pref1[r] - pref1[l] * pow1[length]) % mod1
            h2 = (pref2[r] - pref2[l] * pow2[length]) % mod2
            return (h1, h2)
    
        def has_unique_of_len(length: int) -> bool:
            counts = Counter(get_hash(i, i + length) for i in range(n - length + 1))
            return any(cnt == 1 for cnt in counts.values())
    
        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
    