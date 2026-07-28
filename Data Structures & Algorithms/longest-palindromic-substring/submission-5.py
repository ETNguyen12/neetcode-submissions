class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [-1, -1]
        resLen = 0
        for i, c in enumerate(s):
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > resLen:
                        res = [l, r+1]
                        resLen = r - l + 1
                    l -= 1
                    r += 1
        return s[res[0]:res[1]]
            