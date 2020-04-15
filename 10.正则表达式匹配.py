#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [ [-1 for __ in range(len(s))] for _ in range(len(p))]

        return self.degress(0,0,p,s,dp)

    def isMatchChar(self,r,ch):
        if r=='.' or ch == r:
            return True
        return False
    # 判断是否匹配完
    def isMatchFinished(self,p_i,s_j,p,s):
        # 如果 s串到达了最后
        if s_j==len(s):
            # 如果p串也到达了最后，直接返回True
            if p_i==len(p):
                return True
            # 如果p没有匹配完，此时有两种可能，当前为*，只要后面的是 .*.*这种就算匹配成功
            # 如果当前不是*，只要后面是*.*.*就没问题
            else:
                p_i = p_i+1 if p[p_i] == '*' else p_i
                temp = 0
                while p_i<len(p):
                    temp += 1 if p[p_i]!='*' else -1
                    p_i+=1
                return (temp==0)
        # s串没到达最后直接返回False
        return False
    def degress(self,i,j,p,s,dp):
        i_s,j_s=i,j
        if not (i<len(p) and j <len(s)):
            return self.isMatchFinished(i,j,p,s)
        if dp[i][j]!=-1:
            return dp[i][j]==1
        res = False
        while i < len(p) and j < len(s): 
            r = p[i]
            if r=='*':
                # 出现*代表*前面的那个已经匹配了，此时调用递归待变不继续匹配下去了
                if self.degress(i+1,j,p,s,dp):
                    dp[i][j] = 1
                    return True
                # 如果不继续匹配下去不行，贪心的匹配下一个
                r_ = p[i-1]
                if self.isMatchChar(r_,s[j]):
                    j=j+1
                else:
                    i=i+1
            else:
                # 当前字符不匹配
                if not self.isMatchChar(r,s[j]) :
                    # 如果当前字符不匹配并且下一个不是*，就代表没法跳过当前字符，直接匹配失败
                    if i!=len(p)-1 and p[i+1]!='*':
                        dp[i][j] = 0
                        return False
                    # 如果下一个是 * ，代表能跳过当前字符
                    i+=1
                else:
                    # 当前字符能够匹配，
                    if i!=len(p)-1 and p[i+1]=='*':
                        # 如果下一个是*，尝试不匹配这个字符，直接跳过*
                        if self.degress(i+2,j,p,s,dp):
                            dp[i][j] = 1
                            return True
                    # 匹配当前字符
                    i,j = i+1, j+1
            # s 已经匹配
        res = self.isMatchFinished(i,j,p,s)
        dp[i_s][j_s] = 1 if res else 0
        return res
s = "aaaaaaaaaaaaab"
r = "a*a*a*a*a*a*a*a*a*a*c"
print(Solution().isMatch(s,r))
# import re
# print(re.search(r,s)!=None)
# @lc code=end

