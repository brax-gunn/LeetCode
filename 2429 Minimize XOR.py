class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        n1 = self.__countSetBits(num1)
        n2 = self.__countSetBits(num2)
        
        binaryNum1 = bin(num1)[2:]
        binaryNum2 = bin(num2)[2:]


        if n1 == n2:
            return num1

        elif n1 > n2:
            res = ""
            for char in binaryNum1:
                if char == "1" and n2 > 0:
                    res += "1"
                    n2 -= 1
                else:
                    res += "0"
                    
            return int(res, 2)
        
        else:
            res = ""
            n2 = n2-n1
            for i in range( len(binaryNum1)-1, -1, -1 ):
                char = binaryNum1[i]
                if char == "0" and n2 > 0:
                    res = "1" + res
                    n2 -= 1
                
                elif char == "0" and n2 <= 0:
                    res = "0" + res
                
                elif char == "1":
                    res = "1" + res
            
            res = n2*"1" + res
            
            return int(res, 2)
    
    def __countSetBits(self, n):
        
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        
        return count