#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1),len(nums2)
        medium_num = 2-(m+n)%2
        medium_index = (m+n)//2-(medium_num-1)
        medium_sum = 0.0
        i,j=0,0
        counter = -1
        while i!=m or j!=n:
            while i!=m and j!=n and nums1[i] < nums2[j]:
                i,counter = i+1,counter+1
                medium_num,medium_sum,medium_index = self.judge_finish(
                    medium_sum,medium_num,counter,medium_index,nums1[i-1])
                if medium_num == 0:
                        return medium_sum/(2-(m+n)%2)
            while i!=m and j!=n and nums1[i] >= nums2[j]:
                j,counter = j+1,counter+1
                medium_num,medium_sum,medium_index = self.judge_finish(
                    medium_sum,medium_num,counter,medium_index,nums2[j-1])
                if medium_num == 0:
                        return medium_sum/(2-(m+n)%2)
            while i==m and j!=n:
                j,counter = j+1,counter+1
                medium_num,medium_sum,medium_index = self.judge_finish(
                    medium_sum,medium_num,counter,medium_index,nums2[j-1])
                if medium_num == 0:
                        return medium_sum/(2-(m+n)%2)
            while i!=m and j==n:
                i,counter = i+1,counter+1
                medium_num,medium_sum,medium_index = self.judge_finish(
                    medium_sum,medium_num,counter,medium_index,nums1[i-1])
                if medium_num == 0:
                        return medium_sum/(2-(m+n)%2)
        return 0
    def judge_finish(self,medium_sum,medium_num,counter,medium_index,num):
        if medium_num!=0 and counter==medium_index:
            medium_sum += num
            medium_num -= 1
            medium_index +=1
        return medium_num,medium_sum,medium_index

# s = Solution()
# print(s.findMedianSortedArrays([1,2],[3,4]))       
# @lc code=end

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''