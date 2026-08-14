class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def recurse(index):
            if index == len(nums)-1:
                return True
            if nums[index] == 0:
                cache[index] = False
                return False
            if index in cache:
                return cache[index]
            for i in range(1, nums[index]+1):
                if recurse(index + i):
                    cache[index+i] = True
                    return True
            cache[index] = False
            return False
        return recurse(0)
                
        