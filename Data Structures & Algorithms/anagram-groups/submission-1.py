class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            s = "".join(sorted(i))
            if s not in res:
                res[s] = [i]
            else:
                res[s].append(i)

        return list(res.values()) 