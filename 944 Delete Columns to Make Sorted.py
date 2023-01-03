class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)
        M = len(strs[0])
        grid = self.getGrid(strs, N, M)
        res = self.countUnsortedCols(grid, N, M)
        return res
    
    def countUnsortedCols(self, grid, N, M):
        res = 0
        
        for j in range(M):
            prevVal = -1
            for i in range(N):
                currVal = ord(grid[i][j])
                if currVal < prevVal:
                    res += 1
                    break
                else:
                    prevVal = currVal
        
        return res
        
    
    def getGrid(self, strs, N, M):
        grid = []
    
        for i in range(N):
            row = []
            for j in range(M):
                row.append(strs[i][j])
            grid.append(row)
        
        return grid
