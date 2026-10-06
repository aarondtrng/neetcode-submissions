class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
            elif not stack or stack.pop() != brackets.get(s[i]):
                return False
        return True if not stack else False