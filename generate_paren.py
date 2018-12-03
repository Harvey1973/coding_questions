class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        

        '''
        DP solution
        Idea: dp[i] stores all the possible pair that use i pair of parenthesis 
        '''
        dp = {}
        
        dp[0] = ["()"]
        res = []
        for i in range (1,n):

            size_of_last_dp = len(dp[i-1])
            
            parens = []
            for e in range (size_of_last_dp) : 
                parens.append ('(' + dp[i-1][e] + ')')
                parens.append('(' + ')' + dp[i-1][e])
                parens.append(dp[i-1][e] + '(' + ')')
            print(list(set(parens))) 
            for k in reversed ( range(0,i)):
                counterpart = i - k - 1
                for  p in range (len(dp[k])):
                            
                    for j in range(len(dp[counterpart])):
                        parens.append(dp[k][p] + dp[counterpart][j])
                        parens.append(dp[counterpart][j] + dp[k][p]  )

            dp[i] = list(set(parens)) 
        return dp[n-1]

obj = Solution()
res = obj.generateParenthesis(4)
print(res)


a = ["((())())","(())()()","(()(()))","((()))()","()(()())","()()(())","()(())()","((()()))","(()())()","(()()())","()()()()","()((()))","(((())))"]
b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

print(list(set(b)-set(res)))