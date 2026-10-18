class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [] 
        prefix = 1

        for i in range(len(nums)):
            if i == 0:
                result.append(prefix)
            else:
                prefix *= nums[i-1]
                result.append(prefix)
        
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                postfix *= nums[i+1]
                result[i] *= postfix

        return result

            

