class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                y = int(stack.pop(1))
                x = int(stack.pop(0))
               
                if tokens[i] == '+':
                    stack.append(x+y)
                elif tokens[i] == '-':
                    stack.append(x-y)
                elif tokens[i] == '*':
                    stack.append(x * y)
                elif tokens[i] == '/':
                    stack.append(x//y)
            print(stack)
        return stack.pop()
