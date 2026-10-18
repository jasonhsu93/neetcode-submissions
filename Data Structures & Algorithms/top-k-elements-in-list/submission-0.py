class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mem = {}

        for num in nums:
            mem[num] = mem.get(num,0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in mem.items():
            buckets[count].append(num)

        result = []

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        sorted = dict(mem.items(),)