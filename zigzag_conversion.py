import time
start_time = time.time()

# s = "PAYPALISHIRING"
s = "A"
numRows = 3
numRows = 4
numRows = 1
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# 0     6       12
# 1   5 7    11 13
# 2 4   8 10    
# 3     9       

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = ""
        l = len(s)
        c = numRows
        w = l//c+1    # count waves
        if w<=0:
            w=1
        d = c-2     # count chars in diagonale
        if d<=0:
            d=0
        print("w=",w," , ","d=",d)
        for n in range(c):
            print(n,"--")
            for j in range(w):
                print(j)
                if n+(c+d)*j < l:
                    ii = n+(c+d)*j
                    print(ii , s[ii])
                    r += s[n+(c+d)*j]
                if n in range(1,c-1) and (c+d-n+(c+d)*j < l):
                    ii = c+d-n+(c+d)*j
                    print(ii , s[ii], s)
                    r+=s[c+d-n+(c+d)*j]
        # print(r)
        # if r=="":
        return r


q = Solution()
print(q.convert(s=s, numRows=numRows))


print("")
print("---")
print(time.time() - start_time, "seconds")