class Solution(object):
    def longestCommonPrefix(self, strs):
        substring = ''
        substring_max = ''
        substring_count_curr = 0
        for string in strs:
            i = 0
            substring_max = ''
            while i < len(string):
                substring += string[i]
                for item in strs:
                    if item.startswith(substring):
                        substring_count_curr += 1
                if substring_count_curr == len(strs):
                    substring_max = substring
                i += 1
                substring_count_curr = 0
            substring = ''
        return substring_max

str1 = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(str1))
