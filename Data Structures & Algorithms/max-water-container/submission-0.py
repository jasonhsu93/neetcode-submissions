class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1
        best_area = 0

        while i < j:
            area = min(heights[i],heights[j]) * (j - i)
            if area > best_area:
                best_area = area 
            
            if heights[i] >= heights[j]: 
                j -= 1
            elif heights[j] > heights[i]:
                i += 1

        return best_area

