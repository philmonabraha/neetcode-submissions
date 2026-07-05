class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        area = []

        for i in heights:

            counter = 1

            x = i - 1
            y = i + 1

            while x >= 0 and heights[x] >= heights[i]:
                counter += 1
                x -= 1

            while y < len(heights) and heights[y] >= heights[i]:
                counter += 1
                y += 1

            a = counter * heights[i]
            area.append(a)

        return max(area)
            





        