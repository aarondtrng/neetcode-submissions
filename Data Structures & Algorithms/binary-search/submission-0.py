class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        low = 0
        high = len(nums)
        while low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            elif nums[mid] > target: 
                high = mid-1
            mid = (low + high )// 2
        return -1