

class Solution(object):
    def TwoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement, i]]
            hashmap[nums[i]] = i
        return