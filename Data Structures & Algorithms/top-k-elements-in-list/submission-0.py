class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        l = [0] * k
        for num in nums:
            d[num] += 1
            for i in range(k):
                if d[num] > l[i] and num not in l:
                    l[i] = num
        print(l)
        return l