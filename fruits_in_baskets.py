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
        dp = [0] * n
        if n == 1:
            return 1
        dp[0] = 0
        dp[1] = 0
        basket['0'] = tree[0]
        smallest_index = 0
        for i in range(1,n):
            if tree[i] in basket.values():
                dp[i] = dp [i-1]
            else:
                
                if len(basket) < 2:
                    basket['1'] = tree[i]
                    dp[i] = dp [i-1]
                else:
                    smallest_index = i - 1 
                    dp[i] = smallest_index
                    basket['0'] = tree[i]
                    basket['1'] = tree[i-1]
        print(dp)
        for e in range(len(dp)):
            count = e - dp[e] + 1
            candidates.append(count)
        print(max(candidates))





        #    candidates.append(count)
        #return (max(candidates))





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
tree11 = [4,1,1,1,3,1,7,5]
'''
obj.totalFruit(tree)

obj.totalFruit(tree1)

obj.totalFruit(tree2) #

obj.totalFruit(tree3)

obj.totalFruit(tree4)

obj.totalFruit(tree5)

obj.totalFruit(tree6)

obj.totalFruit(tree7)
'''
obj.totalFruit(tree8)

obj.totalFruit(tree9)
obj.totalFruit(tree10)

obj.totalFruit(tree11)
