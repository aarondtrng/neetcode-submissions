class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        if k == len(nums): return list(max(nums))

        res = []
        currMax = nums[0]
        l=0
        for r in range(len(nums)):
            currMax = max(currMax, nums[r])
            print(nums[r-l+1:r+1])
            if (r-l+1 >= k):
                res.append(currMax)
                while(r-l+1 > k):
                    l+=1

        return res