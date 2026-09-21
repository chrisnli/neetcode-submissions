import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        result = set()
        for num in nums:
            count[num] += 1
            if count[num] > n/3:
                result.add(num)

        return list(result)