class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=s.split()
        return len(n[-1])