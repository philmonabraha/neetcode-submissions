class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        hashmap = {}

        for h in hand:
            if h not in hashmap:
                hashmap[h] = 1
            else:
                hashmap[h] += 1


        while hashmap:

            start = min(hashmap.keys())
            hashmap[start] -= 1
            if hashmap[start] == 0:
                del hashmap[start]

            for i in range(groupSize-1):

                if start+1 not in hashmap:
                    return False
                
                start = start + 1
                hashmap[start] -= 1
                if hashmap[start] == 0:
                    del hashmap[start]

        return True


        