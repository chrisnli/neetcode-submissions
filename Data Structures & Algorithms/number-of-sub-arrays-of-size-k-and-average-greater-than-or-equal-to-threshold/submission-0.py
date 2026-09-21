class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = k - 1
        curr_sum = 0
        for x in range(k):
            curr_sum += arr[x]
        curr_avg = curr_sum / k
        count = 0
        while j + 1 < len(arr):
            if curr_avg >= threshold:
                count += 1
            j += 1
            curr_sum += arr[j]
            curr_sum -= arr[i]
            i += 1
            curr_avg = curr_sum / k
        if curr_avg >= threshold:
            count += 1
        return count
