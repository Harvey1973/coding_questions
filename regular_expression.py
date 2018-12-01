class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # construct the dp table 
        m = len(s) + 1
        n = len(p) + 1

        dp = [ [False]*n for _ in range(m)]

        # if both s and p are empty string , then it is a match 
        dp[0][0] = True

        # edge cases , if s is an empty case and p is not
        # for example  s = "" and p = "a*" then this is still a match 
        # since * can repeat a 0 times and thus s = p = ""

        for i in range (2,n):
            dp[0][i] = dp[0][i-2] and p[i-1] == "*"
        
        # start filling the dp table , i.e the non-empty cases 

        # s
        for i in range (1,m):
            # p
            for j in range (1,n):
                if p [j-1] != "*":
                    dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == ".")

                else :
                    # when there is a * , we can have two choices either use the character 
                    # before * or not 

                    # if dont use the char before *
                    dp[i][j] = dp[i][j-2]

                    # if use the char before *
                    if (p[j-2] == s[i-1]) or (p[j-2] == "."):
                        # key point : do not compare it to dp [i-1][j-1]
                        # because p[j-1] = * , it means it has the power to dupilicate or eliminate the previous character
                        # Thus compare dp[i][j] to dp [i-1][j-1] would not be correct
                        # The or operator is to prevent the value being overwritten by dp[i][j] = dp[i][j-2]
                        dp[i][j] |=  dp[i-1][j]
        print(dp)


obj = Solution()

s = "aa"
p = "ab*c*"
obj.isMatch(s,p)