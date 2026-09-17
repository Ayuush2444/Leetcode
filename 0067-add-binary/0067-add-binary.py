class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=int(a,2)
        m=int(b,2)
        s=n+m
        return bin(s)[2:]