class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_water = min(heights[i], heights[j]) * j
        curr_water = max_water

        while i < j:
            if heights[i] < heights[j]:
                i += 1
                curr_water = min(heights[i], heights[j]) * (j - i)
                max_water = max(max_water, curr_water)
            else:
                j -= 1
                curr_water = min(heights[i], heights[j]) * (j - i)
                max_water = max(max_water, curr_water)

        return max_water