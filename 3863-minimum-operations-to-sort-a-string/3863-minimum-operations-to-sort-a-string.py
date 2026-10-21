class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        has_mn_prefix = mn in s[:-1]
        has_mx_suffix = mx in s[1:]

        if not has_mn_prefix and not has_mx_suffix:
            return 3

        return 2