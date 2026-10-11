class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i,num in enumerate(nums):
            for j,num2 in enumerate(nums[i:]):
                if(num + num2) == target:
                    return [i,j]