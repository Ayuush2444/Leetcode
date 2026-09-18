class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        for ch in first:
            l = first[ch]
            r = last[ch]

            i = l

            while i <= r:
                c = s[i]

                if first[c] < l:
                    break

                r = max(r, last[c])
                i += 1

            else:
                intervals.append((l, r))
    
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r+1])
                prev_end = r

        return result