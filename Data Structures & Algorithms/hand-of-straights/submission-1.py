class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        count = {}
        for num in hand:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        if len(hand) % groupSize != 0:
            return False
        
        j = 0
        while j < len(hand):
            
            c= j % groupSize
            min_num = min(count.keys())
            while c < groupSize:

                if min_num not in count:
                    return False
                
                count[min_num] -= 1
                if count[min_num] == 0:
                    del(count[min_num])
                min_num += 1
                c += 1
                j += 1

        return True