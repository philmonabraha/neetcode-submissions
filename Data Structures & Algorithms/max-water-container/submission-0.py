class Solution:
    def maxArea(self, heights: List[int]) -> int:


        left = 0
        right = len(heights) - 1

        maxsofar = 0

        while left < right:

            height = min(height[left], height[right]) * (right - left)
            
            if height > maxsofar:
                maxsofar = height

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return maxsofar

        