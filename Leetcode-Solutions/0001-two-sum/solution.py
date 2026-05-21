class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,num in enumerate(nums):
            c = target - num
            if c in res:
                return[res[c],i]
            res[num] = i
        return []
