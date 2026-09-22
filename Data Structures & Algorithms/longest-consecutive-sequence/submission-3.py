class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        if len(numsSet) == 0:
            return 0

        length = 0
        maxLength = 0
        for num in numsSet:
            if num-1 not in numsSet:
                curr = num
                length+=1
                while curr+1 in numsSet:
                    length+=1
                    curr = curr+1
                maxLength = length if length > maxLength else maxLength
                length = 0
        return maxLength