from typing import List

"""
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。 
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        print("反转前：", nums)
        self.reverse(nums, 0, n-1)
        print("第一次全局反转：", nums)

        self.reverse(nums, 0, k - 1)
        print("前半部分反转：", nums)

        self.reverse(nums, k, n - 1)
        print("后半部分反转：", nums)


    def reverse(self, nums:List[int], i, j) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

myclass = Solution()
nums = [-1, -100, 3, 99]
k = 2
myclass.rotate(nums, k)
