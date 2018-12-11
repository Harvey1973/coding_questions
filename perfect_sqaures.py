class Solution(object):
    def numSquares(self,n):
        dp = [0]*(n+1)
        p = []
        candidates = []

        for i in range (1,n+1):

            if i**2 > n:
                break
            else :
                p.append(i**2)
        
        for e in p :
            dp[e] = 1
        for j in range (1,n + 1):
            candidates = []
            for e in p :
                #print("e" + str(e))
                if e <= j :
                    candidates.append(dp[j- e])
            
            dp[j] = 1 + min(candidates)

        return dp[-1]
    
perfect_sqaures(13)