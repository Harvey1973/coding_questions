class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [False] * (len(s) + 1)
        dp [0] = True 

        for i in range (len(s)):
            for j in range (len(s)):
                if dp[i] and (s[i:j+1] in wordDict):
                    dp[j+1] = True

        return dp[-1]



s = "catsandog"
wordDict = ["cat", "sand","dog"]
obj = Solution()
print(obj.wordBreak(s,wordDict))