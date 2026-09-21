class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums.sort()
        triplets = []
        dupl = set()
        def helper(n, val):
            nonlocal triplets
            nonlocal dupl
            
            if len(n) > 1:
                n.pop(0) 
            else: return
            # n is nums after index i
            i = 0
            j = len(n) - 1
            while i < j:
                s = n[i] + n[j]
                if s == val:
                    if (n[i], n[j]) not in dupl:
                        triplets.append([-val, n[i], n[j]])
                        dupl.add((n[i], n[j]))
                    i += 1
                    j -= 1
                elif s > val:
                    j -= 1
                else:
                    i += 1
                
            return
        prev = nums[i]
        while i < len(nums) and nums[i] <= 0:
                
            helper(nums[i:], -nums[i])
            i += 1
            if i < len(nums):
                if nums[i] == nums[i - 1]: i += 1
            
        return triplets





        '''
        [-5, -4, -1, -1, 0, 0, 1, 3, 4]
        while i < len nums
            list of nums excluding nums[i]
            helper(list)



        helper()
            while i < j
                find any sums for -nums[i]
                '''
