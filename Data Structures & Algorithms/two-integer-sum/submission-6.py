class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in Map:
                return [Map[diff], i]
            Map[num] = i