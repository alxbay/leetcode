import time
start_time = time.time()

s = "babad"
s = "babadasdds"
# s = "cbbd"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = s[0]
        _lens = len(s)
        _len = len(s)
        polindrom = True
        while _len > 1:
            # print('--')
            # print(_len)
            for i in range(_lens-_len+1):
                ss = s[i:_len+i]
                _f = 0
                _e = len(ss)-1
                _m1 = _e//2
                if _e % 2 == 0:
                    _m2 = _m1
                else:
                    _m2 = _m1+1
                polindrom = True
                for j in range(_m2//2+1):
                    if j !=_m1-j and _m1-j !=_m2+j:
                        # print("    ",ss[j],ss[_e-j], j,_e-j, "|", ss[_m1-j], ss[_m2+j],_m1-j, _m2+j)
                        if ss[j] != ss[_e-j] or ss[_m1-j] != ss[_m2+j]:
                            polindrom = False
                    else:
                        # print("    ",ss[j],ss[_e-j], j,_e-j, "|")
                        if ss[j] != ss[_e-j]:
                            polindrom = False
                    if not polindrom:
                        break
                if polindrom:
                    r = ss
                    # print("Polindrom=",r)
                    break
                # print(ss, _f, _m1, _m2, _e)
            if polindrom:
                break
            _len -= 1
        return r

q = Solution()
r = q.longestPalindrome(s=s)

print("")
print("---")
print(time.time() - start_time, "seconds")