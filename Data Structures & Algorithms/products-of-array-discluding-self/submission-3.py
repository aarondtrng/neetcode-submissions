class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums) 
        s = [1] * len(nums) 
        prod = 1

        for i in range(len(nums)):
            p[i] = prod
            prod*=nums[i]
        

        
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            s[i] = prod
            prod*=nums[i]


        return [a * b for a, b in zip(p, s)]