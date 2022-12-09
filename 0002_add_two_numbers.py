from typing import Optional
import time
start_time = time.time()

# l1 = [2,4,3]
# l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# l1 = [0]
# l2 = [0]

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]

l1 = [5,6]
l2 = [5,4,9]
# Output: [0,1,0,1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        ss = 0

        a  = l1
        i  = 0
        while a!=None:
            s += a.val*(10**i)
            i += 1
            a=a.next

        a  = l2
        i  = 0
        while a!=None:
            s += a.val*(10**i)
            i += 1
            a=a.next

        ss = s
        j=0
        while (ss > 0):  
            ss =  ss // 10  
            j += 1

        a = None
        for i in reversed(range(j)):
            ss = s
            ss=ss//10**i
            a = ListNode(ss,a)
            s -= ss*(10**i)

        if a == None:
            a = ListNode()
        # i=a
        # while i!=None:
        #     print(i.val)
        #     # print(i.next)
        #     i=i.next
        return a

q = Solution()
aa = None
for a in l1[-1::-1]:
    aa = ListNode(a,aa)
bb = None
for b in l2[-1::-1]:
    bb = ListNode(b,bb)

# i=aa
# # i=bb
# while i!=None:
#     print(i.val)
#     # print(i.next)
#     i=i.next

r = q.addTwoNumbers(l1=aa,l2=bb)

print("")
print("---")
print(time.time() - start_time, "seconds")
