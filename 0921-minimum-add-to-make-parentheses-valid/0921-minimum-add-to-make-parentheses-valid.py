class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        c1=0
        c2=0
        for ch in s:
            if ch=="(":
                c1+=1
            else:
                if c1>0:
                    c1-=1
                else:
                    c2+=1
        return c1+c2
