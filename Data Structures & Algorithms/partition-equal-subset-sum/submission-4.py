class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 == 1: return False

        def helper(goal, index):
            nonlocal total
            if index + 1 == len(nums):
                return False
            if goal == (total / 2):
                return True
            if goal > (total / 2):
                return False
            
            return helper(goal + nums[index + 1], index + 1) or helper(goal, index + 1)

        return helper(nums[0], 0) or helper(0, 0)