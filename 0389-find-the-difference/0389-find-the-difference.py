class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans=0
        for i in t + s:
            ans^=ord(i)
        return chr(ans)