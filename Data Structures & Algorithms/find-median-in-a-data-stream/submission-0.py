class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        sort = self.array.sort()
        if len(self.array) % 2 == 0:
            return ((self.array[len(self.array)//2]+self.array[len(self.array)//2-1])/2)
        else:
            return self.array[len(self.array)//2]
            
        