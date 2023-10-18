class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            reversed_x = -int(str(abs(x))[::-1])
        else:
            reversed_x = int(str(x)[::-1])
    
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
    
        return reversed_x