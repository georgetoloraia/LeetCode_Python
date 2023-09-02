class Solution(object):
    def strStr(self, haystack, needle):
        # Check if the needle is an empty string
        if not needle:
            return 0

        # Iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        # Return -1 if needle is not found
        return -1
