class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        total_wo_zero = 1
        zero_count = 0

        for num in nums:
            if num == 0 and zero_count == 0:
                total_wo_zero = total
                zero_count += 1
                total *= num
            elif num == 0 and zero_count != 0:
                total_wo_zero = 0
            else:
                total_wo_zero *= num 
                total *= num
                
            

        result = []

        for num in nums:
            if num == 0 and zero_count == 1:
                result.append(total_wo_zero)
            elif num == 0 and zero_count != 1:
                result.append(0)
            else:
                result.append(int(total/num))

        return result