class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        numsSet = sorted(list(numsSet))
        if len(numsSet) == 1:
            return 1

        length = 0
        maxLength = 0
        for i in range(1,len(numsSet)):
            if numsSet[i]-1 == numsSet[i-1]:
                j = i
                length+=1
                while j < len(numsSet) and numsSet[j]-1 == numsSet[j-1]:
                    length+=1
                    j+=1
                maxLength = length if length > maxLength else maxLength
                length = 0


        return maxLength