class Solution:
    def climbStairs(self, n: int) -> int:

        # 5 3 2 1 0
        
        one, two = 1, 0

        for i in range(n):
            one, two = one + two, one

        return one