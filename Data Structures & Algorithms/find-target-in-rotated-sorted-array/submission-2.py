class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high) // 2
            li = [low,mid,high]
            for i in li:
                if target == nums[i]: return i

            if nums[high] < nums[low]:
                if nums[mid] < nums[high]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                high = mid-1
        return -1