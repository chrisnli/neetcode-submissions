class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        num_map = defaultdict(int)

        for num in nums:
            num_map[num] += 1
        result = True
        for key in num_map.keys():
            result = result & (num_map[key] % 2 == 0)
        
        return result