class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        if len(piles) == h: return maxK

        lowK = 1
        while lowK <= maxK:
            time = 0
            midK = (lowK + maxK) // 2
            for pile in piles: 
                time += math.ceil(pile / midK)
            if time > h:
                lowK = midK+1
            if time <= h: 
                res = midK
                maxK = midK -1 
        return res