class Solution:
    def isPalindrome(self, s: str) -> bool:
        op = self.reverse(s)
        res = ""
        for i in range(0, len(s)):
            if s[i].isalnum():
                res += s[i]

        return res.lower() == op.lower()

    def reverse(self, s):
        res = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                res += s[i]
        
        return res