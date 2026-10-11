class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position,speed))
        for p,s in cars:
            hours = (target - p) // s
            while stack and stack[-1] <= hours:
                stack.pop()
            stack.append(hours)

        return len(stack)
        