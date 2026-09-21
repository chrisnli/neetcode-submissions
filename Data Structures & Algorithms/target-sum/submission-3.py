class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count = 0
        def helper(total, index):
            nonlocal nums, target, count
            if index == len(nums) - 1:
                if total == target:
                    count += 1
                
                return
            helper(total + nums[index + 1], index + 1)
            helper(total - nums[index + 1], index + 1)
        
        helper(nums[0], 0)
        helper(-nums[0], 0)
        return count