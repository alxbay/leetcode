from typing import List
import time

start_time = time.time()
x = 123
x = -1234
# x = 1534236469
# x = 2147483648
    # 2147483412
    # 1534236469

class Solution:
    def reverse(self, x: int) -> int:
        a = x
        r = 0
        l = 2**31 - 1
        if a<0:
            a=a*(-1)
        if a > l:
            r = 0
        else:
            while a > 0:
                r = r*10 + a % 10
                a = a // 10
                # print(a, r)
                if r > l:
                    r = 0
                    a = 0
            if x<0:
                r=r*(-1)
        return r

q = Solution()
r = q.reverse(x)
print(r)
print(time.time() - start_time, "seconds")
