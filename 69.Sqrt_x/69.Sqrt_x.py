class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid

            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        