class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        p = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in p.values():
                stack.append(i)
            else:
                if not stack or stack[-1] != p[i]:
                    return False
                stack.pop()
    
        return len(stack) == 0