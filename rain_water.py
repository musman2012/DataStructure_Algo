class Solution:
    def trap(self, height: List[int]) -> int:
        total_vals = len(height)
        water = 0
        
        if total_vals == 0:
            return water
        
        left_max = [0]*total_vals
        right_max = [0]*total_vals
        
        left_max[0] = height[0]
        right_max[total_vals - 1] = height[total_vals - 1]
        
        for i in range(1, total_vals):
            left_max[i] = max(height[i], left_max[i-1])
            
        for i in range(total_vals - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
            
        for i in range(0, total_vals):
            water += min(right_max[i], left_max[i]) - height[i]
            
        return water
    
## https://www.educative.io/edpresso/the-trapping-rainwater-algorithm-in-cpp-python-and-java
