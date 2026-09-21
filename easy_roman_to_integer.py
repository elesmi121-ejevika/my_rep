class Solution(object):
    def romanToInt(self, s):
        rom_map = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
            'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        i = 0
        result = 0
        while i < len(s):
            couple_of_char = s[i:i+2]
            if couple_of_char in rom_map:
                result += rom_map[couple_of_char]
                i += 2
            else:
                result += rom_map[s[i]]
                i += 1
        return result

s1 = "XV"
print(Solution().romanToInt(s1))
