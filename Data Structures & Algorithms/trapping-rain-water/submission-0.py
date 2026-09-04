class Solution:
    def trap(self, height: List[int]) -> int:

        left = [0] * len(height)
        right = [0] * len(height)

        for i in range(1, len(height)):
            left[i] = max(height[i-1], left[i-1])

        for i in range(0, len(height)- 2, -1):
            right[i] = max(height[i+1], right[i+1])

        res = 0

        for i in range(len(height)):

            water = min(left[i], right[i]) - height[i]
            if water >0:
                res += water
        
        return res


        