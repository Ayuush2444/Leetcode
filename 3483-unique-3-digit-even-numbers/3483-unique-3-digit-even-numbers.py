from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        freq = Counter(digits)
        count = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            s = str(num)
            num_freq = Counter(map(int, s))

            valid = True

            for digit in num_freq:
                if num_freq[digit] > freq[digit]:
                    valid = False
                    break

            if valid:
                count += 1

        return count