class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start < end:
            middle = start + ((end - start) // 2)
            if nums[middle] >= target: end = middle
            else: start = middle + 1
        return start if nums[start] == target else -1