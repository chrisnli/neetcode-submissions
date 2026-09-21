class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = deque()

        i = 0
        while i < len(asteroids):

            curr = asteroids[i]
            
            if res and curr < 0 and res[-1] > 0:
                while res and curr < 0 and res[-1] > 0:
                    if abs(curr) == abs(res[-1]):
                        res.pop()
                        curr = 0
                        break
                    elif abs(curr) > abs(res[-1]):
                        res.pop()
                    else: 
                        
                        curr = 0
                        break
                if curr != 0:
                    res.append(curr)
                
            else:
                res.append(curr)
            i += 1

        return list(res)
            