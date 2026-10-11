class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0

        for i in range(len(position)):
            fleet = int((target - position[i]) / speed[i])
            stack.append(fleet)
        return len(set(stack))
