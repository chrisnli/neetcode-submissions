import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        val_to_freq = defaultdict(int)
        
        for num in nums:
            val_to_freq[num] += 1
        buckets = [[] for _ in range(max(val_to_freq.values()) + 1)]
        for val in val_to_freq:
            
            buckets[val_to_freq[val]].append(val)
        result = []
        count = 0
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                if count == k: break
                result.append(buckets[i][j])
                count += 1
        return result
        