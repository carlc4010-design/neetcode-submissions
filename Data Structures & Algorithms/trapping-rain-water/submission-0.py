class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        amount = 0
        lvl = 0
        while right >= left:
            if height[right] - lvl <= 0:
                right -= 1
            elif height[left] - lvl <= 0:
                left += 1
            else:
                k = min(height[right],height[left])-lvl
                amount += k * (right-left+1)
                lvl += k

        return amount - sum(height)


