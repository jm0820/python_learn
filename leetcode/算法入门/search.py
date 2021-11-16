"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。
https://leetcode-cn.com/problems/binary-search/comments/
"""
from typing import List

"""

知识点：
    也就是文章开头的这个例子：
    def add(x:int, y:int) -> int:
        return x + y
    用 : 类型 的形式指定函数的参数类型，用 -> 类型 的形式指定函数的返回值类型。

踩坑：关于python3和python2 之间的一个小坑
    x / y 在python 3中是表示真除法，不会对小数点后面进行截断，所以是一个float类型的数，然后使用一个float类型的数字来引用列表中的一个位置，就出现了问题     
    解决链接：https://zhuanlan.zhihu.com/p/37632606
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            """
            实际使用求中间mid索引建议用这种方法：int mid = left + (right-left)/2; 可以防止left+right溢出（超出整数范围）。
            """
            middle = left + (right-left)//2
            if nums[middle] < target:
                left = middle+1
            elif nums[middle] > target:
                right = middle-1;
            else:
                return middle
        return -1

myclass =  Solution()
list = [1, 3, 5, 16, 19, 67]
print(myclass.search(list, 5))
