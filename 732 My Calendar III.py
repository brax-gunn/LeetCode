from collections import defaultdict
from sortedcontainers import SortedSet

class MyCalendarThree:

    def __init__(self):
        self.__keyList = SortedSet()
        self.__eventMap = defaultdict(int)
        

    def book(self, start: int, end: int) -> int:
        
        self.__eventMap[start] += 1
        self.__eventMap[end] -= 1
        
        self.__keyList.add(start)
        self.__keyList.add(end)
        
        count = 0
        maxCount = 0
        
        
        for key in self.__keyList:
            count += self.__eventMap[key]
            maxCount = max( count, maxCount )
        
        return maxCount
        
        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)