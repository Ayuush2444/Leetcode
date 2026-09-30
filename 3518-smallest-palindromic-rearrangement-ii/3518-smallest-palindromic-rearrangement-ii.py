from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half_counts = {}
        mid_char = ""
        total_half_len = 0

        for char in sorted(freq.keys()):
            count = freq[char]
            if count % 2 == 1:
                mid_char = char
            half_counts[char] = count // 2
            total_half_len += count // 2

        def count_ways(cnt: dict, remaining: int) -> int:
            ans = 1
            cap = 10**6 + 1
            rem = remaining
            for char, c in cnt.items():
                for j in range(1, c + 1):
                    ans = ans * (rem - c + j) // j
                    if ans > cap:
                        return cap
                rem -= c
            return min(ans, cap)

        if count_ways(half_counts, total_half_len) < k:
            return ""

        left_half = []

        for pos in range(total_half_len):
            for char in sorted(half_counts.keys()):
                if half_counts[char] == 0:
                    continue

                half_counts[char] -= 1
                ways = count_ways(half_counts, total_half_len - pos - 1)

                if ways >= k:
                    left_half.append(char)
                    break
                else:
                    k -= ways
                    half_counts[char] += 1  

        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]
