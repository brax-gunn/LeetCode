from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.__memo = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.__memo[key].append( (timestamp, value) )
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.__memo:
            return ""
        else:
            return self.__binarySearch(key, timestamp)
    
    def __binarySearch(self, key, timestamp):
        
        start = 0
        end = len(self.__memo[key])
        
        res = ""
        
        while start < end:
            
            mid = (start + end)//2
            
            currTime, currVal = self.__memo[key][mid]
            
            if currTime > timestamp:
                end = mid
            
            elif currTime <= timestamp:
                res = currVal
                start = mid + 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)