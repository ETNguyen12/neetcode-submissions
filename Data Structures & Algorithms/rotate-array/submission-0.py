class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_locations = {}
        for i, n in enumerate(nums):
            new_locations[n] = (i+k) % len(nums)
        
        for n, i in new_locations.items():
            nums[i] = n
