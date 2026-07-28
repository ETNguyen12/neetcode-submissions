class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ''
        for i, c in enumerate(s):
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    window = s[l:r+1]
                    best = window if len(window) > len(best) else best
                    l -= 1
                    r += 1
        return best
            