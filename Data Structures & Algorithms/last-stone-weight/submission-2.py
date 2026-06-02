class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stone1 = stones[-1]
            stone2 = stones[-2]
            if stone1 == stone2:
                stones.pop()
                stones.pop()
            elif stone1 > stone2:
                stones[-2] = stone1 - stone2
                stones.pop()
        if stones: return stones[0]
        return 0