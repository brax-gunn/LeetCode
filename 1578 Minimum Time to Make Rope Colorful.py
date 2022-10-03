class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        leftPtr = 0
        rightPtr = 1
        
        N = len(colors)
        
        minTime = 0
        while rightPtr < N:
            
            if colors[leftPtr] == colors[rightPtr]:
                
                currSum = neededTime[leftPtr]
                maxVal = neededTime[leftPtr]
                
                while rightPtr < N and colors[leftPtr] == colors[rightPtr]:
                    currSum += neededTime[rightPtr]
                    maxVal = max(maxVal, neededTime[rightPtr])
                    leftPtr += 1
                    rightPtr += 1
                    
                minTime += (currSum-maxVal)
            
            leftPtr += 1
            rightPtr += 1
        
        return minTime
