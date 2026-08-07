class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #height, index
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                width = i - index
                maxArea = max(maxArea, height * width)
                start = index
            stack.append((h,start))
        for height, index in stack:
            maxArea = max(maxArea, height * (len(heights)-index))
        return maxArea

                
     
                
                




        