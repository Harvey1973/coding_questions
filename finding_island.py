from pandas import *
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        height = len(grid)
        width = len (grid[0])
        connected = [[False]*width for e in range (height)]
        count = 0 
        if(grid == []):
            return 0 
        for i in range(height) :
            for j in range(width)  :
                if grid[i][j] == "1" and connected[i][j] == False :
                    print("for loop")
                    new_count, new_connec = self.DFS(i,j,grid,connected, count)
                    count = count + 1
                    
                    #print(new_count)

        print(new_connec)
        return count

    def DFS (self, i,j,grid, connected,count):
        connected[i][j] = True
        new_index= self.find_neighbour(i,j,grid,connected)
        if (new_index[0] == -100):
            print("NoneNone")
            #print(count)
            count = count + 1
            #print(count)
            return count, connected

        while (new_index[0] != -100):
            print(new_index)
            count, connected = self.DFS(new_index[0],new_index[1],grid,connected,count)
            new_index= self.find_neighbour(i,j,grid,connected)
            print(new_index)
        return count, connected

    


    def find_neighbour (self,i,j,grid, connected):
        height = len(grid)
        width = len(grid[0])

        if (i > 0) and grid[i-1][j] == "1" and connected[i-1][j] == False:
            connected[i-1][j] = True
            return (i - 1 , j)
        elif (i < height - 1) and grid[i + 1][j] == "1" and connected[i+1][j] == False:
            connected[i+1][j] = True
            return (i + 1 , j)
        elif (j > 0 ) and grid[i][j - 1] == "1" and connected[i][j - 1] == False:
            connected[i][j -1 ] = True
            return (i , j - 1)
        elif (j < width - 1) and grid[i][j + 1] == "1" and connected[i][j + 1] == False :
            connected[i][j+1 ] = True
            return (i , j + 1)
        
        else :
            return (-100,-100)



grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","1","0"]]
grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
grid3 = [["1","1","1"],["0","1","0"],["0","1","0"]]
obj = Solution()

print(obj.numIslands(grid1))
print(DataFrame(grid1))


