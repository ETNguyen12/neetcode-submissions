class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0
        while l < r:
            leftHeight = heights[l]
            rightHeight = heights[r]

            height = min(leftHeight, rightHeight)
            width = r - l
            area = max(height * width, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return area