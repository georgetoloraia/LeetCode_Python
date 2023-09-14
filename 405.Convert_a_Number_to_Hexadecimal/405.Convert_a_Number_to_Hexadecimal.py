class Solution(object):
    def toHex(self, num):
        hex_digits = []
        if num < 0:
            num = num + (2 ** 32) 

        if num == 0:
            return "0"

        while num > 0:
            remainder = num % 16
            if remainder < 10:
                hex_digits.append(str(remainder))
            else:
                hex_digits.append(chr(ord('a') + remainder - 10))
            num //= 16
    
        hex_digits.reverse()
        hex_str = ''.join(hex_digits)
    
        return hex_str