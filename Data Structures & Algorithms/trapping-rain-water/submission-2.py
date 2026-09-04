class Solution:
    def trap(self, height: List[int]) -> int:

        
        left, right = 0, len(height) - 1
        leftmax = 0
        rightmax = 0

        res = 0

        while left < right:

            if height[left] < height[right]:

                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        
        return res


        