class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        res = self.__rollingDice(0, n, k, 0, target, {})
        return res % MOD
    
    def __rollingDice(self, currIndex, lastIndex, k, currSum, targetSum, memo):
        
        if currIndex >= lastIndex:
            if currSum == targetSum:
                return 1
            return 0
        
        if currSum > targetSum:
            return 0
        
        currKey = (currIndex, currSum)
        if currKey in memo:
            return memo[currKey]
        
        possibleSum = 0
        for diceVal in range(1,k+1):
            possibleSum += self.__rollingDice(currIndex+1, lastIndex, k, currSum + diceVal, targetSum, memo)
            
        memo[currKey] = possibleSum
        return memo[currKey]