from typing import List
import time

start_time = time.time()
nums = [2,70,11,15]
target = 9
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         j = 0
#         while nums != [] or (a+b == target):
#             a = nums.pop(0)
#             j = i + 1
#             for b in nums:
#                 # print (i,a,sep=' - ')
#                 if a+b==target:
#                     return ([i,j])
#                     break
#                     print(i,j)
#                 j += 1
#             i += 1
#         return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s1 = len(nums)
        for i in range(s1):
            a = target - nums[i]
            for j in range(i+1,s1):
                if a == nums[j]:
                    return ([i,j])
        return []

q = Solution()
r = q.twoSum(nums=nums, target=target)
print(r)
print(time.time() - start_time, "seconds")
