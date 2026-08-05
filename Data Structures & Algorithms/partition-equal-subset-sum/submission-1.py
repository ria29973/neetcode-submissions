class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total/2
        curSum = 0
        def recurse(curSum, i):
            if i>=len(nums):
                return False
            if curSum > target:
                return False
            if curSum == target:
                return True
            return recurse(curSum + nums[i], i+1) or recurse(curSum, i+1)
        return recurse(0, 0)
            
        