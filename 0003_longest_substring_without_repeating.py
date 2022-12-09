import time

start_time = time.time()

# s = "pwwkew"
# s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# s = "oelvjrrrazkwqgotdrwyevqyveanupskteiexzvxyfvqmmkrfipkdfkammpieisxmaclczlcfgvtsfkypcksjwsxlifpqaoe"
# s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfdfdfdfdfoe"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        e = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
        if len(e)>len(s):
            _len = len(s)
        else:
            _len = len(e)
        _lens = len(s)
        # print(len(n))
        # print(_len)
        repeatedstr = ""
        while _len > 0:
            # print('--')
            # print(_len)
            for i in range(_lens-_len+1):
                ss = s[i:_len+i]
                # print(ss)
                aa = []
                repeated=False
                for a in ss:
                    # print(a,ss,sep=" - ")
                    if a in aa:
                        repeated = True
                        break
                    else:
                        aa.append(a)
                if not repeated:
                    repeatedstr = ss
                    break
            if repeatedstr != "":
                break
            _len -= 1

        return len(repeatedstr)

q = Solution()
r = q.lengthOfLongestSubstring(s)
print(r)

print("")
print("---")
print(time.time() - start_time, "seconds")