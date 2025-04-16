class Solution(object):
    def singleNumber(self, nums: list):
        for i in nums:
            if nums.count(i) == 1:
                return i


print(Solution.singleNumber(1, [2, 2, 1]))
