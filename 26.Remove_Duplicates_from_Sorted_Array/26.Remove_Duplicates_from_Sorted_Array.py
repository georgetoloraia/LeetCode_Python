class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return 1
        
        unique_count = 1
        current = 1
        
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[current] = nums[i]
                unique_count += 1
                current += 1
        
        return unique_count
