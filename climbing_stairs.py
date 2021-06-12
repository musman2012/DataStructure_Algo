class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        a = b = 1
        fib_sum = a + b
        
        for i in range(1, n):
            fib_sum = a + b
            a = b
            b = fib_sum
            
        return fib_sum
        
