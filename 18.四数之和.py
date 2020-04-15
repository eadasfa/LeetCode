#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length<4:
            return []
        nums.sort()
        result = []
        for i in range(length-3):

            if i!=0 and nums[i] ==  nums[i-1]:
                continue
            for j in range(i+1,length-2):
                if j!=i+1 and nums[j] ==  nums[j-1]:
                    continue
                left,right = j+1,length-1
                while left < right:
                    plus = nums[i] + nums[j] + nums[left] + nums[right] -target
                    # 相加为target
                    if plus == 0 :
                        left,right = left+1,right-1
                        # 判断是否是和上一个加入结果集中的解相同，如果相同，则继续循环
                        if len(result)!=0 and result[-1][0]==nums[i] and \
                             result[-1][1]==nums[j] and result[-1][2] == nums[left-1]:
                            continue
                        # 如果不相同直接加入结果集
                        result.append([nums[i],nums[j],nums[left-1],nums[right+1]])
                    # 如果加起来大于0，只需要right指针向左移动
                    elif plus>0:
                        right-=1
                    # 如果加起来小于0，只需要left指针向右移动
                    else:
                        left+=1
        return result
# print(Solution().fourSum([1,-2,-5,-4,-3,3,3,5],-11))
# print([[-5,-4,-3,1]])
# @lc code=end

'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''