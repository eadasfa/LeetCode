#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solve2(0,0,board)
                    
    def solve2(self,i,j,board):
        # 超出了
        if i>=9:
            return True
        if board[i][j]!='.':
            return self.solve2(i+(j+1)//9,(j+1)%9,board)
        for k in self.vaild_set(i,j,board):
            board[i][j] = k
            if self.solve(i+(j+1)//9,(j+1)%9,board):
                return True
            board[i][j]='.'
        return False
    def vaild_set(self,i,j,board):
        # res = []
        # for k in range(9):
        #     row_box = k//3 + (i//3)*3
        #     column_box = k%3 + (j//3)*3
        #     res.append(board[i][k])
        #     res.append(board[k][j])
        #     res.append(board[row_box][column_box])
        # return list(set([str(x) for x in range(1,10)])-set(res))
        res = [str(x) for x in range(1,10)]
        for k in range(9):
            row_box = k//3 + (i//3)*3
            column_box = k%3 + (j//3)*3
            if board[i][k] in res:
                res.remove(board[i][k])
            if board[k][j] in res:
                res.remove(board[k][j])
            if board[row_box][column_box] in res:
                res.remove(board[row_box][column_box])
        return res
    def solve(self,i,j,board):
        # 超出了
        if i>=9:
            return True
        if board[i][j]!='.':
            return self.solve(i+(j+1)//9,(j+1)%9,board)
        for k in range(1,10):
            if self.isVaild(board,i,j,k):
                board[i][j] = str(k)
                if self.solve(i+(j+1)//9,(j+1)%9,board):
                    return True
                board[i][j]='.'
        return False
    # i,j: board[i,j] = num 是否有效
    def isVaild(self,board,i,j,num):
        # 3*3 box
        # row,column
        num_str = str(num)
        for k in range(9):
            row_box = k//3 + (i//3)*3
            column_box = k%3 + (j//3)*3
            if board[i][k]==num_str or board[k][j]==num_str or \
            board[row_box][column_box]==num_str:
                return False
        return True
# @lc code=end

# 思路比较简单，创建三个 可用数字统计列表，分别从 行、列、宫三个角度进行放纳和删除，并使用DFS+回溯+剪枝的方式进行逐步空位的填充。
# 时间复杂度为O(9!^9),空间复杂度为O(9^2)
class Solution2(object):
    def solveSudoku(self, board):
        # 初始设定在每个位置可以使用的数字，默认的话，初始任何数字都是可以用的。
        # 行 剩余可用数字
        row=[set(range(1, 10)) for _ in range(9)]
        # 列 剩余可用数字
        col=[set(range(1, 10)) for _ in range(9)]
        # 块 剩余可用数字
        block=[set(range(1, 10)) for _ in range(9)]
        ############################    空位和可用数收集   ########################
        # 收集需填数位置 empty。   并根据现有分布情况 去除那些 在row 、col、block对应序号下按规则不可以用的数字。
        empty = []
        for i in range(9):
            for j in range(9):

                # 更新可用数字   如果是数字的话，进行  行、列上的可用数字更新， 进行一些移除，标识不能用这几个数字。
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    # 对3*3块 内数字进行移除，标识在当前 块序号 内不能使用这个数
                    block[(i // 3)*3 + j // 3].remove(val)
                else:
                    # 加入空位序号
                    empty.append((i, j))
        ############################    对空闲位置，启动回溯方式的填充尝试   ########################
        def backtrack(iter=0):
            # 处理完empty代表找到了答案
            if iter == len(empty):
                return True
            # 获取当前需要填充的空位序号 、以及所归属的块 。
            i, j = empty[iter]
            b = (i // 3)*3 + j // 3

            # 获取到行列 和 块内共同认可的数字。  进行填充尝试使用。  【但是这种填充不一定对，所以只是一种dfs算法，如果不对就对填充操作回溯。】
            # set集合  & 交集， | 并集， - 差集
            for val in row[i] & col[j] & block[b]:
                # 填充后的去除  可用数字操作
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)

                board[i][j] = str(val)

                # 进行 下一步的 后一个空位的dfs填充操作
                if backtrack(iter+1):
                    return True

                # 回溯操作，还原。
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            # 这里没有明显的剪枝，当在当前dfs下，无法 进行空位填充，不能执行for下的操作时，就自动进行树的剪枝即可。
            return False

        backtrack()

'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

'''