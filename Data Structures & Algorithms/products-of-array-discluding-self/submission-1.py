class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums) 
        s = [1] * len(nums) 
        

        for i in range(len(nums)):
            j = 0
            prod = 1
            while(j < i):
                prod*=nums[j]
                j+=1
            p[i] = prod
        
        for i in range(len(nums)):
            j = i+1
            prod = 1
            while(j < len(nums)):
                prod*=nums[j]
                j+=1
            s[i] = prod

        print(p)
        print(s)
        return [a * b for a, b in zip(p, s)]