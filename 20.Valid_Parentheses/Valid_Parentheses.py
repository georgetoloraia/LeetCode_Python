class Solution(object):
    def isValid(self, s):
        stack = []
        opening_brackets = {'(', '{', '['}
        bracket_pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if bracket_pairs[char] != top:
                    return False

        return len(stack) == 0