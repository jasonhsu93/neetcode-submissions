class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        index = 0
        for num in nums:
            if (target - num) in mem:
                return [mem[target-num],index]
            mem[num] = index
            index += 1
