class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                y = stack.pop()
                x = stack.pop()
               
                if tokens[i] == '+':
                    stack.append(x+y)
                elif tokens[i] == '-':
                    stack.append(x-y)
                elif tokens[i] == '*':
                    stack.append(x * y)
                elif tokens[i] == '/':
                    stack.append(math.trunc(x/y))
    
        return (stack.pop())
