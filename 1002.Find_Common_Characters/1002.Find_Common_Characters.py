class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        common_characters = []

        min_frequency = [float('inf')] * 26

        for word in words:

            current_frequency = [0] * 26

            for char in word:
                current_frequency[ord(char) - ord('a')] += 1
            for i in range(26):
                min_frequency[i] = min(min_frequency[i], current_frequency[i])
        for i in range(26):
            if min_frequency[i] > 0:
                common_characters.extend([chr(i + ord('a'))] * min_frequency[i])

        return common_characters

