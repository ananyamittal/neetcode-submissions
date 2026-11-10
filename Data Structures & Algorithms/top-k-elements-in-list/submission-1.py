class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            res[i] = 1 + res.get(i, 0)
        
        for n, c in res.items():
            freq[c].append(n)

        op = []
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                op.append(j)
            if len(op) == k:
                return op