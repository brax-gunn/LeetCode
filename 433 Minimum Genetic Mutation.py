class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        
    def __str__(self):
        return str(self.val)

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        if end not in bank:
            return -1
        
        bank.append(start)
        
        N = len(bank)
        
        nodes = {}
        for elem in bank:
            nodes[elem] = Node(elem)
            
        source = nodes[start]
        target = nodes[end]
        
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                else:
                    if self.__isMutation(bank[i], bank[j]):
                        nodes[ bank[i] ].children.append( nodes[ bank[j] ] )
                        nodes[ bank[j] ].children.append( nodes[ bank[i] ] )
        
        
        minCost = [ float("inf") ]
        self.__dfs(source, target, set(), 0, minCost)
        return minCost[0] if minCost[0] != float("inf") else -1
    
    def __dfs(self, root, target, visitedArr, cost, minCost):
        
        if root.val == target.val:
            minCost[0] = min(minCost[0], cost)
            return
        
        for child in root.children:
            
            if child in visitedArr:
                continue
            
            visitedArr.add(child)
            self.__dfs(child, target, visitedArr, cost+1, minCost)
            visitedArr.pop()
            
    
    def __isMutation(self, currStr, givenStr):
        totalDiff = 0
        for i in range(8):
            if currStr[i] != givenStr[i]:
                totalDiff += 1
        return totalDiff == 1