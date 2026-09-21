class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # increasing
        i = 0
        j = len(numbers) - 1
        while i < j:
            i_num = numbers[i]
            j_num = numbers[j]
            if i_num == j_num:
                break
            if i_num + j_num == target:
                return [i + 1, j + 1]
            elif i_num + j_num < target:
                i += 1
            else:
                j -= 1
        return []
            