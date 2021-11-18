from typing import List

"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j, k = 0, len(nums) - 1, len(nums) - 1
        des = [-1] * len(nums)
        k = len(nums) - 1
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                des[k] = nums[j] ** 2
                j -= 1
            else:
                des[k] = nums[i] ** 2
                i += 1
            k -= 1
        return des

myclass = Solution()
nums = [-4,-1,0,3,10]
print(myclass.sortedSquares(nums))