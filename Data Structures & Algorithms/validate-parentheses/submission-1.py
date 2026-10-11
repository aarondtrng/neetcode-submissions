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
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif stack.pop() != brackets.get(s[i]):
                return False
            
        return True