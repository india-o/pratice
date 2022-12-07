#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
from typing import List
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = []

        newList = nums1 + nums2 
        newList.sort()
        length = len(newList)
        if(length % 2 == 1):
            index=math.floor(length / 2)
            ans = newList[index]
        else:
            index = 0
            index2 = 1
            if(length != 2):
                index = int(length/2)
                index2 = int(length/2) - 1
            val = newList[index] + newList[index2] 
            ans =  val / 2.0
        return ans 

solution=Solution()
nums1 = [1,3]
nums2 = [2]  
print(solution.findMedianSortedArrays(nums1,nums2))        
        
        