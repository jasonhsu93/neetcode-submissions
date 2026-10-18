class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # brute force, every number, check if theres a consecutive integer next, and try to make the longest chain and record it, it'd be n * n O(n^2)

        # each number store in dict, u check each number's surroundings?

        mem = set()
        length = 0
        best_length = 0

        for i in range(len(nums)):
            mem.add(nums[i])

        for num in mem:
            if num - 1 not in mem:
                consecutive = 0
                while num + consecutive in mem:
                    consecutive += 1
                length = consecutive 
                if length > best_length:
                    best_length = length

        return best_length
                
                