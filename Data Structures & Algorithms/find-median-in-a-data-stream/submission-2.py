class MedianFinder:

    def __init__(self):
        self.minimum = [] # right
        self.maximum = [] # left

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maximum, -1 * num) 

        if (self.minimum and self.maximum) and (-1 * self.maximum[0]) > self.minimum[0]:
            temp = heapq.heappop(self.maximum) 
            heapq.heappush(self.minimum, -1 * temp)

        if len(self.minimum) - len(self.maximum) > 1:
            temp = heapq.heappop(self.minimum) 
            heapq.heappush(self.maximum, -1 * temp)
        elif len(self.maximum) - len(self.minimum) > 1:
            temp = heapq.heappop(self.maximum) 
            heapq.heappush(self.minimum, -1 * temp)
 
    def findMedian(self) -> float:
        
        if len(self.minimum) > len(self.maximum):
            return self.minimum[0]
        elif len(self.maximum) > len(self.minimum):
            return -1 * self.maximum[0]
        else:
            return (self.minimum[0] + (-1 * self.maximum[0]))/2 