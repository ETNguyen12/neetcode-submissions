class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ''
        n = len(s)
        for left in range(n):
            right = left
            while right < n:
                substring = s[left:right+1]
                if substring == substring[::-1] and len(best) < len(substring):
                    best = substring
                right += 1
        return best 