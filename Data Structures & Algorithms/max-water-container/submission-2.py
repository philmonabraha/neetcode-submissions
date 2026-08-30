class Solution:
    def maxArea(self, heights: List[int]) -> int:


        left, right = 0, len(heights) - 1
        maxsofar = 0
        
        while left < right:

            current = min(height[left], height[right]) * right - left
            maxsofar = max(maxsofar, current)

            if height[left] < right[right]:
                left += 1
            else:
                right -= 1

        return maxsofar
            

        