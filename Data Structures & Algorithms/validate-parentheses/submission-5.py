class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        added = 0
        for i in range(len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
                added =+1
            elif stack and stack.pop() != brackets.get(s[i]):
                return False
        
        return added != 0 and not stack