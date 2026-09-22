class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        min_until = []
        maximum = 0
        
        for i in range(len(heights)):

            left = i-1
            right = i + 1

            while left >=0 and heights[left] >= heights[i]:
                left -= 1
            while right < len(heights) and heights[right] >= heights[i]:
                right += 1

            curr = (right - left - 1) * heights[i]
            maximum = max(maximum, curr)

        return maximum

            



        