class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        if len(piles) == h: return maxK
        minK = 0
        lowK = 1
        while lowK <= maxK:
            time = 0
            midK = (lowK + maxK) // 2
            print(midK)
            for pile in piles: 
                time += math.ceil(pile / midK)
            if time >= h:
                lowK = midK+1
            if time <= h: 
                maxK = midK -1 
            minK = max(minK,midK)
        return minK