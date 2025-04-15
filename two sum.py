class Solution(object):
    def twoSum(self, nums: list, target):
        for g in nums:
            num1_index = nums.index(g)
            num1 = g
            num2 = target - num1
            num2_index = nums.index(num2)
            if num2 == num1:
                num2_index += 1
            for i in nums:
                if num2_index != num1_index and nums[num1_index] + nums[num2_index] == target:
                    return [num1_index, num2_index]


print(Solution.twoSum(1, [2, 7, 11, 15], 9))
