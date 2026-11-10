class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in nums:
            res[i] = 1 + res.get(i, 0)
        
        res = sorted(res, key = res.get, reverse = True)

        return res[:k]