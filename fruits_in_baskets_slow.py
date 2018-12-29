class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if tree == [] :
            return 0
        basket = {}
        candidates = []
        count = 0
        n = len(tree)
        if n == 1:
            return 1
        for i in range(n):
            count = 0
            for j in range (i,n):
                if (tree[j] not in basket.values()) and (len(basket) != 2 ):
                    basket[str(j)] = tree[j]
                    count = count + 1 
                    
                elif (tree[j]) in basket.values():
                    count = count + 1
                else:
                    # reset 
                    basket = {}
                    #count = 0
                    break
                    #basket[str(i)] = tree[i]
                    #count = count + 1
            #print(count)
            candidates.append(count)
        print(max(candidates))
        return (max(candidates))





obj = Solution()
tree = [1,2,1]
tree1 = [0,1,2]
tree2 = [0,1,2,2]
tree3 = [1,2,3,2,2]
tree4 = [1,2,1,1,2]
tree5 = [0,0,1,1]
tree6 = [0,0,0,0]
tree7 = [0]
tree8 = [3,3,3,1,2,1,1,2,3,3,4]
tree9 = [1,1]
tree10 = [0,1,6,6,4,4,6]
obj.totalFruit(tree)
obj.totalFruit(tree1)
obj.totalFruit(tree2) #
obj.totalFruit(tree3)
obj.totalFruit(tree4)
obj.totalFruit(tree5)
obj.totalFruit(tree6)
obj.totalFruit(tree7)
obj.totalFruit(tree8)
obj.totalFruit(tree9)
obj.totalFruit(tree10)  
tree11 = [4,1,1,1,3,1,7,5]    
obj.totalFruit(tree11)   