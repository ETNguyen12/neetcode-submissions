class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]  * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                j = s.pop()
                res[j] = i - j
            s.append(i)
        return res