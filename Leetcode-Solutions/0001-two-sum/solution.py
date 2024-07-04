class Solution(object):
    def twoSum(self, nums, target):
        a = {}
        for i in range(len(nums)):

            diff = target - nums[i]
            if diff in a:
                return(i,a[diff])
            a[nums[i]] = i
        return []
            
