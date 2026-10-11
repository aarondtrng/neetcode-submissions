class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        brackets = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        s = list(s)
        for i in range(len(s) // 2):
            l = s.pop(0)
            r = s.pop()
            print(l)
            print(r)
            if(brackets.get(l) != r):
                return False
        return True