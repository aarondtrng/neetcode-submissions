class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum,val)
        if self.minStack and val <= self.minStack[-1]:
            self.minStack.append(val)
        elif not self.minStack:
            self.minStack.append(val)
       

    def pop(self) -> None:
        if self.stack:
            temp = self.stack[-1]
            del self.stack[-1]
            if temp == self.minimum:
                del self.minStack[-1]
                if self.minStack:
                    self.minimum = self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum