class Solution(object):
    def isPalindrome(self, x):
        string = str(x)
        for i in range(0, len(str(x))):
            if string[i] != string[len(str(x))-1-i]:
                return False
        return True
x = 121252121
print(Solution().isPalindrome(x))