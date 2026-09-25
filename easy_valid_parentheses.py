class Solution(object):
    def isValid(self, s):
        symbols_list = ["()", "[]", "{}"]
        i = 0
        copy_s = list(s)
        flag = True
        while len(copy_s) > 0:
            if not flag:
                return False
            i = 1
            flag = False
            while i < len(copy_s):
                if copy_s[i-1] + copy_s[i] in symbols_list:
                    copy_s.pop(i)
                    copy_s.pop(i-1)
                    flag = True
                    i += 1
                i += 1
            if len(copy_s) == 1:
                return False
            if len(copy_s) == 0:
                return True
        else:
            return False

s = "[([]])"
print(Solution().isValid(s))