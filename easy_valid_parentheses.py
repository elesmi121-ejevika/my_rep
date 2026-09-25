# class Solution2(object):
#     def isValid(self, s):
#         characters1 = {"(" : ")", "{" : "}", "[" : "]"}
#         s_list = list(s)
#         while len(s_list) > 0:
#             found = s_list[0]
#             if s_list[0] not in characters1:
#                 return False
#             if s_list[0] in characters1 and (s_list[1] in characters1 or s_list[1] == characters1[s_list[0]]):
#                 match = characters1[s_list[0]]
#                 last = s_list[1:]
#                 if match not in last:
#                     return False
#                 if match in s_list:
#                     s_list.remove(found)
#                     s_list.remove(match)
#             if not s_list:
#                 return True
#         return False

# class Solution(object):
#     def isValid(self, s):
#         characters = {"(" : ")", "{" : "}", "[" : "]"}
#         matches = [")", "]", "}"]
#         s_list = list(s)
#         length = len(s_list)
#         index = 0
#         flag = False
#         while index < len(s_list):
#             found = s_list[index]
#             f_next = s_list[index + 1]
#             match = characters[s_list[index]]
#             if found in characters and f_next == match:
#                 s_list.remove(found)
#                 s_list.remove(match)
#                 flag = True
#                 if not s_list:
#                     return True
#                 index -= 2
#             index += 1
#         return flag == True
#
# s = "([])()"
# print(Solution().isValid(s))




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