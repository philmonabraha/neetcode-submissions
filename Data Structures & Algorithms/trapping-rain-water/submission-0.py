class Solution:
    def trap(self, height: List[int]) -> int:


        prefix = [0]*len(height)
        suffix = [0]*len(height)


        for i in range(1, len(height)):
            prefix[i] = max(height[i], prefix[i-1])
        
        suffix[len(n)-1] = height[len(n)-1]
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(height[i], suffix[i+1])


        res = 0

        for i in range(len(height)):
            res += min(suffix[i], prefix[i]) - height[i]

        return res

        