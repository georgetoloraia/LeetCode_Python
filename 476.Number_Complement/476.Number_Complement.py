class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = 1
        while x <= num:
            x <<= 1
        return (x - 1) ^ num