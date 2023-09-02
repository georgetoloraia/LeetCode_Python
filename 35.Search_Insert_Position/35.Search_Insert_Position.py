class Solution(object):
    def searchInsert(self, nums, target):
        for num in nums:
            if num == target:
                return nums.index(num)
            if num > target:
                return nums.index(num)
        return len(nums)

