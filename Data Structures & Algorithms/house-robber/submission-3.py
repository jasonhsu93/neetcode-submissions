class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        
        p1 = nums[0]
        p2 = max(nums[0],nums[1])
        res = 0
        
        for i in range(2,len(nums),1):
            res = max(p1 + nums[i], p2,)
            p1 = p2
            p2 = res 

        return res