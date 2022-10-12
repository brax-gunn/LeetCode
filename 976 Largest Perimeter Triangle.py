class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        # 2 1 1 1 1 
        # + - - - +
        # 2 1 1
        
        N = len(nums)
        
        nums.sort(reverse=True)
        
        i = 0
        while i < N:
            
            j = i+1
            while j < N:
                
                k = j+1
                while k < N and nums[k] < nums[i] + nums[j]:
                  
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]
                    
                    if (a + b > c) and (b + c > a) and (c + a > b):
                        return a + b + c
                    else:
                        break
                    
                    k += 1
                
                j += 1
            
            i += 1
        
        return 0
        