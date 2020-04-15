#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return self.method2(s)

        #todo dp[i] 表示以第i个字符结尾的，最长位多少
        dp = [ 0 for _ in range(len(s))]
        #todo 动态规划
        for i in range(1,len(s)):
            if s[i]==')':
                # 获取上一个没有被匹配的括号的index
                j = i - dp[i-1] - 1 
                if j>=0 and s[j] == '(':
                    dp[i] = i-j+1+ (dp[j-1] if j-1>=0 else 0)
        # print(dp)
        return max(dp) if dp else 0
    def dynamic(self,s,i,dp):
        if i==0:
            return 0
        if dp[i]!=-1:
            return dp[i]
        if s[i]==')':
            j = i-1 - self.dynamic(s,i-1,dp)
            if j>=0 and s[j]=='(':
                dp[i] = i-j+1 + (self.dynamic(s,j-1,dp) if j>=1 else 0)
        else :
            dp[i] = 0

        return dp[i]
    def method2(self,s):
        stack = [] # 栈中只存放左括号'('
        temp = [ False for _ in range(len(s))]
        i = 0
        while i<len(s):
            if s[i] == '(':
                stack.append((i,s[i]))
            # 遇到右括号，并且栈不空
            elif len(stack)>0:
                top = stack.pop() # 栈顶元素
                temp[top[0]],temp[i] =True,True
            i+=1
        pre,current = 0,0
        # print(temp)
        for flag in temp:
            if flag:
                current+=1
            else:
                current, pre =0, pre if pre>current else current
        return pre if pre>current else current

print(Solution().longestValidParentheses( "()"))
# @lc code=end

