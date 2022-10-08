class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        N = len(nums)
        
        closestSum = float('-inf')
        
        for i, a in enumerate(nums):
            
            left = i+1
            right = N-1
            
            while left < right:
                
                b = nums[left]
                c = nums[right]
                
                currentSum = a + b + c
                
                if abs(target-currentSum) < abs(target-closestSum):
                    closestSum = currentSum
                
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return closestSum
        
        return closestSum
        
        