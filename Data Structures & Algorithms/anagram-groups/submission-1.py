class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for i in range(len(strs)):
            key = tuple(sorted(Counter(strs[i]).items()))

            if key in anagrams: 
                anagrams[key].append(strs[i])
            else:
                anagrams[key] = [strs[i]]

        temp = []

        for key in anagrams:
            temp.append(anagrams[key])

        return temp 

        
