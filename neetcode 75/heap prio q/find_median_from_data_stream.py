# problem:
# The median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value, 
# and the median is the mean of the two middle values.
# 
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# 
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
#  
# 
# Example 1:
# 
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 
# soln:
# use a heap prio queue
# split arr into two sides
# leftside = maxheap
# rightside = minheap
# to get median just take (max(leftside) + min(rightside)) / 2
# or if len(leftside) > len(rightside) => return max(left)
# else return min(right)
# each side can only be at most 1 elt greater than the other
# default to insert into left
# when left > right + 1:
# pop max from left and append to right
# 
# implementation:
import heapq

class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        # heappush(heap, elt)
        # since small needs to be a maxheap -> transform data by * -1
        heapq.heappush(self.small, -1 * num)
        
        if self.small and self.large and (self.small[0] * -1 > self.large[0]):
            num = heapq.heappop(self.small)
            heapq.heappush(self.large, num * -1)
        
        if len(self.small) > len(self.large) + 1:
            num = heapq.heappop(self.small)
            heapq.heappush(self.large, num * -1)            
        
        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, num * -1)    
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((self.small[0] * -1) + self.large[0]) / 2