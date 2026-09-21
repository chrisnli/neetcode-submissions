class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])

        n = len(costs) // 2
        total_sum = 0
        for i in range(n):
            total_sum += costs[i][1]
        
        for j in range(n, len(costs)):
            total_sum += costs[j][0]
        return total_sum