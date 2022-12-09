import time
from typing import List

start_time = time.time()

nums1 = [1,3]
nums2 = [2]
# nums1 = [1,2]
# nums2 = [3,4]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n.sort()
        print(n)
        l = len(n)
        r = 0
        if l%2==0:
            r = (n[l//2]+n[l//2-1])/2
        else:
            r = n[l//2]
        # print(r)
        return r

q = Solution()
r = q.findMedianSortedArrays(nums1=nums1,nums2=nums2)

print("")
print("---")
print(time.time() - start_time, "seconds")
