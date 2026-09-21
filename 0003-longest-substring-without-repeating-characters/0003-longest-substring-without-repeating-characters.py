class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        w=set()
        ans=0
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l+=1
            w.add(s[r])
            ans=max(ans,r-l+1)
        return ans