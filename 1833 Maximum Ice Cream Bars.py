class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        N = len(costs)

        costs.sort()

        iceCream = 0

        i = 0
        while i < N and coins > 0 and coins >= costs[i]:
            coins -= costs[i]
            iceCream += 1
            i +=1 
        
        return iceCream