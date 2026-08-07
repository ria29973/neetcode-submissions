class Solution:
    def trap(self, height: List[int]) -> int:
        maxWater = 0
        l, leftMax = 0, height[0]
        r, rightMax = len(height)-1, height[-1]
        res = 0
        while l<r:
            if leftMax < rightMax:
                l +=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res+= rightMax - height[r]
        return res
            
        