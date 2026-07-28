class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        for i, c in enumerate(s):
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > resLen:
                        resIdx, resLen = l, r - l + 1
                    l -= 1
                    r += 1
        return s[resIdx:resIdx+resLen]
            