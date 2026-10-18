class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # we want a dictionary to keep track of the numbers and their frequencies
        # a list of list so that we can keep track of numbers that appear the amount that index describes 

        mem = {}

        for num in nums:
            mem[num] = mem.get(num, 0) + 1 

        buckets = [[] for _ in range(len(nums) + 1)]

        for num,freq in mem.items():
            buckets[freq].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result