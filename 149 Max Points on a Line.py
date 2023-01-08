class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)

        if N == 1:
            return 1
        
        lines = collections.defaultdict(set)

        for i in range(N):
            for j in range(i+1, N):
                x0, y0 = points[i]
                x1, y1 = points[j]
                
                line = self.getLine(x0, y0, x1, y1)

                lines[line].add( (x0, y0) )
                lines[line].add( (x1, y1) )
        
        maxLine = 1
        for key in lines.keys():
            maxLine = max(maxLine, len(lines[key]))
        
        return maxLine

    def getLine(self, x0, y0, x1, y1):

        if y0 == y1:
            return 0, y0
        
        if x0 == x1:
            return x0, None
        
        slope = (y1-y0)/(x1-x0)
        intercept = y0 - slope*x0

        return slope, intercept
    

        