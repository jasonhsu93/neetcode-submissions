class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # calculate the character frequencies of each string in the list in a dict, then return the result as a list

        mem = {}

        for string in strs:
            bucket = [0] * 26
            for i in range(len(string)):
                bucket[ord(string[i])-ord('a')] += 1
            if not tuple(bucket) in mem:
                mem[tuple(bucket)] = [string]
            else:
                mem[tuple(bucket)].append(string)

        result = []

        for value in mem.values():
            result.append(value)

        return result