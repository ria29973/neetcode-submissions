class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0
        leftMax = height[0]
        rightMax = height[len(height)-1]
        while left <= right:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[left])
                res+= leftMax -height[left]
                left+=1
            else:
                rightMax = max(rightMax, height[right])
                res+= rightMax - height[right]
                right-=1
        return res
        