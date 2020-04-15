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

