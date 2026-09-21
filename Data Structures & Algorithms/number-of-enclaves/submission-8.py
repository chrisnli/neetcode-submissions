class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited_false = set() # set of cells we can walk off boundary
        visited_true = set() # set of cells we cannot walk off boundary
        seen = set()
        def traversal(i, j):
            
            if grid[i][j] == 1 and (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
                return False
            if grid[i][j] == 0:
                return True
            if (i, j) in visited_false:
                return False
            if (i, j) in visited_true:
                return True
            if (i, j) in seen:
                return True
            seen.add((i, j))

            return traversal(i - 1, j) and traversal(i, j -1) and traversal(i + 1, j) and traversal(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                seen = set()
                if not traversal(i, j):
                    visited_false.update(seen)
                else:
                    visited_true.update(seen)
        
        return len(visited_true)