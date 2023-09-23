class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ''
        for i in s:
            i.lower().isalnum()
            result += i

        return result == result[::-1]