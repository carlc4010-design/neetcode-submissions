class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        amount = min(heights[left],heights[right])* (right - left)
        while right > left:
            if heights[right] < heights[left]:
                amount = max(amount, heights[right]*(right-left))
                right -= 1
            elif heights[left] <= heights[right]:
                amount = max(amount, heights[left]*(right - left))
                left+= 1
   
        return amount
            