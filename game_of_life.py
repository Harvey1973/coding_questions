class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #print(self.count_neighbours(board,1,0))
        n = len(board)  # rows
        m = len(board[0]) # columns
        out = [ [0]*m for i in range(n)]
        for i in range(n) :
            
            for j in range(m):
                #print(i)
                #print(j)
                if board[i][j] == 0:
                    #print("dead")
                    neighbours = self.count_neighbours(board,i,j)
                    #print("neighbours:" + str(neighbours))
                    if neighbours == 3:
                        out[i][j] = 1
                    #print(out[i][j])
                    #print("------")
                else :
                    #print("alive")
                    neighbours = self.count_neighbours(board,i,j)
                    #print("neighbours:" + str(neighbours))

                    if neighbours < 2:
                        out[i][j] = 0
                    elif neighbours ==2 or neighbours == 3:
                        out[i][j] = board[i][j]
                    elif neighbours > 3:
                        out[i][j] = 0
                    #print(out[i][j])
                    #print("------")
                #print(out)
        print(out)
        board = out
        print(board)   
    def count_neighbours(self,board,i,j):
        pos1 = (i - 1, j - 1)
        pos2 = (i - 1, j)
        pos3 = (i - 1, j + 1)
        pos4 = (i, j - 1)
        pos5 = (i, j + 1)
        pos6 = (i + 1, j - 1)
        pos7 = (i + 1, j)
        pos8 = (i + 1, j + 1)
        count = 0

        if not self.test_bound(pos1,board):
            if board[pos1[0]][pos1[1]] == 1:
                count = count + 1
        if not self.test_bound(pos2,board):
            if board[pos2[0]][pos2[1]] == 1:
                count = count + 1
        if not self.test_bound(pos3,board):
            if board[pos3[0]][pos3[1]] == 1:
                count = count + 1
        if not self.test_bound(pos4,board):
            if board[pos4[0]][pos4[1]] == 1:
                count = count + 1
        if not self.test_bound(pos5,board):
            if board[pos5[0]][pos5[1]] == 1:
                count = count + 1
        if not self.test_bound(pos6,board):
            if board[pos6[0]][pos6[1]] == 1:
                count = count + 1
        if not self.test_bound(pos7,board):
            if board[pos7[0]][pos7[1]] == 1:
                count = count + 1
        if not self.test_bound(pos8,board):
            if board[pos8[0]][pos8[1]] == 1:
                count = count + 1
        return count
        


    
    def test_bound(self,pos,board):
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(board) or pos[1] >= len(board[0])  :
            return True

        


obj = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
obj.gameOfLife(board)