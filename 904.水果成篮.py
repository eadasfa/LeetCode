#
# @lc app=leetcode.cn id=904 lang=python
#
# [904] 水果成篮
#

# @lc code=start
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        dic,dif_num,left,right,max_ = {},0,0,0,0

        while left<=right and right<len(tree):

            if dic.get(tree[right])==None:
                dic[tree[right]] = 1
                dif_num+=1
                if dif_num>2:
                    while left<=right and dif_num>2:
                        dic[tree[left]]-=1
                        if dic[tree[left]]<=0:
                            del dic[tree[left]]
                            dif_num-=1
                        left+=1
            else:
                dic[tree[right]] += 1
            right += 1
            max_ = max(max_,right-left)
        return max_  

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
# @lc code=end

