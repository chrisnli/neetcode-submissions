import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
         
         
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2 

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        pivot = left
        left = 0
        right = len(nums) - 1

        while left <= right:
            
            middle = (left + right) // 2
            real_mid = (middle + pivot) % len(nums)
            if nums[real_mid] == target: return real_mid
            if nums[real_mid] < target:
                left = middle + 1
            else:
                right = middle - 1
       
        return -1

        