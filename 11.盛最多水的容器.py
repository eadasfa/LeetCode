#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 左右两个指针，表示正方形范围
        left,right = 0,len(height)-1
        # 初始化最大为整个数组第0个和最后一个个的范围
        max_ =  (right-left) * min(height[left],height[right])
        while left<right:
            if height[left]<height[right]:
                temp = height[left]
                # 左边小于右边时，将左边指针向右滑动，一直到其值大于初始的左边的值
                while left<right and height[left]<=temp:
                    left+=1
            else :
                temp = height[right]
                # 右边小于左边时，将右边指针向左滑动，一直到其值大于初始的右边的值
                while left<right and height[right]<=temp:
                    right-=1
            x = (right-left) * min(height[left],height[right])
            max_ = max(x,max_)
        return max_
# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
# @lc code=end

'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 
示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
'''